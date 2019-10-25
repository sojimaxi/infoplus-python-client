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
from Infoplus.api.order_source_stock_status_api import OrderSourceStockStatusApi  # noqa: E501
from Infoplus.rest import ApiException


class TestOrderSourceStockStatusApi(unittest.TestCase):
    """OrderSourceStockStatusApi unit test stubs"""

    def setUp(self):
        self.api = Infoplus.api.order_source_stock_status_api.OrderSourceStockStatusApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_order_source_stock_status_audit(self):
        """Test case for add_order_source_stock_status_audit

        Add new audit for an orderSourceStockStatus  # noqa: E501
        """
        pass

    def test_add_order_source_stock_status_file(self):
        """Test case for add_order_source_stock_status_file

        Attach a file to an orderSourceStockStatus  # noqa: E501
        """
        pass

    def test_add_order_source_stock_status_tag(self):
        """Test case for add_order_source_stock_status_tag

        Add new tags for an orderSourceStockStatus.  # noqa: E501
        """
        pass

    def test_delete_order_source_stock_status_tag(self):
        """Test case for delete_order_source_stock_status_tag

        Delete a tag for an orderSourceStockStatus.  # noqa: E501
        """
        pass

    def test_get_duplicate_order_source_stock_status_by_id(self):
        """Test case for get_duplicate_order_source_stock_status_by_id

        Get a duplicated an orderSourceStockStatus by id  # noqa: E501
        """
        pass

    def test_get_order_source_stock_status_by_filter(self):
        """Test case for get_order_source_stock_status_by_filter

        Search orderSourceStockStatuses by filter  # noqa: E501
        """
        pass

    def test_get_order_source_stock_status_by_id(self):
        """Test case for get_order_source_stock_status_by_id

        Get an orderSourceStockStatus by id  # noqa: E501
        """
        pass

    def test_get_order_source_stock_status_tags(self):
        """Test case for get_order_source_stock_status_tags

        Get the tags for an orderSourceStockStatus.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
