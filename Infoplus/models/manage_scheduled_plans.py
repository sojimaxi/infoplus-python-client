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


class ManageScheduledPlans(object):
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
        'description': 'str',
        'scheduledplantypeid': 'int',
        'planid': 'int',
        'active': 'bool',
        'user': 'int',
        'deleted': 'bool',
        'warehouse_id': 'int',
        'custom_fields': 'dict(str, object)'
    }

    attribute_map = {
        'id': 'id',
        'create_date': 'createDate',
        'modify_date': 'modifyDate',
        'description': 'description',
        'scheduledplantypeid': 'scheduledplantypeid',
        'planid': 'planid',
        'active': 'active',
        'user': 'user',
        'deleted': 'deleted',
        'warehouse_id': 'warehouseId',
        'custom_fields': 'customFields'
    }

    def __init__(self, id=None, create_date=None, modify_date=None, description=None, scheduledplantypeid=None, planid=None, active=False, user=None, deleted=False, warehouse_id=None, custom_fields=None):  # noqa: E501
        """ManageScheduledPlans - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._create_date = None
        self._modify_date = None
        self._description = None
        self._scheduledplantypeid = None
        self._planid = None
        self._active = None
        self._user = None
        self._deleted = None
        self._warehouse_id = None
        self._custom_fields = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if create_date is not None:
            self.create_date = create_date
        if modify_date is not None:
            self.modify_date = modify_date
        if description is not None:
            self.description = description
        if scheduledplantypeid is not None:
            self.scheduledplantypeid = scheduledplantypeid
        if planid is not None:
            self.planid = planid
        if active is not None:
            self.active = active
        if user is not None:
            self.user = user
        if deleted is not None:
            self.deleted = deleted
        self.warehouse_id = warehouse_id
        if custom_fields is not None:
            self.custom_fields = custom_fields

    @property
    def id(self):
        """Gets the id of this ManageScheduledPlans.  # noqa: E501


        :return: The id of this ManageScheduledPlans.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ManageScheduledPlans.


        :param id: The id of this ManageScheduledPlans.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def create_date(self):
        """Gets the create_date of this ManageScheduledPlans.  # noqa: E501


        :return: The create_date of this ManageScheduledPlans.  # noqa: E501
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this ManageScheduledPlans.


        :param create_date: The create_date of this ManageScheduledPlans.  # noqa: E501
        :type: datetime
        """

        self._create_date = create_date

    @property
    def modify_date(self):
        """Gets the modify_date of this ManageScheduledPlans.  # noqa: E501


        :return: The modify_date of this ManageScheduledPlans.  # noqa: E501
        :rtype: datetime
        """
        return self._modify_date

    @modify_date.setter
    def modify_date(self, modify_date):
        """Sets the modify_date of this ManageScheduledPlans.


        :param modify_date: The modify_date of this ManageScheduledPlans.  # noqa: E501
        :type: datetime
        """

        self._modify_date = modify_date

    @property
    def description(self):
        """Gets the description of this ManageScheduledPlans.  # noqa: E501


        :return: The description of this ManageScheduledPlans.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ManageScheduledPlans.


        :param description: The description of this ManageScheduledPlans.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def scheduledplantypeid(self):
        """Gets the scheduledplantypeid of this ManageScheduledPlans.  # noqa: E501


        :return: The scheduledplantypeid of this ManageScheduledPlans.  # noqa: E501
        :rtype: int
        """
        return self._scheduledplantypeid

    @scheduledplantypeid.setter
    def scheduledplantypeid(self, scheduledplantypeid):
        """Sets the scheduledplantypeid of this ManageScheduledPlans.


        :param scheduledplantypeid: The scheduledplantypeid of this ManageScheduledPlans.  # noqa: E501
        :type: int
        """

        self._scheduledplantypeid = scheduledplantypeid

    @property
    def planid(self):
        """Gets the planid of this ManageScheduledPlans.  # noqa: E501


        :return: The planid of this ManageScheduledPlans.  # noqa: E501
        :rtype: int
        """
        return self._planid

    @planid.setter
    def planid(self, planid):
        """Sets the planid of this ManageScheduledPlans.


        :param planid: The planid of this ManageScheduledPlans.  # noqa: E501
        :type: int
        """

        self._planid = planid

    @property
    def active(self):
        """Gets the active of this ManageScheduledPlans.  # noqa: E501


        :return: The active of this ManageScheduledPlans.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this ManageScheduledPlans.


        :param active: The active of this ManageScheduledPlans.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def user(self):
        """Gets the user of this ManageScheduledPlans.  # noqa: E501


        :return: The user of this ManageScheduledPlans.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this ManageScheduledPlans.


        :param user: The user of this ManageScheduledPlans.  # noqa: E501
        :type: int
        """

        self._user = user

    @property
    def deleted(self):
        """Gets the deleted of this ManageScheduledPlans.  # noqa: E501


        :return: The deleted of this ManageScheduledPlans.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this ManageScheduledPlans.


        :param deleted: The deleted of this ManageScheduledPlans.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def warehouse_id(self):
        """Gets the warehouse_id of this ManageScheduledPlans.  # noqa: E501


        :return: The warehouse_id of this ManageScheduledPlans.  # noqa: E501
        :rtype: int
        """
        return self._warehouse_id

    @warehouse_id.setter
    def warehouse_id(self, warehouse_id):
        """Sets the warehouse_id of this ManageScheduledPlans.


        :param warehouse_id: The warehouse_id of this ManageScheduledPlans.  # noqa: E501
        :type: int
        """
        if warehouse_id is None:
            raise ValueError("Invalid value for `warehouse_id`, must not be `None`")  # noqa: E501

        self._warehouse_id = warehouse_id

    @property
    def custom_fields(self):
        """Gets the custom_fields of this ManageScheduledPlans.  # noqa: E501


        :return: The custom_fields of this ManageScheduledPlans.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this ManageScheduledPlans.


        :param custom_fields: The custom_fields of this ManageScheduledPlans.  # noqa: E501
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
        if not isinstance(other, ManageScheduledPlans):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
