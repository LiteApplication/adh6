# coding=utf-8
from dataclasses import asdict

from connexion import NoContent

from src.constants import DEFAULT_LIMIT, DEFAULT_OFFSET
from src.entity.account import Account
from src.exceptions import AccountNotFoundError, UserInputError
from src.interface_adapter.http_api.decorator.with_context import with_context
from src.interface_adapter.http_api.member import _map_member_to_http_response
from src.interface_adapter.http_api.util.error import bad_request
from src.interface_adapter.sql.decorator.auth import auth_regular_admin
from src.interface_adapter.sql.decorator.sql_session import require_sql
from src.use_case.account_manager import PartialMutationRequest, AccountManager, FullMutationRequest
from src.use_case.transaction_manager import TransactionManager
from src.util.context import log_extra
from src.util.log import LOG


class AccountHandler:
    def __init__(self, account_manager: AccountManager, transaction_manager: TransactionManager):
        self.account_manager = account_manager
        self.transaction_manager = transaction_manager

    @with_context
    @require_sql
    @auth_regular_admin
    def search(self, ctx, limit=DEFAULT_LIMIT, offset=DEFAULT_OFFSET, terms=None, pinned=None):

        LOG.debug("http_account_search_called", extra=log_extra(ctx,
                                                                limit=limit,
                                                                offset=offset,
                                                                pinned=None,
                                                                terms=terms))
        try:
            result, count = self.account_manager.search(ctx, account_id=None, terms=terms, pinned=None)
            headers = {
                "X-Total-Count": count,
                'access-control-expose-headers': 'X-Total-Count'
            }
            return list(map(_map_account_to_http_response, result)), 200, headers

        except UserInputError as e:
            return bad_request(e), 400  # 400 Bad Request

    @with_context
    @require_sql
    @auth_regular_admin
    def post(self, ctx, body):
        """ Add an account record in the database """
        LOG.debug("http_account_post_called", extra=log_extra(ctx, request=body))

        try:
            created = self.account_manager.update_or_create(ctx, req=FullMutationRequest(
                name=body.get('name'),
                type=body.get('type_'),
                actif=body.get('actif'),
                creation_date=body.get('creation_date')),
                                                            account_id=body.get('account_id'))
            if created:
                return NoContent, 201  # 201 Created
            else:
                return NoContent, 204  # 204 No Content

        except UserInputError as e:
            return bad_request(e), 400  # 400 Bad Request

    @with_context
    @require_sql
    @auth_regular_admin
    def get(self, ctx, account_id):
        """ Get a specific account. """
        LOG.debug("http_account_get_called", extra=log_extra(ctx, account_id=account_id))
        try:
            result = self.account_manager.get_by_id(ctx, account_id)
            return _map_account_to_http_response(result), 200  # 200 OK
        except AccountNotFoundError:
            return NoContent, 404  # 404 Not Found

    @with_context
    @require_sql
    @auth_regular_admin
    def put(self, ctx, account_id, body):
        """ Partially update an account from the database """
        LOG.debug("http_account_patch_called", extra=log_extra(ctx, account_id=account_id, request=body))
        try:
            mutation_request = _map_http_request_to_full_mutation_request(body)
            self.account_manager.update_or_create(ctx, mutation_request, account_id)
            return NoContent, 204  # 204 No Content

        except AccountNotFoundError:
            return NoContent, 404  # 404 Not Found


def _map_http_request_to_partial_mutation_request(body) -> PartialMutationRequest:
    return PartialMutationRequest(
        name=body.get('name'),
        type=body.get('type_'),
        actif=body.get('actif'),
        creation_date=body.get('creation_date'),
    )


def _map_account_to_http_response(account: Account) -> dict:
    fields = {
        'name': account.name,
        'creation_date': account.creation_date,
        'actif': account.actif,
        'type': account.type,
        'id': account.account_id,
        'adherent': _map_member_to_http_response(account.adherent) if account.adherent else None,
        'balance': account.balance,
        'compte_courant': account.compte_courant,
        'pinned': account.pinned
    }
    return {k: v for k, v in fields.items() if v is not None}


def _map_http_request_to_full_mutation_request(body) -> FullMutationRequest:
    partial = _map_http_request_to_partial_mutation_request(body)
    return FullMutationRequest(**asdict(partial))
