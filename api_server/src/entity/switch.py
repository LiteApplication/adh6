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

from src.entity import AbstractSwitch


class Switch(object):
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
        'description': 'str',
        'community': 'str',
        'ip': 'str'
    }
    if hasattr(AbstractSwitch, "swagger_types"):
        swagger_types.update(AbstractSwitch.swagger_types)

    attribute_map = {
        'id': 'id',
        'description': 'description',
        'community': 'community',
        'ip': 'ip'
    }
    if hasattr(AbstractSwitch, "attribute_map"):
        attribute_map.update(AbstractSwitch.attribute_map)

    def __init__(self, id=None, description=None, community=None, ip=None, *args, **kwargs):  # noqa: E501
        """Switch - a model defined in Swagger"""  # noqa: E501
        AbstractSwitch.__init__(self, *args, **kwargs)
        self._id = None
        self._description = None
        self._community = None
        self._ip = None
        self.discriminator = None
        self.id = id
        self.description = description
        self.community = community
        self.ip = ip

    @property
    def id(self):
        """Gets the id of this Switch.  # noqa: E501

        The unique identifier of this switch  # noqa: E501

        :return: The id of this Switch.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Switch.

        The unique identifier of this switch  # noqa: E501

        :param id: The id of this Switch.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def description(self):
        """Gets the description of this Switch.  # noqa: E501

        The friendly name of this switch  # noqa: E501

        :return: The description of this Switch.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Switch.

        The friendly name of this switch  # noqa: E501

        :param description: The description of this Switch.  # noqa: E501
        :type: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def community(self):
        """Gets the community of this Switch.  # noqa: E501

        The community string used for SNMP access to this switch  # noqa: E501

        :return: The community of this Switch.  # noqa: E501
        :rtype: str
        """
        return self._community

    @community.setter
    def community(self, community):
        """Sets the community of this Switch.

        The community string used for SNMP access to this switch  # noqa: E501

        :param community: The community of this Switch.  # noqa: E501
        :type: str
        """
        if community is None:
            raise ValueError("Invalid value for `community`, must not be `None`")  # noqa: E501

        self._community = community

    @property
    def ip(self):
        """Gets the ip of this Switch.  # noqa: E501

        The IPv4 address of this switch  # noqa: E501

        :return: The ip of this Switch.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this Switch.

        The IPv4 address of this switch  # noqa: E501

        :param ip: The ip of this Switch.  # noqa: E501
        :type: str
        """
        if ip is None:
            raise ValueError("Invalid value for `ip`, must not be `None`")  # noqa: E501

        self._ip = ip

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
        if issubclass(Switch, dict):
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
        if not isinstance(other, Switch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
