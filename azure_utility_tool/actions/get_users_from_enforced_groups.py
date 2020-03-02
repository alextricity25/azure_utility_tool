"""
Author(s):
    Miguel Alex Cantu
Date: 02/21/20
Description:
    This action will return all the users in the MFA_ENFORCED_GROUPS
"""
from azure_utility_tool.graph_endpoints import GROUP_LIST_TRANSITIVEMEMBERS
from azure_utility_tool.utils import paginate
from azure_utility_tool.test_cases import TestCases

def get_users_from_enforced_groups(parsed_args, config, app):
    """
    This action will return all the users in the MFA_ENFORCED_GROUPS
    """
    users = []
    groups = config["MFA_ENFORCED_GROUPS"].copy()
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
            if "user" in member["@odata.type"]:
                member["mfaEnforcedGroup"] = group
                users.append(member)
            if "group" in member["@odata.type"]:
                groups.append(member["id"])

    users_dict = {}
    for user in users:
        if user["userPrincipalName"] in users_dict.keys():
            users_dict[user["userPrincipalName"]]["mfaEnforcedGroups"].append(user["mfaEnforcedGroup"])
        else:
            users_dict[user["userPrincipalName"]] = user
            users_dict[user["userPrincipalName"]]["mfaEnforcedGroups"] = [user["mfaEnforcedGroup"]]

    return users_dict
