"""
Author(s):
    Miguel Alex Cantu (miguel.can2@gmail.com)
Date: 02/21/2020
Description:
    This action will return several lines, with each line being a JSON
    representation of the user
"""
from azure_utility_tool.utils import paginate
from azure_utility_tool.graph_endpoints import USER_GET_ENDPOINT
from azure_utility_tool.test_cases import TestCases
from azure_utility_tool.transformers import expand_onPremisesExtensionAttributes

def list_all_users(parsed_args, config, app):
    """
    This action returns a dictionary of all the users indexed by
    userPrincipalName
    """
    user_data = []
    paginate(
            USER_GET_ENDPOINT,
            user_data,
            'value',
            parsed_args,
            config,
            app,
            test_data=TestCases().get_test_user_graph_data(),
            std_output=False,
            transformer=expand_onPremisesExtensionAttributes)

    # Return a dictionary of all the users in the tenant, indexed by
    # userPrincipalName
    users = {}
    for user in user_data:
        users[user["userPrincipalName"]] = user

    return users
