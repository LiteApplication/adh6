# coding=utf-8
import abc

from src.entity.vlan import Vlan


class VLANRepository(metaclass=abc.ABCMeta):
    """
    Abstract interface to handle VLANs.
    """

    @abc.abstractmethod
    def get_vlan(self, ctx, vlan_number: int) -> Vlan:
        """
        Get a VLAN.

        :raise VlanNotFound
        """
        pass  # pragma: no cover
