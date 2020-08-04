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
from azure_utility_tool.actions.get_signins_for_app import get_signins_for_app
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
            "numTotalSignIns": 0,
            "numDistinctUserSignIns": 0
    }
    applications = {}
    for appId, app_details in all_applications.items():
        application = report_template.copy()

        # If the AppID does not have a corresponding appid in the list of
        # service principals, then it's only an app registration, which we
        # do not care for.
        try:
            application['displayName'] = all_sps[appId]['displayName']
        except KeyError:
            continue

        users_and_groups = _get_app_role_assignments(all_sps[appId]['id'], parsed_args, config, app)
        application['notificationEmailAddresses'] = all_sps[appId]['notificationEmailAddresses']
        application['preferredSingleSignOnMode'] = all_sps[appId]['preferredSingleSignOnMode']
        application['servicePrincipalType'] = all_sps[appId]['servicePrincipalType']
        application['groups'] = users_and_groups['groups']
        application['numUsersDirectlyAssigned'] = users_and_groups['numUsers']
        application['numTotalSignIns'] = _get_num_distinct_signins(appId, parsed_args, config, app)[0]
        application['numDistinctUserSignIns'] = _get_num_distinct_signins(appId, parsed_args, config, app)[1]

        try:
            key_creds = all_sps[appId]['keyCredentials'][0]
            application['certExp'] = key_creds['endDateTime']
        except IndexError:
            application['certExp'] = "NO_CERT_DATA"
            
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

def _get_num_distinct_signins(appId, parsed_args, config, app):
    signIns = get_signins_for_app(parsed_args, config, app, appId)
    # Building set with the user's ID as entries. This will tell us the
    # number of distinct users that signed into the application in the past
    # month.
    distinct_signins = set()
    for signin_id, signin_data in signIns.items():
        distinct_signins.add(signin_data['userId'])

    return (len(signIns.keys()), len(distinct_signins))
