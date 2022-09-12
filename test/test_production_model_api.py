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
from Infoplus.api.production_model_api import ProductionModelApi  # noqa: E501
from Infoplus.rest import ApiException


class TestProductionModelApi(unittest.TestCase):
    """ProductionModelApi unit test stubs"""

    def setUp(self):
        self.api = Infoplus.api.production_model_api.ProductionModelApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_production_model(self):
        """Test case for add_production_model

        Create a productionModel  # noqa: E501
        """
        pass

    def test_add_production_model_audit(self):
        """Test case for add_production_model_audit

        Add new audit for a productionModel  # noqa: E501
        """
        pass

    def test_add_production_model_file(self):
        """Test case for add_production_model_file

        Attach a file to a productionModel  # noqa: E501
        """
        pass

    def test_add_production_model_file_by_url(self):
        """Test case for add_production_model_file_by_url

        Attach a file to a productionModel by URL.  # noqa: E501
        """
        pass

    def test_add_production_model_tag(self):
        """Test case for add_production_model_tag

        Add new tags for a productionModel.  # noqa: E501
        """
        pass

    def test_delete_production_model(self):
        """Test case for delete_production_model

        Delete a productionModel  # noqa: E501
        """
        pass

    def test_delete_production_model_file(self):
        """Test case for delete_production_model_file

        Delete a file for a productionModel.  # noqa: E501
        """
        pass

    def test_delete_production_model_tag(self):
        """Test case for delete_production_model_tag

        Delete a tag for a productionModel.  # noqa: E501
        """
        pass

    def test_get_duplicate_production_model_by_id(self):
        """Test case for get_duplicate_production_model_by_id

        Get a duplicated a productionModel by id  # noqa: E501
        """
        pass

    def test_get_production_model_by_filter(self):
        """Test case for get_production_model_by_filter

        Search productionModels by filter  # noqa: E501
        """
        pass

    def test_get_production_model_by_id(self):
        """Test case for get_production_model_by_id

        Get a productionModel by id  # noqa: E501
        """
        pass

    def test_get_production_model_files(self):
        """Test case for get_production_model_files

        Get the files for a productionModel.  # noqa: E501
        """
        pass

    def test_get_production_model_tags(self):
        """Test case for get_production_model_tags

        Get the tags for a productionModel.  # noqa: E501
        """
        pass

    def test_update_production_model(self):
        """Test case for update_production_model

        Update a productionModel  # noqa: E501
        """
        pass

    def test_update_production_model_custom_fields(self):
        """Test case for update_production_model_custom_fields

        Update a productionModel custom fields  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
