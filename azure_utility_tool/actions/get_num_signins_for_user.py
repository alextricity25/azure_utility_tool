"""
Author(s):
    Miguel Alex Cantu (miguel.can2@gmail.com)
Date: 08/03/2020
Description:
    This action will return a dictionary of the number of sign-ins
    (up to 100) for a specified user.
"""

import logging
# TODO: Add testing data for this action
#from azure_utility_tool.test_cases import TestCases
from azure_utility_tool.graph_endpoints import LIST_SIGNINS_FOR_USER
from azure_utility_tool.utils import paginate
from azure_utility_tool.file_logger import file_logger

def get_num_signins_for_user(
        parsed_args,
        config,
        app):
    """
    This action will return a dictionary of the number of sign-ins
    (up to 100) for a specified user.
    """
    # If the UPN is not specified, throw an exception.
    if not parsed_args.user:
        raise Exception("You must specify the user parameter when using"
                " get_num_signins_for_user action")

    # Getting the number of signins for the user, up to 100.
    # To save cycles, this action does not paginate results.
    # This 100 limit is enfourced in graph_endpoints.py
    sign_ins = []
    paginate(
            LIST_SIGNINS_FOR_USER.format(parsed_args.user),
            sign_ins,
            'value',
            parsed_args,
            config,
            app,
            std_output=False,
            skiptoken=False)
    # Build a dictionary with using in the signIn object id
    # as the key.
    num_of_signins = {}
    num_of_signins[parsed_args.user] = {
            'num_of_sign_ins': str(len(sign_ins))
    }
    # Log dataset to logfile if -l flag is given
    if parsed_args.log:
        file_logger.to_file("get_num_signins_for_user", num_of_signins)
    return num_of_signins
