"""
Author(s):
    Miguel Alex Cantu (miguel.can2@gmail.com)
Date: 02/21/2020
Description:
    This action will return serveral lines, with each line being a JSON
    representation of the user with it's attributes and MFA registration
    details
"""
from azure_utility_tool.actions.list_credential_user_registration_details import list_credential_user_registration_details
from azure_utility_tool.actions.get_users_from_enforced_groups import get_users_from_enforced_groups
from azure_utility_tool.actions.list_all_users import list_all_users
from azure_utility_tool.file_logger import file_logger

def list_all_users_mfa(parsed_args, config, app):
    """
    This action will return serveral lines, with each line being a JSON
    representation of the user with it's attributes and MFA registration
    details
    """
    users_reg_details = list_credential_user_registration_details(parsed_args, config, app)
    users_attribute_details = list_all_users(parsed_args, config, app)
    enforced_users = get_users_from_enforced_groups(parsed_args, config, app)
    # Now we merge the each user's attribute details with their
    # mfa and SSPR registration information
    for upn, user_details in users_attribute_details.items():
        user_reg_details = users_reg_details.get(upn, {})
        user_details['isCapable'] = user_reg_details.get('isCapable', "No isCapable field for user")
        user_details['isEnabled'] = user_reg_details.get('isEnabled', "No isEnabled field for user")
        user_details['isRegistered'] = user_reg_details.get('isRegistered', "No isRegistered field for user")
        user_details['isMfaRegistered'] = user_reg_details.get('isMfaRegistered', "No isMfaRegistered field for user")
        user_details['authMethods'] = user_reg_details.get('authMethods', "No authMethods field for user")
        user_details["isMfaEnforced"] = "False"
        if user_details["userPrincipalName"] in enforced_users.keys():
            user_details["isMfaEnforced"] = "True"
    if parsed_args.log:
        file_logger.to_file("list_all_users_mfa", users_attribute_details)
    return users_attribute_details
