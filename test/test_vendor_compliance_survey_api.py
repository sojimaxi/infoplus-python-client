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
from Infoplus.api.vendor_compliance_survey_api import VendorComplianceSurveyApi  # noqa: E501
from Infoplus.rest import ApiException


class TestVendorComplianceSurveyApi(unittest.TestCase):
    """VendorComplianceSurveyApi unit test stubs"""

    def setUp(self):
        self.api = Infoplus.api.vendor_compliance_survey_api.VendorComplianceSurveyApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_vendor_compliance_survey(self):
        """Test case for add_vendor_compliance_survey

        Create a vendorComplianceSurvey  # noqa: E501
        """
        pass

    def test_add_vendor_compliance_survey_audit(self):
        """Test case for add_vendor_compliance_survey_audit

        Add new audit for a vendorComplianceSurvey  # noqa: E501
        """
        pass

    def test_add_vendor_compliance_survey_file(self):
        """Test case for add_vendor_compliance_survey_file

        Attach a file to a vendorComplianceSurvey  # noqa: E501
        """
        pass

    def test_add_vendor_compliance_survey_tag(self):
        """Test case for add_vendor_compliance_survey_tag

        Add new tags for a vendorComplianceSurvey.  # noqa: E501
        """
        pass

    def test_delete_vendor_compliance_survey(self):
        """Test case for delete_vendor_compliance_survey

        Delete a vendorComplianceSurvey  # noqa: E501
        """
        pass

    def test_delete_vendor_compliance_survey_tag(self):
        """Test case for delete_vendor_compliance_survey_tag

        Delete a tag for a vendorComplianceSurvey.  # noqa: E501
        """
        pass

    def test_get_duplicate_vendor_compliance_survey_by_id(self):
        """Test case for get_duplicate_vendor_compliance_survey_by_id

        Get a duplicated a vendorComplianceSurvey by id  # noqa: E501
        """
        pass

    def test_get_vendor_compliance_survey_by_filter(self):
        """Test case for get_vendor_compliance_survey_by_filter

        Search vendorComplianceSurveys by filter  # noqa: E501
        """
        pass

    def test_get_vendor_compliance_survey_by_id(self):
        """Test case for get_vendor_compliance_survey_by_id

        Get a vendorComplianceSurvey by id  # noqa: E501
        """
        pass

    def test_get_vendor_compliance_survey_tags(self):
        """Test case for get_vendor_compliance_survey_tags

        Get the tags for a vendorComplianceSurvey.  # noqa: E501
        """
        pass

    def test_update_vendor_compliance_survey(self):
        """Test case for update_vendor_compliance_survey

        Update a vendorComplianceSurvey  # noqa: E501
        """
        pass

    def test_update_vendor_compliance_survey_custom_fields(self):
        """Test case for update_vendor_compliance_survey_custom_fields

        Update a vendorComplianceSurvey custom fields  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
