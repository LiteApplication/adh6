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


class AbstractDevice(object):
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
        'connection_type': 'str',
        'ipv4_address': 'str',
        'ipv6_address': 'str',
        'mac': 'str',
        'member': 'OneOfAbstractDeviceMember'
    }

    attribute_map = {
        'id': 'id',
        'connection_type': 'connectionType',
        'ipv4_address': 'ipv4Address',
        'ipv6_address': 'ipv6Address',
        'mac': 'mac',
        'member': 'member'
    }

    def __init__(self, id=None, connection_type=None, ipv4_address=None, ipv6_address=None, mac=None, member=None):  # noqa: E501
        """AbstractDevice - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._connection_type = None
        self._ipv4_address = None
        self._ipv6_address = None
        self._mac = None
        self._member = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if connection_type is not None:
            self.connection_type = connection_type
        if ipv4_address is not None:
            self.ipv4_address = ipv4_address
        if ipv6_address is not None:
            self.ipv6_address = ipv6_address
        if mac is not None:
            self.mac = mac
        if member is not None:
            self.member = member

    @property
    def id(self):
        """Gets the id of this AbstractDevice.  # noqa: E501

        The unique identifier of this device  # noqa: E501

        :return: The id of this AbstractDevice.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AbstractDevice.

        The unique identifier of this device  # noqa: E501

        :param id: The id of this AbstractDevice.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def connection_type(self):
        """Gets the connection_type of this AbstractDevice.  # noqa: E501

        The connection type of this device  # noqa: E501

        :return: The connection_type of this AbstractDevice.  # noqa: E501
        :rtype: str
        """
        return self._connection_type

    @connection_type.setter
    def connection_type(self, connection_type):
        """Sets the connection_type of this AbstractDevice.

        The connection type of this device  # noqa: E501

        :param connection_type: The connection_type of this AbstractDevice.  # noqa: E501
        :type: str
        """
        allowed_values = ["wired", "wireless"]  # noqa: E501
        if connection_type not in allowed_values:
            raise ValueError(
                "Invalid value for `connection_type` ({0}), must be one of {1}"  # noqa: E501
                .format(connection_type, allowed_values)
            )

        self._connection_type = connection_type

    @property
    def ipv4_address(self):
        """Gets the ipv4_address of this AbstractDevice.  # noqa: E501

        The ipv4 address assigned to this device  # noqa: E501

        :return: The ipv4_address of this AbstractDevice.  # noqa: E501
        :rtype: str
        """
        return self._ipv4_address

    @ipv4_address.setter
    def ipv4_address(self, ipv4_address):
        """Sets the ipv4_address of this AbstractDevice.

        The ipv4 address assigned to this device  # noqa: E501

        :param ipv4_address: The ipv4_address of this AbstractDevice.  # noqa: E501
        :type: str
        """

        self._ipv4_address = ipv4_address

    @property
    def ipv6_address(self):
        """Gets the ipv6_address of this AbstractDevice.  # noqa: E501

        The ipv6 address assigned to this device  # noqa: E501

        :return: The ipv6_address of this AbstractDevice.  # noqa: E501
        :rtype: str
        """
        return self._ipv6_address

    @ipv6_address.setter
    def ipv6_address(self, ipv6_address):
        """Sets the ipv6_address of this AbstractDevice.

        The ipv6 address assigned to this device  # noqa: E501

        :param ipv6_address: The ipv6_address of this AbstractDevice.  # noqa: E501
        :type: str
        """

        self._ipv6_address = ipv6_address

    @property
    def mac(self):
        """Gets the mac of this AbstractDevice.  # noqa: E501

        The MAC address of this device  # noqa: E501

        :return: The mac of this AbstractDevice.  # noqa: E501
        :rtype: str
        """
        return self._mac

    @mac.setter
    def mac(self, mac):
        """Sets the mac of this AbstractDevice.

        The MAC address of this device  # noqa: E501

        :param mac: The mac of this AbstractDevice.  # noqa: E501
        :type: str
        """

        self._mac = mac

    @property
    def member(self):
        """Gets the member of this AbstractDevice.  # noqa: E501

        The member this device belongs to  # noqa: E501

        :return: The member of this AbstractDevice.  # noqa: E501
        :rtype: OneOfAbstractDeviceMember
        """
        return self._member

    @member.setter
    def member(self, member):
        """Sets the member of this AbstractDevice.

        The member this device belongs to  # noqa: E501

        :param member: The member of this AbstractDevice.  # noqa: E501
        :type: OneOfAbstractDeviceMember
        """

        self._member = member

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
        if issubclass(AbstractDevice, dict):
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
        if not isinstance(other, AbstractDevice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
