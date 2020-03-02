"""
Author(s):
    Miguel Alex Cantu (miguel.can2@gmail.com)
Date: 02/21/2020
Description:
    This module will include common utility methods for the actions that will
    be implemented in this `action` subpackage of AUT.
"""

import requests
import logging
import datetime

from azure_utility_tool.graph_endpoints import *
from azure_utility_tool.utils import paginate
from azure_utility_tool.test_cases import TestCases
from azure_utility_tool.file_logger import file_logger
from azure_utility_tool.transformers import expand_onPremisesExtensionAttributes

def get_mfa_enforced_groups_displayname(parsed_args, config, app):
    """
    This method returns a dictionary mapping of the IDs of the
    MFA_ENFORCED_GROUPS defined in the config and their respective
    displayNames
    """
    MFA_ENFORCED_GROUPS_WITH_DISPLAY_NAME = {}
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
        MFA_ENFORCED_GROUPS_WITH_DISPLAY_NAME[group] = "".join(group_info)

    return MFA_ENFORCED_GROUPS_WITH_DISPLAY_NAME

def get_users_from_enforced_groups(parsed_args, config, app):
    """
    This method returns a list of dictionary objects representing the users
    in the MFA_ENFORCED_GROUPS.
    """
    users = []
    groups = config['MFA_ENFORCED_GROUPS'].copy()
    while groups:
        members = []
        group = groups.pop()
        paginate(
            GROUP_LIST_TRANSITIVEMEMBERS.format(group),
            members,
            'value',
            parsed_args,
            config,
            app,
            test_data=TestCases().
                get_users_in_enforced_groups_test_data(),
            std_output=False)
        for member in members:
            if 'user' in member["@odata.type"]:
                member['mfaEnforcedGroup'] = group
                users.append(member)
            if 'group' in member["@odata.type"]:
                groups.append(member["id"])
    return users
