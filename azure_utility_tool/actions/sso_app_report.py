"""
Author(s):
    Miguel Alex Cantu
Date: 07/21/2020
Description:
    This action will generate a report of SSO applications configured
    on the Azure tenant
"""
from azure_utility_tool.graph_endpoints import APP_ROLE_ASSIGNED_TO, LIST_SIGNINS_FOR_APP
from azure_utility_tool.actions.list_all_applications import list_all_applications
from azure_utility_tool.actions.list_all_service_principals import list_all_service_principals
from azure_utility_tool.utils import paginate
from azure_utility_tool.file_logger import file_logger

import ipdb

def sso_app_report(parsed_args, config, app):
    """
    This action will generate a report of SSO applications configured
    on the Azure tenant
    """
    if parsed_args.smoke:
        raise Exception("This action does not support the -s flag")
    all_applications = list_all_applications(parsed_args, config, app)
    all_sps = list_all_service_principals(parsed_args, config, app)

    report_template = {
            "displayName": "",
            "notificationEmailAddresses": None,
            "preferredSingleSignOnMode": None,
            "servicePrincipalType": None,
            "certExp": "",
            "groups": None,
            "numUsersDirectlyAssigned": 0,
            "numSignIns": 0
    }
    applications = {}
    # Now we merge the each user's attribute details with their
    # mfa and SSPR registration information
    for appId, app_details in all_applications.items():
        application = report_template.copy()

        # If the AppID does not have a corresponding appid in the list of
        # service principals, then it's only an app registration, which we
        # do not care for.
        try:
            report_template['displayName'] = all_sps[appId]['displayName']
        except KeyError:
            continue

        users_and_groups = _get_app_role_assignments(all_sps[appId]['id'], parsed_args, config, app)
        report_template['notificationEmailAddresses'] = all_sps[appId]['notificationEmailAddresses']
        report_template['preferredSingleSignOnMode'] = all_sps[appId]['preferredSingleSignOnMode']
        report_template['servicePrincipalType'] = all_sps[appId]['servicePrincipalType']
        report_template['groups'] = users_and_groups['groups']
        report_template['numUsersDirectlyAssigned'] = users_and_groups['numUsers']
        report_template['numSignIns'] = _get_num_signins(appId, parsed_args, config, app)

        try:
            key_creds = all_sps[appId]['keyCredentials'][0]
            report_template['certExp'] = key_creds['endDateTime']
        except IndexError:
            report_template['certExp'] = "NO_CERT_DATA"
            
        applications[appId] = application

    if parsed_args.log:
        file_logger.to_file("sso_app_report", applications)
    return applications

def _get_app_role_assignments(sp_id, parsed_args, config, app):
    assignments = []
    users_and_groups = {
            "groups": [],
            "numUsers": None
            }
    paginate(
            APP_ROLE_ASSIGNED_TO.format(sp_id),
            assignments,
            'value',
            parsed_args,
            config,
            app,
            std_output=False)
    users = []
    for assignment in assignments:
        if assignment['principalType'] == 'Group':
            users_and_groups['groups'].append(assignment['principalDisplayName'])
        elif assignment['principalType'] == 'User':
            users.append(assignment['principalDisplayName'])
    users_and_groups['numUsers'] = len(users)
    return users_and_groups

def _get_num_signins(appId, parsed_args, config, app):
    signIns = []
    count = 0
    paginate(
           LIST_SIGNINS_FOR_APP.format(appId),
           signIns,
           'value',
           parsed_args,
           config,
           app,
           std_output=False)
    return len(signIns)
