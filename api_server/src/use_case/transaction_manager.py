# coding=utf-8
""" Use cases (business rule layer) of everything related to transactions. """
from typing import Optional, Tuple
from src.constants import CTX_ROLES
from src.entity import AbstractTransaction
from src.entity.transaction import Transaction
from src.exceptions import TransactionNotFoundError, ValidationError, IntMustBePositive
from src.interface_adapter.http_api.decorator.log_call import log_call
from src.use_case.crud_manager import CRUDManager
from src.use_case.decorator.auto_raise import auto_raise
from src.use_case.decorator.security import SecurityDefinition, Roles, defines_security, has_any_role, is_admin, uses_security
from src.use_case.interface.cashbox_repository import CashboxRepository
from src.use_case.interface.transaction_repository import TransactionRepository
from src.util.context import log_extra
from src.util.log import LOG


@defines_security(SecurityDefinition(
    item={
        "read": is_admin(),
        "update": has_any_role([Roles.TRESO]),
        "delete": has_any_role([Roles.TRESO])
    },
    collection={
        "read": is_admin(),
        "create": is_admin(),
    }
))
class TransactionManager(CRUDManager):
    """
    Implements all the use cases related to transaction management.
    """

    def __init__(self, transaction_repository: TransactionRepository, cashbox_repository: CashboxRepository):
        super().__init__(transaction_repository, AbstractTransaction, TransactionNotFoundError)
        self.transaction_repository = transaction_repository
        self.cashbox_repository = cashbox_repository

    @log_call
    @auto_raise
    def update_or_create(self, ctx, abstract_transaction: AbstractTransaction, id: Optional[int] = None) -> Tuple[Transaction, bool]:
        if abstract_transaction.src == abstract_transaction.dst:
            raise ValidationError('the source and destination accounts must not be the same')
        if abstract_transaction.value is None:
            raise ValidationError('the value field should not be None')
        if abstract_transaction.value <= 0:
            raise IntMustBePositive('value')

        if Roles.TRESO.value not in ctx.get(CTX_ROLES):
            abstract_transaction.pending_validation = True

        transaction, created = super().update_or_create(ctx, abstract_transaction, id=id)

        if created:
            LOG.info('cashbox_update', extra=log_extra(
                ctx,
                value_modifier=abstract_transaction.value,
                transaction=transaction,
            ))
            if transaction.cashbox == "to":
                self.cashbox_repository.update(ctx, value_modifier=transaction.value, transaction=transaction)
            elif transaction.cashbox == "from":
                self.cashbox_repository.update(ctx, value_modifier=-transaction.value, transaction=transaction)
                
        return transaction, created

    @log_call
    @auto_raise
    def partially_update(self, ctx, abstract_transaction: AbstractTransaction, id=None, override=False, **kwargs):
        if any(True for _ in filter(lambda e: e is not None, [
            abstract_transaction.value,
            abstract_transaction.src,
            abstract_transaction.dst,
            abstract_transaction.timestamp,
            abstract_transaction.payment_method,
            abstract_transaction.cashbox,
            abstract_transaction.author,
        ])):
            raise ValidationError('you are trying to update a transaction with fields that cannot be updated')
        raise NotImplementedError

    @log_call
    @auto_raise
    def validate(self, ctx, id: int):
        transaction = self.get_by_id(ctx, id=id)
        if not transaction.pending_validation:
            raise ValidationError("you are trying to validate a transaction that is already validated")

        @uses_security("update", is_collection=False)
        def _validate(cls, ctx, id):
            self.transaction_repository.validate(ctx, id)

        return _validate(self, ctx, id)

    @log_call
    @auto_raise
    def delete(self, ctx, id: int):
        transaction = self.get_by_id(ctx, id=id)
        if not transaction.pending_validation:
            raise ValidationError("you are trying to delete a transaction that is already validated")

        return super().delete(ctx, id=id)
