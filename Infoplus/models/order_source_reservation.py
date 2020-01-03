# coding: utf-8

"""
    Infoplus API

    Infoplus API.  # noqa: E501

    OpenAPI spec version: beta
    Contact: api@infopluscommerce.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class OrderSourceReservation(object):
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
        'order_source_id': 'int',
        'create_date': 'datetime',
        'modify_date': 'datetime',
        'reserved_quantity': 'int',
        'custom_fields': 'dict(str, object)',
        'sku': 'str'
    }

    attribute_map = {
        'id': 'id',
        'order_source_id': 'orderSourceId',
        'create_date': 'createDate',
        'modify_date': 'modifyDate',
        'reserved_quantity': 'reservedQuantity',
        'custom_fields': 'customFields',
        'sku': 'sku'
    }

    def __init__(self, id=None, order_source_id=None, create_date=None, modify_date=None, reserved_quantity=None, custom_fields=None, sku=None):  # noqa: E501
        """OrderSourceReservation - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._order_source_id = None
        self._create_date = None
        self._modify_date = None
        self._reserved_quantity = None
        self._custom_fields = None
        self._sku = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.order_source_id = order_source_id
        if create_date is not None:
            self.create_date = create_date
        if modify_date is not None:
            self.modify_date = modify_date
        self.reserved_quantity = reserved_quantity
        if custom_fields is not None:
            self.custom_fields = custom_fields
        if sku is not None:
            self.sku = sku

    @property
    def id(self):
        """Gets the id of this OrderSourceReservation.  # noqa: E501


        :return: The id of this OrderSourceReservation.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OrderSourceReservation.


        :param id: The id of this OrderSourceReservation.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def order_source_id(self):
        """Gets the order_source_id of this OrderSourceReservation.  # noqa: E501


        :return: The order_source_id of this OrderSourceReservation.  # noqa: E501
        :rtype: int
        """
        return self._order_source_id

    @order_source_id.setter
    def order_source_id(self, order_source_id):
        """Sets the order_source_id of this OrderSourceReservation.


        :param order_source_id: The order_source_id of this OrderSourceReservation.  # noqa: E501
        :type: int
        """
        if order_source_id is None:
            raise ValueError("Invalid value for `order_source_id`, must not be `None`")  # noqa: E501

        self._order_source_id = order_source_id

    @property
    def create_date(self):
        """Gets the create_date of this OrderSourceReservation.  # noqa: E501


        :return: The create_date of this OrderSourceReservation.  # noqa: E501
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this OrderSourceReservation.


        :param create_date: The create_date of this OrderSourceReservation.  # noqa: E501
        :type: datetime
        """

        self._create_date = create_date

    @property
    def modify_date(self):
        """Gets the modify_date of this OrderSourceReservation.  # noqa: E501


        :return: The modify_date of this OrderSourceReservation.  # noqa: E501
        :rtype: datetime
        """
        return self._modify_date

    @modify_date.setter
    def modify_date(self, modify_date):
        """Sets the modify_date of this OrderSourceReservation.


        :param modify_date: The modify_date of this OrderSourceReservation.  # noqa: E501
        :type: datetime
        """

        self._modify_date = modify_date

    @property
    def reserved_quantity(self):
        """Gets the reserved_quantity of this OrderSourceReservation.  # noqa: E501


        :return: The reserved_quantity of this OrderSourceReservation.  # noqa: E501
        :rtype: int
        """
        return self._reserved_quantity

    @reserved_quantity.setter
    def reserved_quantity(self, reserved_quantity):
        """Sets the reserved_quantity of this OrderSourceReservation.


        :param reserved_quantity: The reserved_quantity of this OrderSourceReservation.  # noqa: E501
        :type: int
        """
        if reserved_quantity is None:
            raise ValueError("Invalid value for `reserved_quantity`, must not be `None`")  # noqa: E501

        self._reserved_quantity = reserved_quantity

    @property
    def custom_fields(self):
        """Gets the custom_fields of this OrderSourceReservation.  # noqa: E501


        :return: The custom_fields of this OrderSourceReservation.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this OrderSourceReservation.


        :param custom_fields: The custom_fields of this OrderSourceReservation.  # noqa: E501
        :type: dict(str, object)
        """

        self._custom_fields = custom_fields

    @property
    def sku(self):
        """Gets the sku of this OrderSourceReservation.  # noqa: E501


        :return: The sku of this OrderSourceReservation.  # noqa: E501
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """Sets the sku of this OrderSourceReservation.


        :param sku: The sku of this OrderSourceReservation.  # noqa: E501
        :type: str
        """

        self._sku = sku

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OrderSourceReservation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
