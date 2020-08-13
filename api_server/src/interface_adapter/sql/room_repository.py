# coding=utf-8
"""
Implements everything related to actions on the SQL database.
"""
from datetime import datetime
from typing import List

from src.constants import CTX_SQL_SESSION, DEFAULT_LIMIT, DEFAULT_OFFSET
from src.entity import AbstractRoom
from src.entity.null import Null
from src.entity.room import Room
from src.exceptions import RoomNotFoundError, VLANNotFoundError
from src.interface_adapter.http_api.decorator.log_call import log_call
from src.interface_adapter.sql.model.models import Chambre, Vlan
from src.interface_adapter.sql.track_modifications import track_modifications
from src.use_case.interface.room_repository import RoomRepository


class RoomSQLRepository(RoomRepository):

    @log_call
    def search_by(self, ctx, limit=DEFAULT_LIMIT, offset=DEFAULT_OFFSET, terms=None,
                  filter_: AbstractRoom = None) -> (List[Room], int):
        s = ctx.get(CTX_SQL_SESSION)

        q = s.query(Chambre)

        if filter_.id is not None:
            q = q.filter(Chambre.id == filter_.id)
        if terms:
            q = q.filter(Chambre.description.contains(terms))
        if filter_.description:
            q = q.filter(Chambre.description.contains(filter_.description))
        if filter_.room_number is not None:
            q = q.filter(Chambre.numero == filter_.room_number)


        count = q.count()
        q = q.order_by(Chambre.numero.asc())
        q = q.offset(offset)
        q = q.limit(limit)
        r = q.all()

        return list(map(_map_room_sql_to_entity, r)), count

    @log_call
    def create(self, ctx, abstract_room: Room) -> object:
        s = ctx.get(CTX_SQL_SESSION)
        now = datetime.now()

        vlan = None
        if abstract_room.vlan is not None:
            vlan = s.query(Vlan).filter(Vlan.numero == abstract_room.vlan).one_or_none()
            if not vlan:
                raise VLANNotFoundError(str(abstract_room.vlan))

        room = Chambre(
            numero=abstract_room.room_number,
            description=abstract_room.description,
            created_at=now,
            updated_at=now,
            vlan=vlan,
        )

        with track_modifications(ctx, s, room):
            s.add(room)

        return _map_room_sql_to_entity(room)

    @log_call
    def update(self, ctx, abstract_room: AbstractRoom, override=False) -> object:
        raise NotImplementedError

    @log_call
    def delete(self, ctx, room_id) -> None:
        s = ctx.get(CTX_SQL_SESSION)

        room = s.query(Chambre).filter(Chambre.id == room_id).one_or_none()
        if room is None:
            raise RoomNotFoundError(room_id)

        with track_modifications(ctx, s, room):
            s.delete(room)


def _map_room_sql_to_entity(r: Chambre) -> Room:
    return Room(
        id=r.id,
        room_number=r.numero,
        description=r.description,
        vlan=r.vlan.numero if r.vlan is not None else Null()
    )
