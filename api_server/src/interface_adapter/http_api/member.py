# coding=utf-8
"""
Contain all the http http_api functions.
"""
from connexion import NoContent
from dataclasses import asdict

from main import member_manager
from src.interface_adapter.http_api.decorator.auth import auth_regular_admin
from src.interface_adapter.http_api.decorator.sql_session import require_sql
from src.interface_adapter.http_api.decorator.with_context import with_context
from src.interface_adapter.http_api.util.error import bad_request
from src.util.log import LOG
from src.use_case.member_manager import MutationRequest, UsernameMismatchError, MissingRequiredFieldError, \
    PasswordTooShortError, InvalidRoomNumberError, InvalidEmailError, \
    MemberNotFound, IntMustBePositiveException, StringMustNotBeEmptyException, NoPriceAssignedToThatDurationException
from src.use_case.mutation import Mutation
from src.util.context import log_extra
from src.util.date import string_to_date


@with_context
@require_sql
@auth_regular_admin
def search(ctx, limit=100, offset=0, terms=None, roomNumber=None):
    """ Search all the member. """
    LOG.debug("http_member_search_called", extra=log_extra(ctx,
                                                           limit=limit,
                                                           offset=offset,
                                                           terms=terms,
                                                           roomNumber=roomNumber))
    try:
        result, total_count = member_manager.search(ctx, limit, offset, roomNumber, terms)
        headers = {
            "X-Total-Count": str(total_count),
            'access-control-expose-headers': 'X-Total-Count'
        }
        result = list(map(asdict, result))
        return result, 200, headers  # 200 OK

    except IntMustBePositiveException as e:
        return bad_request(e), 400  # 400 Bad Request


@with_context
@require_sql
@auth_regular_admin
def get(ctx, username):
    """ Get a specific member. """
    LOG.debug("http_member_get_called", extra=log_extra(ctx, username=username))
    try:
        return asdict(member_manager.get_by_username(ctx, username)), 200  # 200 OK

    except MemberNotFound:
        return NoContent, 404  # 404 Not Found


@with_context
@require_sql
@auth_regular_admin
def delete(ctx, username):
    """ Delete the specified User from the database """
    LOG.debug("http_member_delete_called", extra=log_extra(ctx, username=username))
    try:
        member_manager.delete(ctx, username)
        return NoContent, 204  # 204 No Content

    except MemberNotFound:
        return NoContent, 404  # 404 Not Found


@with_context
@require_sql
@auth_regular_admin
def patch(ctx, username, body):
    """ Partially update a member from the database """
    LOG.debug("http_member_patch_called", extra=log_extra(ctx, username=username, request=body))
    try:
        mutation_request = _map_body_to_mutation_request(body)
        member_manager.update_partially(ctx, username, mutation_request)
        return NoContent, 204  # 204 No Content

    except MemberNotFound:
        return NoContent, 404  # 404 Not Found


@with_context
@require_sql
@auth_regular_admin
def put(ctx, username, body):
    """ Create/Update member from the database """
    LOG.debug("http_member_put_called", extra=log_extra(ctx, username=username, request=body))

    mutation_request = _map_body_to_mutation_request(body)
    try:
        created = member_manager.update_or_create(ctx, username, mutation_request)
        if created:
            return NoContent, 201  # 201 Created
        else:
            return NoContent, 204  # 204 No Content

    except (InvalidRoomNumberError, MissingRequiredFieldError, UsernameMismatchError, InvalidEmailError,
            StringMustNotBeEmptyException) as e:
        return bad_request(e), 400  # 400 Bad Request


@with_context
@require_sql
@auth_regular_admin
def post_membership(ctx, username, body):
    """ Add a membership record in the database """
    LOG.debug("http_member_post_membership_called", extra=log_extra(ctx, username=username, request=body))

    try:
        member_manager.new_membership(ctx, username, body.get('duration'), start_str=body.get('start'))

    except MemberNotFound as e:
        return NoContent, 404  # 404 Not Found

    except (IntMustBePositiveException, NoPriceAssignedToThatDurationException) as e:
        return bad_request(e), 400  # 400 Bad Request

    return NoContent, 200  # 200 OK


@with_context
@require_sql
@auth_regular_admin
def put_password(ctx, username, body):
    """ Set the password of a member. """
    # Careful not to log the body here!
    LOG.debug("http_member_put_password_called", extra=log_extra(ctx, username=username, body=None))

    try:
        member_manager.change_password(ctx, username, body.get('password'))

    except MemberNotFound:
        return NoContent, 404  # 404 Not Found

    except PasswordTooShortError as e:
        return bad_request(e), 400  # 400 Bad Request

    return NoContent, 204  # 204 No Content


@with_context
@require_sql
@auth_regular_admin
def get_logs(ctx, username):
    """ Get logs from a member. """
    LOG.debug("http_member_get_logs_called", extra=log_extra(ctx, username=username))
    try:
        return member_manager.get_logs(ctx, username), 200

    except MemberNotFound:
        return NoContent, 404


def _map_body_to_mutation_request(body) -> MutationRequest:
    return MutationRequest(
        email=body.get('email', Mutation.NOT_SET),
        first_name=body.get('firstName', Mutation.NOT_SET),
        last_name=body.get('lastName', Mutation.NOT_SET),
        username=body.get('username', Mutation.NOT_SET),
        departure_date=_string_to_date_or_unset(body.get('departureDate')),
        comment=body.get('comment', Mutation.NOT_SET),
        association_mode=_string_to_date_or_unset(body.get('associationMode')),
        room_number=body.get('roomNumber', Mutation.NOT_SET),
    )


def _string_to_date_or_unset(d):
    if d is None:
        return Mutation.NOT_SET

    if isinstance(d, str):
        return string_to_date(d)

    return d
