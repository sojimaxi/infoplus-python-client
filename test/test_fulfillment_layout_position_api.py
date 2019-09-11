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
from Infoplus.api.fulfillment_layout_position_api import FulfillmentLayoutPositionApi  # noqa: E501
from Infoplus.rest import ApiException


class TestFulfillmentLayoutPositionApi(unittest.TestCase):
    """FulfillmentLayoutPositionApi unit test stubs"""

    def setUp(self):
        self.api = Infoplus.api.fulfillment_layout_position_api.FulfillmentLayoutPositionApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_fulfillment_layout_position_audit(self):
        """Test case for add_fulfillment_layout_position_audit

        Add new audit for a fulfillmentLayoutPosition  # noqa: E501
        """
        pass

    def test_add_fulfillment_layout_position_file(self):
        """Test case for add_fulfillment_layout_position_file

        Attach a file to a fulfillmentLayoutPosition  # noqa: E501
        """
        pass

    def test_add_fulfillment_layout_position_tag(self):
        """Test case for add_fulfillment_layout_position_tag

        Add new tags for a fulfillmentLayoutPosition.  # noqa: E501
        """
        pass

    def test_delete_fulfillment_layout_position_tag(self):
        """Test case for delete_fulfillment_layout_position_tag

        Delete a tag for a fulfillmentLayoutPosition.  # noqa: E501
        """
        pass

    def test_get_duplicate_fulfillment_layout_position_by_id(self):
        """Test case for get_duplicate_fulfillment_layout_position_by_id

        Get a duplicated a fulfillmentLayoutPosition by id  # noqa: E501
        """
        pass

    def test_get_fulfillment_layout_position_by_filter(self):
        """Test case for get_fulfillment_layout_position_by_filter

        Search fulfillmentLayoutPositions by filter  # noqa: E501
        """
        pass

    def test_get_fulfillment_layout_position_by_id(self):
        """Test case for get_fulfillment_layout_position_by_id

        Get a fulfillmentLayoutPosition by id  # noqa: E501
        """
        pass

    def test_get_fulfillment_layout_position_tags(self):
        """Test case for get_fulfillment_layout_position_tags

        Get the tags for a fulfillmentLayoutPosition.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
