# coding=utf-8
"""
Implements everything related to actions on the SQL database.
"""
from datetime import datetime
from typing import List

from src.constants import CTX_SQL_SESSION, DEFAULT_LIMIT, DEFAULT_OFFSET
from src.entity import AbstractDevice
from src.entity.device import Device
from src.exceptions import DeviceNotFoundError, MemberNotFoundError
from src.interface_adapter.http_api.decorator.log_call import log_call
from src.interface_adapter.sql.member_repository import _map_member_sql_to_entity
from src.interface_adapter.sql.model.models import Device as SQLDevice, Adherent
from src.interface_adapter.sql.track_modifications import track_modifications
from src.use_case.interface.device_repository import DeviceRepository


class DeviceSQLRepository(DeviceRepository):

    @log_call
    def search_by(self, ctx, limit=DEFAULT_LIMIT, offset=DEFAULT_OFFSET, terms=None,
                  filter_: AbstractDevice = None) -> (List[Device], int):
        s = ctx.get(CTX_SQL_SESSION)

        q = s.query(SQLDevice)
        q = q.join(Adherent, Adherent.id == SQLDevice.adherent_id)

        if filter_.id is not None:
            q = q.filter(SQLDevice.id == filter_.id)
        if terms:
            q = q.filter(
                (SQLDevice.mac.contains(terms)) |
                (SQLDevice.ip.contains(terms)) |
                (SQLDevice.ipv6.contains(terms)) |
                (Adherent.login.contains(terms))
            )
        if filter_.mac:
            q = q.filter(SQLDevice.mac == filter_.mac)
        if filter_.connection_type:
            q = q.filter(SQLDevice.type == filter_.connection_type)

        count = q.count()
        q = q.offset(offset)
        q = q.order_by(SQLDevice.created_at.asc())
        q = q.limit(limit)
        r = q.all()

        return list(map(_map_device_sql_to_entity, r)), count

    @log_call
    def create(self, ctx, abstract_device: Device) -> object:
        s = ctx.get(CTX_SQL_SESSION)

        now = datetime.now()

        adherent = None
        if abstract_device.member is not None:
            adherent = s.query(Adherent).filter(Adherent.id == abstract_device.member).one_or_none()
            if not adherent:
                raise MemberNotFoundError(abstract_device.member)

        device = SQLDevice(
            mac=abstract_device.mac,
            created_at=now,
            updated_at=now,
            last_seen=now,
            type=abstract_device.connection_type,
            adherent=adherent
        )

        with track_modifications(ctx, s, device):
            s.add(device)

        return _map_device_sql_to_entity(device)

    def update(self, ctx, abstract_device: AbstractDevice, override=False) -> object:
        raise NotImplemented

    @log_call
    def delete(self, ctx, device_id) -> None:
        s = ctx.get(CTX_SQL_SESSION)

        device = s.query(Device).filter(Device.id == device_id).one_or_none()
        if device is None:
            raise DeviceNotFoundError(device_id)

        with track_modifications(ctx, s, device):
            s.delete(device)


def _map_device_sql_to_entity(d) -> Device:
    """
    Map a Device object from SQLAlchemy to a Device (from the entity folder/layer).
    """
    return Device(
        id=d.id,
        mac=d.mac,
        member=_map_member_sql_to_entity(d.adherent),
        connection_type=d.type,
        ipv4_address=d.ip,
        ipv6_address=d.ipv6,
    )
