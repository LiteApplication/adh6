# coding=utf-8
"""
Implements everything related to actions on the SQL database.
"""
from typing import List

from src.constants import CTX_SQL_SESSION, DEFAULT_LIMIT, DEFAULT_OFFSET
from src.entity.device import Device
from src.interface_adapter.sql.model.models import Adherent
from src.interface_adapter.sql.util.device_helper import get_all_devices, update_wired_device, \
    update_wireless_device, delete_wired_device, create_wireless_device, delete_wireless_device, create_wired_device
from src.interface_adapter.sql.util.ip_controller import get_available_ip, get_all_used_ipv4, get_all_used_ipv6
from src.use_case.interface.device_repository import DeviceRepository
from src.use_case.interface.ip_allocator import IPAllocator
from src.exceptions import NoMoreIPAvailableException, DeviceAlreadyExist, DeviceNotFoundError
from src.util.context import log_extra
from src.util.log import LOG


class DeviceSQLRepository(DeviceRepository, IPAllocator):

    def search_device_by(self, ctx, limit=DEFAULT_LIMIT, offset=DEFAULT_OFFSET, mac_address=None, username=None,
                         terms=None) \
            -> (List[Device], int):
        LOG.debug("sql_device_repository_search_called", extra=log_extra(ctx))
        s = ctx.get(CTX_SQL_SESSION)

        # Return a subquery with all devices (wired & wireless)
        # The fields, ip, ipv6, dns, etc, are set to None for wireless devices
        # There is also a field "type" wich is wired and wireless
        all_devices = get_all_devices(s)

        # Query all devices and their owner's unsername
        q = s.query(all_devices, Adherent.login.label("login"))
        q = q.join(Adherent, Adherent.id == all_devices.columns.adherent_id)

        if mac_address:
            q = q.filter(all_devices.columns.mac == mac_address)

        if username:
            q = q.filter(Adherent.login == username)

        if terms:
            q = q.filter(
                (all_devices.columns.mac.contains(terms)) |
                (all_devices.columns.ip.contains(terms)) |
                (all_devices.columns.ipv6.contains(terms)) |
                (Adherent.login.contains(terms))
            )
        count = q.count()
        q = q.order_by(all_devices.columns.mac.asc())
        q = q.offset(offset)
        q = q.limit(limit)
        r = q.all()
        results = list(map(_map_device_sql_to_entity, r))

        return results, count

    def create_device(self, ctx, mac_address=None, owner_username=None, connection_type=None, ip_v4_address=None,
                      ip_v6_address=None):
        LOG.debug("sql_device_repository_create_device_called", extra=log_extra(ctx, mac=mac_address))
        s = ctx.get(CTX_SQL_SESSION)

        all_devices = get_all_devices(s)
        device = s.query(all_devices).filter(all_devices.columns.mac == mac_address).one_or_none()

        if device is not None:
            raise DeviceAlreadyExist()

        # If the user do not change the connection type, we just need to update...
        if connection_type == 'wired':
            create_wired_device(
                ctx,
                s=s,
                mac_address=mac_address,
                ip_v4_address=ip_v4_address or 'En Attente',
                ip_v6_address=ip_v6_address or 'En Attente',
                username=owner_username,
            )
        else:
            create_wireless_device(
                ctx,
                s=s,
                mac_address=mac_address,
                username=owner_username,
            )

    def update_device(self, ctx, device_to_update, mac_address=None, owner_username=None, connection_type=None,
                      ip_v4_address=None, ip_v6_address=None):
        s = ctx.get(CTX_SQL_SESSION)
        LOG.debug("sql_device_repository_update_device_called", extra=log_extra(ctx, mac=device_to_update))

        all_devices = get_all_devices(s)
        device = s.query(all_devices).filter(all_devices.columns.mac == device_to_update).one_or_none()

        if device is None:
            return DeviceNotFoundError(device_to_update)

        # If the user do not change the connection type, we just need to update...
        if device.type == connection_type:
            if connection_type == 'wired':
                update_wired_device(
                    ctx,
                    s=s,
                    device_to_update=device_to_update,
                    mac_address=mac_address,
                    ip_v4_address=ip_v4_address or 'En Attente',
                    ip_v6_address=ip_v6_address or 'En Attente',
                    username=owner_username,
                )
            else:
                update_wireless_device(
                    ctx,
                    device_to_update=device_to_update,
                    s=s,
                    mac_address=mac_address,
                    username=owner_username,
                )
            return

        # If the user change the connection type, we have to move the Device row from one table to another
        # (Wired table to Wireless table or the other way around)
        # To do that, we first delete the device and then re-create it in the other table.
        if device.type == 'wired':
            delete_wired_device(
                ctx,
                s=s,
                mac_address=device_to_update,
            )
            create_wireless_device(
                ctx,
                s=s,
                mac_address=device_to_update,
                username=owner_username,
            )
        else:
            delete_wireless_device(
                ctx,
                s=s,
                mac_address=device_to_update,
            )
            create_wired_device(
                ctx,
                s=s,
                mac_address=device_to_update,
                ip_v4_address=ip_v4_address,
                ip_v6_address=ip_v6_address,
                username=owner_username,
            )

    def delete_device(self, ctx, mac_address=None):
        s = ctx.get(CTX_SQL_SESSION)
        LOG.debug("sql_device_repository_delete_device_called", extra=log_extra(ctx, mac=mac_address))

        all_devices = get_all_devices(s)
        device = s.query(all_devices).filter(all_devices.columns.mac == mac_address).one_or_none()
        if not device:
            raise DeviceNotFoundError(mac_address)

        if device.type == 'wired':
            delete_wired_device(ctx, s, mac_address)
        else:
            delete_wireless_device(ctx, s, mac_address)

    def allocate_ip_v4(self, ctx, ip_range: str) -> str:
        s = ctx.get(CTX_SQL_SESSION)
        LOG.debug("sql_device_repository_allocate_ip_v4_called", extra=log_extra(ctx))

        result = get_available_ip(ip_range, get_all_used_ipv4(s))
        if result is None:
            raise NoMoreIPAvailableException()

        return result

    def allocate_ip_v6(self, ctx, ip_range: str) -> str:
        s = ctx.get(CTX_SQL_SESSION)
        LOG.debug("sql_device_repository_allocate_ip_v6_called", extra=log_extra(ctx))

        result = get_available_ip(ip_range, get_all_used_ipv6(s))
        if result is None:
            raise NoMoreIPAvailableException()

        return result


def _map_device_sql_to_entity(d) -> Device:
    """
    Map a Device object from SQLAlchemy to a Device (from the entity folder/layer).
    """
    t = 'wired'
    if d.type == 'wireless':
        t = 'wireless'
    return Device(
        mac_address=d.mac,
        owner_username=d.login,
        connection_type=t,
        ip_v4_address=d.ip,
        ip_v6_address=d.ipv6,
    )
