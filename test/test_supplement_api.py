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
from Infoplus.api.supplement_api import SupplementApi  # noqa: E501
from Infoplus.rest import ApiException


class TestSupplementApi(unittest.TestCase):
    """SupplementApi unit test stubs"""

    def setUp(self):
        self.api = Infoplus.api.supplement_api.SupplementApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_supplement(self):
        """Test case for add_supplement

        Create a supplement  # noqa: E501
        """
        pass

    def test_add_supplement_audit(self):
        """Test case for add_supplement_audit

        Add new audit for a supplement  # noqa: E501
        """
        pass

    def test_add_supplement_file(self):
        """Test case for add_supplement_file

        Attach a file to a supplement  # noqa: E501
        """
        pass

    def test_add_supplement_tag(self):
        """Test case for add_supplement_tag

        Add new tags for a supplement.  # noqa: E501
        """
        pass

    def test_delete_supplement(self):
        """Test case for delete_supplement

        Delete a supplement  # noqa: E501
        """
        pass

    def test_delete_supplement_tag(self):
        """Test case for delete_supplement_tag

        Delete a tag for a supplement.  # noqa: E501
        """
        pass

    def test_get_duplicate_supplement_by_id(self):
        """Test case for get_duplicate_supplement_by_id

        Get a duplicated a supplement by id  # noqa: E501
        """
        pass

    def test_get_supplement_by_filter(self):
        """Test case for get_supplement_by_filter

        Search supplements by filter  # noqa: E501
        """
        pass

    def test_get_supplement_by_id(self):
        """Test case for get_supplement_by_id

        Get a supplement by id  # noqa: E501
        """
        pass

    def test_get_supplement_tags(self):
        """Test case for get_supplement_tags

        Get the tags for a supplement.  # noqa: E501
        """
        pass

    def test_update_supplement(self):
        """Test case for update_supplement

        Update a supplement  # noqa: E501
        """
        pass

    def test_update_supplement_custom_fields(self):
        """Test case for update_supplement_custom_fields

        Update a supplement custom fields  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
