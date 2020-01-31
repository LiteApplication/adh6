# coding=utf-8
"""
Room repository.
"""
import abc
from typing import List

from src.constants import DEFAULT_LIMIT, DEFAULT_OFFSET
from src.entity.room import Room


class RoomRepository(metaclass=abc.ABCMeta):
    """
    Abstract interface to handle rooms.
    """

    @abc.abstractmethod
    def search_room_by(self, ctx, limit=DEFAULT_LIMIT, offset=DEFAULT_OFFSET, room_number=None, owner_username=None,
                       terms=None) -> (
            List[Room], int):
        """
        Search rooms.
        """
        pass  # pragma: no cover

    @abc.abstractmethod
    def update_room(self, ctx, room_to_update, room_number=None, description=None,
                    vlan_number=None) -> None:
        """
        Update a room.
        """
        pass  # pragma: no cover

    @abc.abstractmethod
    def create_room(self, ctx, room_number=None, description=None, vlan_number=None) -> None:
        """
        Create a room.
        """
        pass  # pragma: no cover

    @abc.abstractmethod
    def delete_room(self, ctx, room_number) -> None:
        """
        Delete a room.
        """
        pass  # pragma: no cover
