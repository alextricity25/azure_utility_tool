"""
Author(s):
    Miguel Alex Cantu (miguel.can2@gmail.com)
Date: 02/21/2020
Description:
    This action will return a dictionary of all the
    credentialUserRegistrationDetails objects from the tenant indexed by
    userPrincipalName
"""

from azure_utility_tool.test_cases import TestCases
from azure_utility_tool.graph_endpoints import USER_REG_DETAILS
from azure_utility_tool.utils import paginate
from azure_utility_tool.file_logger import file_logger

def list_credential_user_registration_details(
        parsed_args,
        config,
        app):
    """
    This action will return a dictionary of all the
    credentialUserRegistrationDetails objects from the tenant indexed by
    userPrincipalName
    """
    user_reg_data = []
    paginate_result = paginate(
            USER_REG_DETAILS,
            user_reg_data,
            'value',
            parsed_args,
            config,
            app,
            test_data=TestCases().
                get_test_user_reg_info_graph_data(),
            std_output=False)

    # Retry if request failed
    retries = config["MAX_RETRIES"]
    current_retry = 1
    while retries and paginate_result == "FAILED":
        user_reg_data = []
        paginate_result = paginate(
                USER_REG_DETAILS,
                user_reg_data,
                'value',
                parsed_args,
                config,
                app,
                test_data=TestCases().
                    get_test_user_reg_info_graph_data(),
                std_output=False,
                retry_count=current_retry)
        retries -= 1
        current_retry += 1

    user_reg_details = {}
    for user in user_reg_data:
        user_reg_details[user["userPrincipalName"]] = user
    if parsed_args.log:
        file_logger.to_file("list_credential_user_registration_details", user_reg_details)
    return user_reg_details
