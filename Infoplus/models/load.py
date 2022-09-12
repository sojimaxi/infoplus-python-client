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


class Load(object):
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
        'create_date': 'datetime',
        'modify_date': 'datetime',
        'lob_id': 'int',
        'lpn': 'str',
        'behavior_type': 'str',
        'warehouse_id': 'int',
        'location_id': 'int',
        'parent_load_id': 'int',
        'pallet_type_id': 'int',
        'carton_type_id': 'int',
        'order_no_list': 'list[float]',
        'custom_fields': 'dict(str, object)'
    }

    attribute_map = {
        'id': 'id',
        'create_date': 'createDate',
        'modify_date': 'modifyDate',
        'lob_id': 'lobId',
        'lpn': 'lpn',
        'behavior_type': 'behaviorType',
        'warehouse_id': 'warehouseId',
        'location_id': 'locationId',
        'parent_load_id': 'parentLoadId',
        'pallet_type_id': 'palletTypeId',
        'carton_type_id': 'cartonTypeId',
        'order_no_list': 'orderNoList',
        'custom_fields': 'customFields'
    }

    def __init__(self, id=None, create_date=None, modify_date=None, lob_id=None, lpn=None, behavior_type=None, warehouse_id=None, location_id=None, parent_load_id=None, pallet_type_id=None, carton_type_id=None, order_no_list=None, custom_fields=None):  # noqa: E501
        """Load - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._create_date = None
        self._modify_date = None
        self._lob_id = None
        self._lpn = None
        self._behavior_type = None
        self._warehouse_id = None
        self._location_id = None
        self._parent_load_id = None
        self._pallet_type_id = None
        self._carton_type_id = None
        self._order_no_list = None
        self._custom_fields = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if create_date is not None:
            self.create_date = create_date
        if modify_date is not None:
            self.modify_date = modify_date
        if lob_id is not None:
            self.lob_id = lob_id
        self.lpn = lpn
        self.behavior_type = behavior_type
        self.warehouse_id = warehouse_id
        if location_id is not None:
            self.location_id = location_id
        if parent_load_id is not None:
            self.parent_load_id = parent_load_id
        if pallet_type_id is not None:
            self.pallet_type_id = pallet_type_id
        if carton_type_id is not None:
            self.carton_type_id = carton_type_id
        if order_no_list is not None:
            self.order_no_list = order_no_list
        if custom_fields is not None:
            self.custom_fields = custom_fields

    @property
    def id(self):
        """Gets the id of this Load.  # noqa: E501


        :return: The id of this Load.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Load.


        :param id: The id of this Load.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def create_date(self):
        """Gets the create_date of this Load.  # noqa: E501


        :return: The create_date of this Load.  # noqa: E501
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this Load.


        :param create_date: The create_date of this Load.  # noqa: E501
        :type: datetime
        """

        self._create_date = create_date

    @property
    def modify_date(self):
        """Gets the modify_date of this Load.  # noqa: E501


        :return: The modify_date of this Load.  # noqa: E501
        :rtype: datetime
        """
        return self._modify_date

    @modify_date.setter
    def modify_date(self, modify_date):
        """Sets the modify_date of this Load.


        :param modify_date: The modify_date of this Load.  # noqa: E501
        :type: datetime
        """

        self._modify_date = modify_date

    @property
    def lob_id(self):
        """Gets the lob_id of this Load.  # noqa: E501


        :return: The lob_id of this Load.  # noqa: E501
        :rtype: int
        """
        return self._lob_id

    @lob_id.setter
    def lob_id(self, lob_id):
        """Sets the lob_id of this Load.


        :param lob_id: The lob_id of this Load.  # noqa: E501
        :type: int
        """

        self._lob_id = lob_id

    @property
    def lpn(self):
        """Gets the lpn of this Load.  # noqa: E501


        :return: The lpn of this Load.  # noqa: E501
        :rtype: str
        """
        return self._lpn

    @lpn.setter
    def lpn(self, lpn):
        """Sets the lpn of this Load.


        :param lpn: The lpn of this Load.  # noqa: E501
        :type: str
        """
        if lpn is None:
            raise ValueError("Invalid value for `lpn`, must not be `None`")  # noqa: E501

        self._lpn = lpn

    @property
    def behavior_type(self):
        """Gets the behavior_type of this Load.  # noqa: E501


        :return: The behavior_type of this Load.  # noqa: E501
        :rtype: str
        """
        return self._behavior_type

    @behavior_type.setter
    def behavior_type(self, behavior_type):
        """Sets the behavior_type of this Load.


        :param behavior_type: The behavior_type of this Load.  # noqa: E501
        :type: str
        """
        if behavior_type is None:
            raise ValueError("Invalid value for `behavior_type`, must not be `None`")  # noqa: E501

        self._behavior_type = behavior_type

    @property
    def warehouse_id(self):
        """Gets the warehouse_id of this Load.  # noqa: E501


        :return: The warehouse_id of this Load.  # noqa: E501
        :rtype: int
        """
        return self._warehouse_id

    @warehouse_id.setter
    def warehouse_id(self, warehouse_id):
        """Sets the warehouse_id of this Load.


        :param warehouse_id: The warehouse_id of this Load.  # noqa: E501
        :type: int
        """
        if warehouse_id is None:
            raise ValueError("Invalid value for `warehouse_id`, must not be `None`")  # noqa: E501

        self._warehouse_id = warehouse_id

    @property
    def location_id(self):
        """Gets the location_id of this Load.  # noqa: E501


        :return: The location_id of this Load.  # noqa: E501
        :rtype: int
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """Sets the location_id of this Load.


        :param location_id: The location_id of this Load.  # noqa: E501
        :type: int
        """

        self._location_id = location_id

    @property
    def parent_load_id(self):
        """Gets the parent_load_id of this Load.  # noqa: E501


        :return: The parent_load_id of this Load.  # noqa: E501
        :rtype: int
        """
        return self._parent_load_id

    @parent_load_id.setter
    def parent_load_id(self, parent_load_id):
        """Sets the parent_load_id of this Load.


        :param parent_load_id: The parent_load_id of this Load.  # noqa: E501
        :type: int
        """

        self._parent_load_id = parent_load_id

    @property
    def pallet_type_id(self):
        """Gets the pallet_type_id of this Load.  # noqa: E501


        :return: The pallet_type_id of this Load.  # noqa: E501
        :rtype: int
        """
        return self._pallet_type_id

    @pallet_type_id.setter
    def pallet_type_id(self, pallet_type_id):
        """Sets the pallet_type_id of this Load.


        :param pallet_type_id: The pallet_type_id of this Load.  # noqa: E501
        :type: int
        """

        self._pallet_type_id = pallet_type_id

    @property
    def carton_type_id(self):
        """Gets the carton_type_id of this Load.  # noqa: E501


        :return: The carton_type_id of this Load.  # noqa: E501
        :rtype: int
        """
        return self._carton_type_id

    @carton_type_id.setter
    def carton_type_id(self, carton_type_id):
        """Sets the carton_type_id of this Load.


        :param carton_type_id: The carton_type_id of this Load.  # noqa: E501
        :type: int
        """

        self._carton_type_id = carton_type_id

    @property
    def order_no_list(self):
        """Gets the order_no_list of this Load.  # noqa: E501


        :return: The order_no_list of this Load.  # noqa: E501
        :rtype: list[float]
        """
        return self._order_no_list

    @order_no_list.setter
    def order_no_list(self, order_no_list):
        """Sets the order_no_list of this Load.


        :param order_no_list: The order_no_list of this Load.  # noqa: E501
        :type: list[float]
        """

        self._order_no_list = order_no_list

    @property
    def custom_fields(self):
        """Gets the custom_fields of this Load.  # noqa: E501


        :return: The custom_fields of this Load.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this Load.


        :param custom_fields: The custom_fields of this Load.  # noqa: E501
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
        if not isinstance(other, Load):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
