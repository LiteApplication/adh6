# coding: utf-8

"""
    ADH6 API

    This is the specification for **MiNET**'s ADH6 plaform. Its aim is to manage our users, devices and treasury.   # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: equipe@minet.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

from src.entity.decorator.entity_property import entity_property as property

from src.entity import AbstractVlan


class Vlan(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'number': 'int',
        'ipv4_network': 'str',
        'ipv6_network': 'str'
    }
    if hasattr(AbstractVlan, "swagger_types"):
        swagger_types.update(AbstractVlan.swagger_types)

    attribute_map = {
        'id': 'id',
        'number': 'number',
        'ipv4_network': 'ipv4Network',
        'ipv6_network': 'ipv6Network'
    }
    if hasattr(AbstractVlan, "attribute_map"):
        attribute_map.update(AbstractVlan.attribute_map)

    def __init__(self, id=None, number=None, ipv4_network=None, ipv6_network=None, *args, **kwargs):  # noqa: E501
        """Vlan - a model defined in Swagger"""  # noqa: E501
        AbstractVlan.__init__(self, *args, **kwargs)
        self._id = None
        self._number = None
        self._ipv4_network = None
        self._ipv6_network = None
        self.discriminator = None
        self.id = id
        self.number = number
        self.ipv4_network = ipv4_network
        self.ipv6_network = ipv6_network

    @property
    def id(self):
        """Gets the id of this Vlan.  # noqa: E501

        The unique identifier of this vlan  # noqa: E501

        :return: The id of this Vlan.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Vlan.

        The unique identifier of this vlan  # noqa: E501

        :param id: The id of this Vlan.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def number(self):
        """Gets the number of this Vlan.  # noqa: E501

        The number of this VLAN  # noqa: E501

        :return: The number of this Vlan.  # noqa: E501
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this Vlan.

        The number of this VLAN  # noqa: E501

        :param number: The number of this Vlan.  # noqa: E501
        :type: int
        """
        if number is None:
            raise ValueError("Invalid value for `number`, must not be `None`")  # noqa: E501

        self._number = number

    @property
    def ipv4_network(self):
        """Gets the ipv4_network of this Vlan.  # noqa: E501

        The IPv4 network range for this VLAN  # noqa: E501

        :return: The ipv4_network of this Vlan.  # noqa: E501
        :rtype: str
        """
        return self._ipv4_network

    @ipv4_network.setter
    def ipv4_network(self, ipv4_network):
        """Sets the ipv4_network of this Vlan.

        The IPv4 network range for this VLAN  # noqa: E501

        :param ipv4_network: The ipv4_network of this Vlan.  # noqa: E501
        :type: str
        """
        if ipv4_network is None:
            raise ValueError("Invalid value for `ipv4_network`, must not be `None`")  # noqa: E501

        self._ipv4_network = ipv4_network

    @property
    def ipv6_network(self):
        """Gets the ipv6_network of this Vlan.  # noqa: E501

        The IPv6 network range for this VLAN  # noqa: E501

        :return: The ipv6_network of this Vlan.  # noqa: E501
        :rtype: str
        """
        return self._ipv6_network

    @ipv6_network.setter
    def ipv6_network(self, ipv6_network):
        """Sets the ipv6_network of this Vlan.

        The IPv6 network range for this VLAN  # noqa: E501

        :param ipv6_network: The ipv6_network of this Vlan.  # noqa: E501
        :type: str
        """
        if ipv6_network is None:
            raise ValueError("Invalid value for `ipv6_network`, must not be `None`")  # noqa: E501

        self._ipv6_network = ipv6_network

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Vlan, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Vlan):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
