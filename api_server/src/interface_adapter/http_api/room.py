# coding=utf-8
from connexion import NoContent

from src.constants import DEFAULT_LIMIT, DEFAULT_OFFSET
from src.exceptions import RoomNotFoundError, UserInputError
from src.interface_adapter.http_api.decorator.with_context import with_context
from src.interface_adapter.http_api.util.error import bad_request
from src.interface_adapter.http_api.util.serializer import serialize_response
from src.interface_adapter.sql.decorator.auth import auth_regular_admin, auth_super_admin
from src.interface_adapter.sql.decorator.sql_session import require_sql
from src.use_case.room_manager import MutationRequest, RoomManager
from src.util.context import log_extra
from src.util.log import LOG


class RoomHandler:
    def __init__(self, room_manager: RoomManager):
        self.room_manager = room_manager

    @with_context
    @require_sql
    @auth_regular_admin
    def search(self, ctx, limit=DEFAULT_LIMIT, offset=DEFAULT_OFFSET, terms=None, filter_=None):
        """ Filter the list of the rooms """
        LOG.debug("http_room_search_called", extra=log_extra(ctx, limit=limit, offset=offset, terms=terms, filter_=filter_))
        try:
            result, count = self.room_manager.search(ctx, limit=limit, offset=offset, terms=terms)
            result = map(serialize_response, result)
            result = list(result)
            headers = {
                'access-control-expose-headers': 'X-Total-Count',
                'X-Total-Count': str(count)
            }
            return result, 200, headers

        except UserInputError as e:
            return bad_request(e), 400

    @with_context
    @require_sql
    @auth_regular_admin
    def post(self, ctx, body):
        pass

    @with_context
    @require_sql
    @auth_super_admin
    def put(self, ctx, room_number, body):
        """ Update/create a room in the database """
        LOG.debug("http_room_put_called", extra=log_extra(ctx, room_number=room_number, request=body))
        try:
            created = self.room_manager.update_or_create(ctx, room_number, MutationRequest(
                room_number=body.get('room_number'),
                description=body.get('description'),
                vlan_number=body.get('vlan'),
            ))
            if created:
                return NoContent, 201
            else:
                return NoContent, 204

        except UserInputError as e:
            return bad_request(e), 400

    @with_context
    @require_sql
    @auth_regular_admin
    def get(self, ctx, room_number):
        """ Get the room specified """
        LOG.debug("http_room_get_called", extra=log_extra(ctx, room_number=room_number))
        try:
            result = self.room_manager.get_by_number(ctx, room_number)
            return serialize_response(result), 200

        except RoomNotFoundError:
            return NoContent, 404

    @with_context
    @require_sql
    @auth_super_admin
    def delete(self, ctx, room_number):
        """ Delete room from the database """
        LOG.debug("http_room_delete_called", extra=log_extra(ctx, room_number=room_number))
        try:
            self.room_manager.delete(ctx, room_number)
            return NoContent, 204

        except RoomNotFoundError:
            return NoContent, 404
