from datetime import datetime
import uuid
from sqlalchemy.orm.query import Query
from sqlalchemy.orm.session import Session

from sqlalchemy.sql.expression import desc, or_
from typing import List, Optional, Tuple

from src.util.log import LOG
from src.util.context import log_extra
from src.exceptions import AccountNotFoundError, MemberNotFoundError, MembershipAlreadyExist, MembershipNotFoundError, MembershipPending, MembershipStatusNotAllowed, PaymentMethodNotFoundError
from src.constants import CTX_SQL_SESSION, DEFAULT_LIMIT, DEFAULT_OFFSET, MembershipStatus
from src.entity import Membership, PaymentMethod, AbstractMembership, Member, Account
from src.interface_adapter.sql.model.models import Adherent, Membership as MembershipSQL, PaymentMethod as PaymentMethodSQL, Account as SQLAccount
from src.interface_adapter.http_api.decorator.log_call import log_call
from src.use_case.interface.membership_repository import MembershipRepository


class MembershipSQLRepository(MembershipRepository):
    @log_call
    def membership_search_by(self, ctx, limit=DEFAULT_LIMIT, offset=DEFAULT_OFFSET, terms=None,
                             filter_: Optional[AbstractMembership] = None) -> Tuple[List[AbstractMembership], int]:
        LOG.debug("sql_membership_repository_search_membership_called", extra=log_extra(ctx))
        session: Session = ctx.get(CTX_SQL_SESSION)
        query = session.query(MembershipSQL)
        query = query.outerjoin(Adherent, Adherent.id == MembershipSQL.adherent_id)
        if filter_:
            if filter_.uuid is not None:
                query = query.filter(MembershipSQL.uuid == filter_.uuid)
            if filter_.status is not None:
                query = query.filter(MembershipSQL.status == filter_.status)
            if filter_.first_time is not None:
                query = query.filter(MembershipSQL.first_time == filter_.first_time)
            if filter_.duration is not None:
                query = query.filter(MembershipSQL.duration == filter_.duration)
            if filter_.payment_method is not None:
                if isinstance(filter_.payment_method, PaymentMethod):
                    filter_.payment_method = filter_.payment_method.id
                query = query.filter(MembershipSQL.payment_method == filter_.payment_method)
            if filter_.account is not None:
                if isinstance(filter_.account, Account):
                    filter_.account = filter_.account.id
                query = query.filter(MembershipSQL.account == filter_.account)
            if filter_.member is not None:
                if isinstance(filter_.member, Member):
                    filter_.member = filter_.member.id
                query = query.filter(MembershipSQL.adherent_id == filter_.member)

        query = query.order_by(MembershipSQL.uuid)
        query = query.offset(offset)
        query = query.limit(limit)
        r = query.all()

        return list(map(_map_membership_sql_to_abstract_entity, r)), query.count()

    @log_call
    def create_membership(self, ctx, member_id: int, membership: Membership) -> Membership:
        """
        Add a membership record.

        :raise MemberNotFound
        """
        now = datetime.now()
        session: Session = ctx.get(CTX_SQL_SESSION)
        LOG.debug("sql_membership_repository_add_membership_called", extra=log_extra(ctx, member_id=member_id))

        # Check the member exists
        member: Adherent = session.query(Adherent).filter(Adherent.id == member_id).one_or_none()
        if member is None:
            raise MemberNotFoundError(str(member_id))

        # Check the transaction does not already exist
        _membership: Optional[MembershipSQL] = None
        if membership.uuid is not None:
            _membership = session.query(MembershipSQL).filter(MembershipSQL.uuid == membership.uuid).one_or_none()
        if _membership is not None:
            raise MembershipAlreadyExist()

        to_add: MembershipSQL = _map_entity_to_membership_sql(membership)
        to_add.uuid = str(uuid.uuid4())
        to_add.create_at = now
        to_add.update_at = now

        # Check any other membership from this member
        all_membership: List[MembershipSQL] = session.query(MembershipSQL) \
            .filter(MembershipSQL.adherent_id == member_id) \
            .all()

        # Check no other membership are Pending
        for i in all_membership:
            if i.status != MembershipStatus.COMPLETE and i.status != MembershipStatus.ABORTED and membership.status != MembershipStatus.CANCELLED:
                raise MembershipPending(i.uuid)

        to_add.first_time = len(all_membership) == 0
        session.add(to_add)
        session.flush()

        LOG.debug("sql_membership_repository_add_membership_finished", extra=log_extra(ctx, membership_uuid=to_add.uuid))

        return _map_membership_sql_to_entity(to_add)

    def update_membership(self, ctx, member_id: int, membership_uuid: str, abstract_membership: AbstractMembership) -> Membership:
        LOG.debug("sql_membership_repository_update_membership_called", extra=log_extra(ctx, membership_uuid=membership_uuid))
        now = datetime.now()
        session: Session = ctx.get(CTX_SQL_SESSION)
        adherent: Adherent = session.query(Adherent).filter(Adherent.id == member_id).one_or_none()
        if adherent is None:
            raise MemberNotFoundError(str(member_id))
        query: Query = session.query(MembershipSQL).filter(MembershipSQL.uuid == membership_uuid)
        membership: MembershipSQL = query.one_or_none()
        if membership is None:
            raise MembershipNotFoundError(membership_uuid)

        if abstract_membership.duration is not None:
            membership.duration = abstract_membership.duration
        if abstract_membership.products is not None:
            membership.products = str(abstract_membership.products)
        if abstract_membership.account is not None:
            if isinstance(abstract_membership.account, Account):
                abstract_membership.account = abstract_membership.account.id
            account: SQLAccount = session.query(SQLAccount).filter(SQLAccount.id == abstract_membership.account).one_or_none()
            if account is None:
                raise AccountNotFoundError(str(abstract_membership.account))
            membership.account = account
        if abstract_membership.member is not None:
            if isinstance(abstract_membership.member, Member):
                abstract_membership.member = abstract_membership.member.id
            adherent: Adherent = session.query(Adherent).filter(Adherent.id == abstract_membership.member).one_or_none()
            if adherent is None:
                raise MemberNotFoundError(str(abstract_membership.member))
            membership.adherent = adherent
        if abstract_membership.payment_method is not None:
            if isinstance(abstract_membership.payment_method, PaymentMethod):
                abstract_membership.payment_method = abstract_membership.payment_method.id
            payment_method: PaymentMethodSQL = session.query(PaymentMethodSQL).filter(PaymentMethodSQL.id == abstract_membership.payment_method).one_or_none()
            if payment_method is None:
                raise PaymentMethodNotFoundError(str(abstract_membership.payment_method))
            membership.payment_method = payment_method
        if abstract_membership.status is not None:
            membership.status = abstract_membership.status

        membership.update_at = now
        session.flush()

        LOG.debug("sql_membership_repository_update_membership_finished", extra=log_extra(ctx, duration=membership.duration))
        return _map_membership_sql_to_entity(query.one_or_none())

    def validate_membership(self, ctx, membership_uuid: str) -> None:
        session: Session = ctx.get(CTX_SQL_SESSION)
        query: Query = session.query(MembershipSQL).filter(MembershipSQL.uuid == membership_uuid)
        membership: MembershipSQL = query.one_or_none()
        if membership is None:
            raise MembershipNotFoundError(membership_uuid)
        if membership.status != MembershipStatus.PENDING_PAYMENT_VALIDATION:
            raise MembershipStatusNotAllowed(membership.status, "Should be PENDING_PAYMENT_VALIDATION")
        membership.status = MembershipStatus.COMPLETE
        session.flush()
        
    @log_call
    def get_latest_membership(self, ctx, member_id: int) -> Optional[AbstractMembership]:
        session: Session = ctx.get(CTX_SQL_SESSION)
        query = session.query(MembershipSQL).filter(MembershipSQL.adherent_id == member_id).filter(
                or_(
                    MembershipSQL.status == MembershipStatus.PENDING_RULES, 
                    MembershipSQL.status == MembershipStatus.PENDING_PAYMENT, 
                    MembershipSQL.status == MembershipStatus.PENDING_PAYMENT_INITIAL, 
                    MembershipSQL.status == MembershipStatus.PENDING_PAYMENT_VALIDATION
                )
            )
        membership: MembershipSQL = query.one_or_none()
        if membership is None:
            query = session.query(MembershipSQL).filter(MembershipSQL.adherent_id == member_id).filter(
                or_(
                    MembershipSQL.status == MembershipStatus.INITIAL,
                    MembershipSQL.status == MembershipStatus.COMPLETE,
                    MembershipSQL.status == MembershipStatus.ABORTED,
                    MembershipSQL.status == MembershipStatus.CANCELLED,
                )
            ).order_by(desc(MembershipSQL.create_at)).limit(1)
            membership = query.one_or_none()
            if membership is None:
                return None
        
        return _map_membership_sql_to_abstract_entity(membership)


