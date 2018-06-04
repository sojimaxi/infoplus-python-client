# coding: utf-8

"""
    Infoplus API

    Infoplus API.  # noqa: E501

    OpenAPI spec version: beta
    Contact: api@infopluscommerce.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import Infoplus
from Infoplus.api.warehouse_api import WarehouseApi  # noqa: E501
from Infoplus.rest import ApiException


class TestWarehouseApi(unittest.TestCase):
    """WarehouseApi unit test stubs"""

    def setUp(self):
        self.api = Infoplus.api.warehouse_api.WarehouseApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_warehouse_audit(self):
        """Test case for add_warehouse_audit

        Add new audit for a warehouse  # noqa: E501
        """
        pass

    def test_add_warehouse_tag(self):
        """Test case for add_warehouse_tag

        Add new tags for a warehouse.  # noqa: E501
        """
        pass

    def test_delete_warehouse_tag(self):
        """Test case for delete_warehouse_tag

        Delete a tag for a warehouse.  # noqa: E501
        """
        pass

    def test_get_duplicate_warehouse_by_id(self):
        """Test case for get_duplicate_warehouse_by_id

        Get a duplicated a warehouse by id  # noqa: E501
        """
        pass

    def test_get_warehouse_by_filter(self):
        """Test case for get_warehouse_by_filter

        Search warehouses by filter  # noqa: E501
        """
        pass

    def test_get_warehouse_by_id(self):
        """Test case for get_warehouse_by_id

        Get a warehouse by id  # noqa: E501
        """
        pass

    def test_get_warehouse_tags(self):
        """Test case for get_warehouse_tags

        Get the tags for a warehouse.  # noqa: E501
        """
        pass

    def test_update_warehouse(self):
        """Test case for update_warehouse

        Update a warehouse  # noqa: E501
        """
        pass

    def test_update_warehouse_custom_fields(self):
        """Test case for update_warehouse_custom_fields

        Update a warehouse custom fields  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
