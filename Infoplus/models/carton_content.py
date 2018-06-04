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


class CartonContent(object):
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
        'group_order_id': 'float',
        'order_no': 'float',
        'carton_no': 'int',
        'carton_id': 'int',
        'line_item_id': 'int',
        'location': 'str',
        'quantity': 'int',
        'quantity_scanned': 'int',
        'completed': 'datetime',
        'tote_id': 'str',
        'picker_id': 'str',
        'status': 'str',
        'custom_fields': 'dict(str, object)'
    }

    attribute_map = {
        'id': 'id',
        'group_order_id': 'groupOrderId',
        'order_no': 'orderNo',
        'carton_no': 'cartonNo',
        'carton_id': 'cartonId',
        'line_item_id': 'lineItemId',
        'location': 'location',
        'quantity': 'quantity',
        'quantity_scanned': 'quantityScanned',
        'completed': 'completed',
        'tote_id': 'toteId',
        'picker_id': 'pickerId',
        'status': 'status',
        'custom_fields': 'customFields'
    }

    def __init__(self, id=None, group_order_id=None, order_no=None, carton_no=None, carton_id=None, line_item_id=None, location=None, quantity=None, quantity_scanned=None, completed=None, tote_id=None, picker_id=None, status=None, custom_fields=None):  # noqa: E501
        """CartonContent - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._group_order_id = None
        self._order_no = None
        self._carton_no = None
        self._carton_id = None
        self._line_item_id = None
        self._location = None
        self._quantity = None
        self._quantity_scanned = None
        self._completed = None
        self._tote_id = None
        self._picker_id = None
        self._status = None
        self._custom_fields = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if group_order_id is not None:
            self.group_order_id = group_order_id
        self.order_no = order_no
        if carton_no is not None:
            self.carton_no = carton_no
        self.carton_id = carton_id
        self.line_item_id = line_item_id
        if location is not None:
            self.location = location
        self.quantity = quantity
        if quantity_scanned is not None:
            self.quantity_scanned = quantity_scanned
        if completed is not None:
            self.completed = completed
        if tote_id is not None:
            self.tote_id = tote_id
        if picker_id is not None:
            self.picker_id = picker_id
        if status is not None:
            self.status = status
        if custom_fields is not None:
            self.custom_fields = custom_fields

    @property
    def id(self):
        """Gets the id of this CartonContent.  # noqa: E501


        :return: The id of this CartonContent.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CartonContent.


        :param id: The id of this CartonContent.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def group_order_id(self):
        """Gets the group_order_id of this CartonContent.  # noqa: E501


        :return: The group_order_id of this CartonContent.  # noqa: E501
        :rtype: float
        """
        return self._group_order_id

    @group_order_id.setter
    def group_order_id(self, group_order_id):
        """Sets the group_order_id of this CartonContent.


        :param group_order_id: The group_order_id of this CartonContent.  # noqa: E501
        :type: float
        """

        self._group_order_id = group_order_id

    @property
    def order_no(self):
        """Gets the order_no of this CartonContent.  # noqa: E501


        :return: The order_no of this CartonContent.  # noqa: E501
        :rtype: float
        """
        return self._order_no

    @order_no.setter
    def order_no(self, order_no):
        """Sets the order_no of this CartonContent.


        :param order_no: The order_no of this CartonContent.  # noqa: E501
        :type: float
        """
        if order_no is None:
            raise ValueError("Invalid value for `order_no`, must not be `None`")  # noqa: E501

        self._order_no = order_no

    @property
    def carton_no(self):
        """Gets the carton_no of this CartonContent.  # noqa: E501


        :return: The carton_no of this CartonContent.  # noqa: E501
        :rtype: int
        """
        return self._carton_no

    @carton_no.setter
    def carton_no(self, carton_no):
        """Sets the carton_no of this CartonContent.


        :param carton_no: The carton_no of this CartonContent.  # noqa: E501
        :type: int
        """

        self._carton_no = carton_no

    @property
    def carton_id(self):
        """Gets the carton_id of this CartonContent.  # noqa: E501


        :return: The carton_id of this CartonContent.  # noqa: E501
        :rtype: int
        """
        return self._carton_id

    @carton_id.setter
    def carton_id(self, carton_id):
        """Sets the carton_id of this CartonContent.


        :param carton_id: The carton_id of this CartonContent.  # noqa: E501
        :type: int
        """
        if carton_id is None:
            raise ValueError("Invalid value for `carton_id`, must not be `None`")  # noqa: E501

        self._carton_id = carton_id

    @property
    def line_item_id(self):
        """Gets the line_item_id of this CartonContent.  # noqa: E501


        :return: The line_item_id of this CartonContent.  # noqa: E501
        :rtype: int
        """
        return self._line_item_id

    @line_item_id.setter
    def line_item_id(self, line_item_id):
        """Sets the line_item_id of this CartonContent.


        :param line_item_id: The line_item_id of this CartonContent.  # noqa: E501
        :type: int
        """
        if line_item_id is None:
            raise ValueError("Invalid value for `line_item_id`, must not be `None`")  # noqa: E501

        self._line_item_id = line_item_id

    @property
    def location(self):
        """Gets the location of this CartonContent.  # noqa: E501


        :return: The location of this CartonContent.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this CartonContent.


        :param location: The location of this CartonContent.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def quantity(self):
        """Gets the quantity of this CartonContent.  # noqa: E501


        :return: The quantity of this CartonContent.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this CartonContent.


        :param quantity: The quantity of this CartonContent.  # noqa: E501
        :type: int
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501

        self._quantity = quantity

    @property
    def quantity_scanned(self):
        """Gets the quantity_scanned of this CartonContent.  # noqa: E501


        :return: The quantity_scanned of this CartonContent.  # noqa: E501
        :rtype: int
        """
        return self._quantity_scanned

    @quantity_scanned.setter
    def quantity_scanned(self, quantity_scanned):
        """Sets the quantity_scanned of this CartonContent.


        :param quantity_scanned: The quantity_scanned of this CartonContent.  # noqa: E501
        :type: int
        """

        self._quantity_scanned = quantity_scanned

    @property
    def completed(self):
        """Gets the completed of this CartonContent.  # noqa: E501


        :return: The completed of this CartonContent.  # noqa: E501
        :rtype: datetime
        """
        return self._completed

    @completed.setter
    def completed(self, completed):
        """Sets the completed of this CartonContent.


        :param completed: The completed of this CartonContent.  # noqa: E501
        :type: datetime
        """

        self._completed = completed

    @property
    def tote_id(self):
        """Gets the tote_id of this CartonContent.  # noqa: E501


        :return: The tote_id of this CartonContent.  # noqa: E501
        :rtype: str
        """
        return self._tote_id

    @tote_id.setter
    def tote_id(self, tote_id):
        """Sets the tote_id of this CartonContent.


        :param tote_id: The tote_id of this CartonContent.  # noqa: E501
        :type: str
        """

        self._tote_id = tote_id

    @property
    def picker_id(self):
        """Gets the picker_id of this CartonContent.  # noqa: E501


        :return: The picker_id of this CartonContent.  # noqa: E501
        :rtype: str
        """
        return self._picker_id

    @picker_id.setter
    def picker_id(self, picker_id):
        """Sets the picker_id of this CartonContent.


        :param picker_id: The picker_id of this CartonContent.  # noqa: E501
        :type: str
        """

        self._picker_id = picker_id

    @property
    def status(self):
        """Gets the status of this CartonContent.  # noqa: E501


        :return: The status of this CartonContent.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CartonContent.


        :param status: The status of this CartonContent.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def custom_fields(self):
        """Gets the custom_fields of this CartonContent.  # noqa: E501


        :return: The custom_fields of this CartonContent.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this CartonContent.


        :param custom_fields: The custom_fields of this CartonContent.  # noqa: E501
        :type: dict(str, object)
        """

        self._custom_fields = custom_fields

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
        if not isinstance(other, CartonContent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