def _map_string_to_list(product_str: str) -> list:
    session = product_str.split(",")
    session[0] = session[0][1:]
    session[-1] = session[-1][:-1]
    return [int(elem) for elem in session if elem != '']


def _map_membership_sql_to_abstract_entity(obj_sql: MembershipSQL) -> AbstractMembership:
    """
    Map a Adherent object from SQLAlchemy to a Member (from the entity folder/layer).
    """
    return AbstractMembership(
        uuid=str(obj_sql.uuid),
        duration=obj_sql.duration,
        has_room=obj_sql.has_room,
        products=_map_string_to_list(obj_sql.products),
        first_time=obj_sql.first_time,
        payment_method=obj_sql.payment_method.id if obj_sql.payment_method else None,
        account=obj_sql.account.id if obj_sql.account else None,
        member=obj_sql.adherent.id if obj_sql.adherent else None,
        status=obj_sql.status if isinstance(obj_sql.status, str) else obj_sql.status.value,
    )

def _map_membership_sql_to_entity(obj_sql: MembershipSQL) -> Membership:
    """
    Map a Adherent object from SQLAlchemy to a Member (from the entity folder/layer).
    """
    return Membership(
        uuid=str(obj_sql.uuid),
        duration=obj_sql.duration,
        has_room=obj_sql.has_room,
        products=_map_string_to_list(obj_sql.products),
        first_time=obj_sql.first_time,
        payment_method=obj_sql.payment_method.id if obj_sql.payment_method else None,
        account=obj_sql.account.id if obj_sql.account else None,
        member=obj_sql.adherent.id if obj_sql.adherent else None,
        status=obj_sql.status if isinstance(obj_sql.status, str) else obj_sql.status.value,
    )


def _map_entity_to_membership_sql(entity: Membership) -> MembershipSQL:
    """
    Map a Adherent object from SQLAlchemy to a Member (from the entity folder/layer).
    """
    return MembershipSQL(
        uuid=entity.uuid,
        duration=entity.duration,
        has_room=entity.has_room if entity is not None else False,
        products=str(entity.products) if entity.products is not None else "",
        first_time=entity.first_time,
        payment_method_id=entity.payment_method,
        account_id=entity.account,
        adherent_id=entity.member,
        status=entity.status,
        create_at=entity.created_at,
        update_at=entity.updated_at
    )
