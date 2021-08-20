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

from src.entity import AbstractMembership


class Membership(object):
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
        'uuid': 'str',
        'duration': 'int',
        'products': 'list[Object]',
        'first_time': 'bool',
        'payment_method': 'Object',
        'account': 'Object',
        'member': 'Object',
        'status': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }
    if hasattr(AbstractMembership, "swagger_types"):
        swagger_types.update(AbstractMembership.swagger_types)

    attribute_map = {
        'uuid': 'uuid',
        'duration': 'duration',
        'products': 'products',
        'first_time': 'firstTime',
        'payment_method': 'paymentMethod',
        'account': 'account',
        'member': 'member',
        'status': 'status',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt'
    }
    if hasattr(AbstractMembership, "attribute_map"):
        attribute_map.update(AbstractMembership.attribute_map)

    def __init__(self, uuid=None, duration=None, products=None, first_time=None, payment_method=None, account=None, member=None, status=None, created_at=None, updated_at=None, *args, **kwargs):  # noqa: E501
        """Membership - a model defined in Swagger"""  # noqa: E501
        AbstractMembership.__init__(self, *args, **kwargs)
        self._uuid = None
        self._duration = None
        self._products = None
        self._first_time = None
        self._payment_method = None
        self._account = None
        self._member = None
        self._status = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None
        self.uuid = uuid
        if duration is not None:
            self.duration = duration
        if products is not None:
            self.products = products
        if first_time is not None:
            self.first_time = first_time
        if payment_method is not None:
            self.payment_method = payment_method
        if account is not None:
            self.account = account
        self.member = member
        self.status = status
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def uuid(self):
        """Gets the uuid of this Membership.  # noqa: E501

        The UUID associated with this membership request  # noqa: E501

        :return: The uuid of this Membership.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this Membership.

        The UUID associated with this membership request  # noqa: E501

        :param uuid: The uuid of this Membership.  # noqa: E501
        :type: str
        """
        if uuid is None:
            raise ValueError("Invalid value for `uuid`, must not be `None`")  # noqa: E501

        self._uuid = uuid

    @property
    def duration(self):
        """Gets the duration of this Membership.  # noqa: E501

        The requested duration (in days) for this membership  # noqa: E501

        :return: The duration of this Membership.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this Membership.

        The requested duration (in days) for this membership  # noqa: E501

        :param duration: The duration of this Membership.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 30, 60, 90, 120, 150, 180, 360]  # noqa: E501
        if duration not in allowed_values:
            raise ValueError(
                "Invalid value for `duration` ({0}), must be one of {1}"  # noqa: E501
                .format(duration, allowed_values)
            )

        self._duration = duration

    @property
    def products(self):
        """Gets the products of this Membership.  # noqa: E501

        A list of products to buy  # noqa: E501

        :return: The products of this Membership.  # noqa: E501
        :rtype: list[Object]
        """
        return self._products

    @products.setter
    def products(self, products):
        """Sets the products of this Membership.

        A list of products to buy  # noqa: E501

        :param products: The products of this Membership.  # noqa: E501
        :type: list[Object]
        """

        self._products = products

    @property
    def first_time(self):
        """Gets the first_time of this Membership.  # noqa: E501

        Whether this is the first membership request ever for this member  # noqa: E501

        :return: The first_time of this Membership.  # noqa: E501
        :rtype: bool
        """
        return self._first_time

    @first_time.setter
    def first_time(self, first_time):
        """Sets the first_time of this Membership.

        Whether this is the first membership request ever for this member  # noqa: E501

        :param first_time: The first_time of this Membership.  # noqa: E501
        :type: bool
        """

        self._first_time = first_time

    @property
    def payment_method(self):
        """Gets the payment_method of this Membership.  # noqa: E501

        The payment method to be used for the transaction  # noqa: E501

        :return: The payment_method of this Membership.  # noqa: E501
        :rtype: Object
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this Membership.

        The payment method to be used for the transaction  # noqa: E501

        :param payment_method: The payment_method of this Membership.  # noqa: E501
        :type: Object
        """

        self._payment_method = payment_method

    @property
    def account(self):
        """Gets the account of this Membership.  # noqa: E501

        The source account from which to execute the transaction  # noqa: E501

        :return: The account of this Membership.  # noqa: E501
        :rtype: Object
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this Membership.

        The source account from which to execute the transaction  # noqa: E501

        :param account: The account of this Membership.  # noqa: E501
        :type: Object
        """

        self._account = account

    @property
    def member(self):
        """Gets the member of this Membership.  # noqa: E501

        The member to whom this membership applies  # noqa: E501

        :return: The member of this Membership.  # noqa: E501
        :rtype: Object
        """
        return self._member

    @member.setter
    def member(self, member):
        """Sets the member of this Membership.

        The member to whom this membership applies  # noqa: E501

        :param member: The member of this Membership.  # noqa: E501
        :type: Object
        """
        if member is None:
            raise ValueError("Invalid value for `member`, must not be `None`")  # noqa: E501

        self._member = member

    @property
    def status(self):
        """Gets the status of this Membership.  # noqa: E501

        The current status of this membership request:  * `INITIAL` - Just created  * `PENDING_RULES` - Waiting for the member to sign the rules  * `PENDING_PAYMENT_INITIAL` - Initiating the payment flow  * `PENDING_PAYMENT` - During the payment flow  * `PENDING_PAYMENT_VALIDATION` - After the payment flow, waiting for confirmation  * `COMPLETE` - The membership request is completed  * `CANCELLED` - The membership has been cancelled  * `ABORTED` - The membership request flow was aborted Do note that some of the steps may be skipped depending on the payment method, whether or not this is the member's first membership request etc.   # noqa: E501

        :return: The status of this Membership.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Membership.

        The current status of this membership request:  * `INITIAL` - Just created  * `PENDING_RULES` - Waiting for the member to sign the rules  * `PENDING_PAYMENT_INITIAL` - Initiating the payment flow  * `PENDING_PAYMENT` - During the payment flow  * `PENDING_PAYMENT_VALIDATION` - After the payment flow, waiting for confirmation  * `COMPLETE` - The membership request is completed  * `CANCELLED` - The membership has been cancelled  * `ABORTED` - The membership request flow was aborted Do note that some of the steps may be skipped depending on the payment method, whether or not this is the member's first membership request etc.   # noqa: E501

        :param status: The status of this Membership.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501
        allowed_values = ["INITIAL", "PENDING_RULES", "PENDING_PAYMENT_INITIAL", "PENDING_PAYMENT", "PENDING_PAYMENT_VALIDATION", "COMPLETE", "CANCELLED", "ABORTED"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def created_at(self):
        """Gets the created_at of this Membership.  # noqa: E501

        The date-time at which this membership request was first created  # noqa: E501

        :return: The created_at of this Membership.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Membership.

        The date-time at which this membership request was first created  # noqa: E501

        :param created_at: The created_at of this Membership.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Membership.  # noqa: E501

        The date-time at which this membership request was last updated  # noqa: E501

        :return: The updated_at of this Membership.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Membership.

        The date-time at which this membership request was last updated  # noqa: E501

        :param updated_at: The updated_at of this Membership.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

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
        if issubclass(Membership, dict):
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
        if not isinstance(other, Membership):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
