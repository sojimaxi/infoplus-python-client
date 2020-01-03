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
from Infoplus.api.item_account_code_api import ItemAccountCodeApi  # noqa: E501
from Infoplus.rest import ApiException


class TestItemAccountCodeApi(unittest.TestCase):
    """ItemAccountCodeApi unit test stubs"""

    def setUp(self):
        self.api = Infoplus.api.item_account_code_api.ItemAccountCodeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_item_account_code(self):
        """Test case for add_item_account_code

        Create an itemAccountCode  # noqa: E501
        """
        pass

    def test_add_item_account_code_audit(self):
        """Test case for add_item_account_code_audit

        Add new audit for an itemAccountCode  # noqa: E501
        """
        pass

    def test_add_item_account_code_file(self):
        """Test case for add_item_account_code_file

        Attach a file to an itemAccountCode  # noqa: E501
        """
        pass

    def test_add_item_account_code_tag(self):
        """Test case for add_item_account_code_tag

        Add new tags for an itemAccountCode.  # noqa: E501
        """
        pass

    def test_delete_item_account_code(self):
        """Test case for delete_item_account_code

        Delete an itemAccountCode  # noqa: E501
        """
        pass

    def test_delete_item_account_code_tag(self):
        """Test case for delete_item_account_code_tag

        Delete a tag for an itemAccountCode.  # noqa: E501
        """
        pass

    def test_get_duplicate_item_account_code_by_id(self):
        """Test case for get_duplicate_item_account_code_by_id

        Get a duplicated an itemAccountCode by id  # noqa: E501
        """
        pass

    def test_get_item_account_code_by_filter(self):
        """Test case for get_item_account_code_by_filter

        Search itemAccountCodes by filter  # noqa: E501
        """
        pass

    def test_get_item_account_code_by_id(self):
        """Test case for get_item_account_code_by_id

        Get an itemAccountCode by id  # noqa: E501
        """
        pass

    def test_get_item_account_code_tags(self):
        """Test case for get_item_account_code_tags

        Get the tags for an itemAccountCode.  # noqa: E501
        """
        pass

    def test_update_item_account_code(self):
        """Test case for update_item_account_code

        Update an itemAccountCode  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
