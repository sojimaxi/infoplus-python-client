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
from Infoplus.api.packing_plan_detail_api import PackingPlanDetailApi  # noqa: E501
from Infoplus.rest import ApiException


class TestPackingPlanDetailApi(unittest.TestCase):
    """PackingPlanDetailApi unit test stubs"""

    def setUp(self):
        self.api = Infoplus.api.packing_plan_detail_api.PackingPlanDetailApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_packing_plan_detail_audit(self):
        """Test case for add_packing_plan_detail_audit

        Add new audit for a packingPlanDetail  # noqa: E501
        """
        pass

    def test_add_packing_plan_detail_file(self):
        """Test case for add_packing_plan_detail_file

        Attach a file to a packingPlanDetail  # noqa: E501
        """
        pass

    def test_add_packing_plan_detail_file_by_url(self):
        """Test case for add_packing_plan_detail_file_by_url

        Attach a file to a packingPlanDetail by URL.  # noqa: E501
        """
        pass

    def test_add_packing_plan_detail_tag(self):
        """Test case for add_packing_plan_detail_tag

        Add new tags for a packingPlanDetail.  # noqa: E501
        """
        pass

    def test_delete_packing_plan_detail_file(self):
        """Test case for delete_packing_plan_detail_file

        Delete a file for a packingPlanDetail.  # noqa: E501
        """
        pass

    def test_delete_packing_plan_detail_tag(self):
        """Test case for delete_packing_plan_detail_tag

        Delete a tag for a packingPlanDetail.  # noqa: E501
        """
        pass

    def test_get_duplicate_packing_plan_detail_by_id(self):
        """Test case for get_duplicate_packing_plan_detail_by_id

        Get a duplicated a packingPlanDetail by id  # noqa: E501
        """
        pass

    def test_get_packing_plan_detail_by_filter(self):
        """Test case for get_packing_plan_detail_by_filter

        Search packingPlanDetails by filter  # noqa: E501
        """
        pass

    def test_get_packing_plan_detail_by_id(self):
        """Test case for get_packing_plan_detail_by_id

        Get a packingPlanDetail by id  # noqa: E501
        """
        pass

    def test_get_packing_plan_detail_files(self):
        """Test case for get_packing_plan_detail_files

        Get the files for a packingPlanDetail.  # noqa: E501
        """
        pass

    def test_get_packing_plan_detail_tags(self):
        """Test case for get_packing_plan_detail_tags

        Get the tags for a packingPlanDetail.  # noqa: E501
        """
        pass

    def test_update_packing_plan_detail_custom_fields(self):
        """Test case for update_packing_plan_detail_custom_fields

        Update a packingPlanDetail custom fields  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
