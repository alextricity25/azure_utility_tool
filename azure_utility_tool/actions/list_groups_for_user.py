"""
Author(s):
    Miguel Alex Cantu (miguel.can2@gmail.com)
Date: 02/21/20
Description:
    This action will return the details of all the groups a 
    specified user is a part of. It will return a dictionary
    indexed by the groups UserPrincipalName
"""
from azure_utility_tool.graph_endpoints import USER_GETMEMBERGROUPS, GROUP_GET
from azure_utility_tool.utils import paginate
import pdb

def list_groups_for_user(parsed_args, config, app):
    """
    This action will return the details of all the groups a 
    specified user is a part of. It will return a dictionary
    indexed by the groups UserPrincipalName
    """
    if not parsed_args.user:
        raise Exception("--user or -u flags must be used with this action!")
    groups = []
    payload = {
            "securityEnabledOnly": "true"
            }
    paginate(
            USER_GETMEMBERGROUPS.format(parsed_args.user),
            groups,
            'value',
            parsed_args,
            config,
            app,
            payload=payload,
            std_output=False) 
    # The above requests only retrieves IDs, we must retrieve their friendly displayName now
    # TODO: Look into using the $select odata query parameter to achieve this
    group_details = {}
    for group_id in groups:
        group_info = []
        paginate(
                GROUP_GET.format(group_id),
                group_info,
                '',
                parsed_args,
                config,
                app,
                std_output=False)
        group_details[group_info[0]['id']] = group_info
    return group_details
