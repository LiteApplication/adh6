# coding=utf-8
import typing as t
import abc

from adh6.entity import Room, AbstractRoom, Member
from adh6.default import CRUDRepository


class RoomRepository(CRUDRepository[Room, AbstractRoom]):
    @abc.abstractmethod
    def get_by_number(self, room_number: int) -> t.Union[Room, None]:
        pass  # pragma: no cover

    @abc.abstractmethod
    def get_from_member(self, member: Member) -> t.Union[Room, None]:
        pass  # pragma: no cover

    @abc.abstractmethod
    def get_members(self, room_id: int) -> t.List[int]:
        pass  # pragma: no cover

    @abc.abstractmethod
    def add_member(self, room_id: int, member: Member) -> None:
        pass  # pragma: no cover

    @abc.abstractmethod
    def remove_member(self, member: Member) -> None:
        pass  # pragma: no cover
