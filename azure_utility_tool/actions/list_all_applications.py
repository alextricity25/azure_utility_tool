"""
Author(s):
    Miguel Alex Cantu (miguel.can2@gmail.com)
Date: 07/20/2020
Description:
    This action will return a dictionary of all the applications in our tenant
"""
from azure_utility_tool.graph_endpoints import LIST_APPLICATIONS
from azure_utility_tool.test_cases import TestCases
from azure_utility_tool.utils import paginate

def list_all_applications(parsed_args, config, app):
    """
    This action will return a dictionary of applications
    indexed by the ID of the record.
    """
    application_entries = []
    paginate(
            LIST_APPLICATIONS,
            application_entries,
            'value',
            parsed_args,
            config,
            app,
            test_data=TestCases().get_application_test_data(),
            std_output=False)
    applications = {}
    for entry in application_entries:
        applications[entry["appId"]] = entry
    return applications
