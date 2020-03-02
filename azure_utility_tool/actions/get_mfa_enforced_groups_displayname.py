"""
Author(s):
    Miguel Alex Cantu
Date: 02/21/20
Description:
    This action will return all the users in the MFA_ENFORCED_GROUPS
"""
from azure_utility_tool.graph_endpoints import GROUP_GET
from azure_utility_tool.utils import paginate
from azure_utility_tool.test_cases import TestCases

def get_mfa_enforced_groups_displayname(parsed_args, config, app):
    """
    This method returns a dictionary mapping of the IDs of the
    MFA_ENFORCED_GROUPS defined in the config and their respective
    displayNames
    """
    mfa_enforced_groups_with_display_name = {}
    for group in config["MFA_ENFORCED_GROUPS"].copy():
        group_info = []
        paginate(
                GROUP_GET.format(group),
                group_info,
                'displayName',
                parsed_args,
                config,
                app,
                test_data=TestCases().get_group_test_data(),
                std_output=False)
        mfa_enforced_groups_with_display_name[group] = "".join(group_info)
    return mfa_enforced_groups_with_display_name

