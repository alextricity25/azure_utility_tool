"""
Author(s):
    Miguel Alex Cantu (miguel.can2@gmail.com)
Date: 08/03/2020
Description:
    This action will return a dictionary of all the signins of a specified
    application.
"""

import logging
# TODO: Add testing data for this action
#from azure_utility_tool.test_cases import TestCases
from azure_utility_tool.graph_endpoints import LIST_SIGNINS_FOR_APP
from azure_utility_tool.utils import paginate
from azure_utility_tool.file_logger import file_logger

def get_signins_for_app(
        parsed_args,
        config,
        app,
        application_id=""):
    """
    This action will return a dictionary of all the signins of a specified
    application.
    """
    # Getting the number of signins for the application
    sign_ins = []
    paginate(
            LIST_SIGNINS_FOR_APP.format(application_id),
            sign_ins,
            'value',
            parsed_args,
            config,
            app,
            std_output=False)
    # Build a dictionary with using in the signIn object id
    # as the key.
    sign_ins_details = {}
    for sign_in in sign_ins:
        sign_ins_details[sign_in['id']] = sign_in
    # Log dataset to logfile if -l flag is given
    if parsed_args.log:
        file_logger.to_file("get_signins_for_app", sign_ins_details)
    return sign_ins_details
