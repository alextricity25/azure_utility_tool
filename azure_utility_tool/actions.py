"""
Author: Miguel Alex Cantu
Email: miguel.can2@gmail.com
Date: 12/25/2019
Description:
    These are all available actions that the Azure Utility Tool can
    perform. They are called by the user via arguments. For example,
    to output all users:
    > aut list_all_users
    To get all users with attributes and mfa registration details:
    > aut list_all_users_mfa
    To get all users and check whether they are in a group:
    > aut list_all_users --in-groups [<GROUPID>, <GROUPID>]
"""

import requests
import logging
import msal
import json
import datetime

from azure_utility_tool.graph_endpoints import *
from azure_utility_tool.utils import paginate
from azure_utility_tool.test_cases import TestCases

def list_all_users(parsed_args, config, app):
    """
    This action will return several lines, with each line being a JSON
    representation of the user
    """
    # A list of dictionaries
    user_data = []
    paginate(
            USER_GET_ENDPOINT,
            user_data,
            'value',
            parsed_args,
            config,
            app,
            test_data=TestCases().get_test_user_graph_data())

def list_all_users_mfa(parsed_args, config, app):
    """
    This action will return the MFA/SSPR registration details of all
    users, as well as their attributes.
    """
    user_reg_data = []
    paginate(
            USER_REG_DETAILS_ENDPOINT,
            user_reg_data,
            'value',
            parsed_args,
            config,
            app,
            test_data=TestCases().
                        get_test_user_reg_info_graph_data(),
            std_output=False)
    # Convert the user_reg_data to a dictionary indexable by user's UPN
    users_reg_info = {}
    for user in user_reg_data:
        users_reg_info[user["userPrincipalName"]] = user

    # Get user attributes
    users_attr_info = []
    paginate(
            USER_GET_ENDPOINT,
            users_attr_info,
            'value',
            parsed_args,
            config,
            app,
            test_data=TestCases().
                    get_test_user_graph_data(),
            std_output=False)
    # Merge the reg info with the user attr info
    # Get users in MFA_ENFORCED_GROUPS
    mfa_enforced_users = _get_users_from_enforced_groups(
                                            parsed_args,
                                            config,
                                            app)
    for user in users_attr_info:
        user_mfa_reg_info = users_reg_info.get(user["userPrincipalName"], '')
        user.update(user_mfa_reg_info)
        # Check to see if user is enforced
        for enforced_user in mfa_enforced_users:
            if enforced_user["userPrincipalName"] == user["userPrincipalName"]:
                user["mfaEnforced"] = "True"
            else:
                user["mfaEnforced"] = "False"
    # Output the users
    # TODO: Make output drivers
    for user in users_attr_info:
        print(json.dumps(user))

def list_directory_audits(parsed_args, config, app):
    """
    This action will return all audit logs in the tenant for the
    past day.
    """
    audit_entries = []
    date = datetime.datetime.today()
    yesterday = date - datetime.timedelta(days=1)
    paginate(
            LIST_DIRECTORY_AUDITS.format(yesterday.year,
                                         yesterday.month,
                                         yesterday.day),
            audit_entries,
            'value',
            parsed_args,
            config,
            app)

def list_groups_for_user(parsed_args, config, app):
    """
    This action will return a list of groups for a specified user
    """
    groups = []
    payload = {"securityEnabledOnly": "true"}
    paginate(
            GET_MEMBER_GROUPS.format(parsed_args.user),
            groups,
            'value',
            parsed_args,
            config,
            app,
            payload=payload,
            std_output=False)

    group_names = []
    for group_id in groups:
        group_info = []
        paginate(
                GET_GROUP.format(group_id),
                group_info,
                'displayName',
                parsed_args,
                config,
                app,
                std_output=False)
        group_names.append("".join(group_info))

    for group in group_names:
        print(group)

# Helper functions
def _get_users_from_enforced_groups(parsed_args, config, app):
    users = []
    groups = config['MFA_ENFORCED_GROUPS']
    while groups:
        members = []
        group = groups.pop()
        paginate(
                LIST_TRANSITIVE_MEMBERS_ENDPOINT.format(group),
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
                users.append(member)
            if 'group' in member["@odata.type"]:
                groups.append(member["id"])
    return users
