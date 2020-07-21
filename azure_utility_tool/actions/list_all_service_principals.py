"""
Author(s):
    Miguel Alex Cantu
Date: 07/21/2020
Description:
    This action will return a dictionary of all the service principles
    in the Azure tenant
"""
from azure_utility_tool.graph_endpoints import LIST_SERVICE_PRINCIPALS
from azure_utility_tool.test_cases import TestCases
from azure_utility_tool.utils import paginate

def list_all_service_principals(parsed_args, config, app):
    """
    This action will return a dictionary of service principals
    indexed by the ID of the record.
    """
    sp_entries = []
    paginate(
            LIST_SERVICE_PRINCIPALS,
            sp_entries,
            'value',
            parsed_args,
            config,
            app,
            test_data=TestCases().get_service_principal_test_data(),
            std_output=False)
    sps = {}
    for entry in sp_entries:
        sps[entry["id"]] = entry
    return sps
