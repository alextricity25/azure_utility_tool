"""
Author(s):
    Miguel Alex Cantu (miguel.can2@gmail.com)
Date: 02/21/2020
Description:
    This action will return a dictionary of all the id's read from a file
    along with their UPNs
"""

import logging
from azure_utility_tool.test_cases import TestCases
from azure_utility_tool.graph_endpoints import USER_REG_DETAILS, ONE_USER_GET
from azure_utility_tool.utils import paginate
from azure_utility_tool.file_logger import file_logger

def get_upn_from_id(
        parsed_args,
        config,
        app):
    """
    This action will return a dictionary of all the id's read from a file
    along with their UPNs
    """
    if not parsed_args.input_file:
        logging.error("INPUT FILE REQUIRED FOR THIS ACTION") 
        exit()

    # Opening file for reading
    file1 = open(parsed_args.input_file, 'r')
    users = []
    for line in file1:
        user_data = []
        paginate_result = paginate(
                ONE_USER_GET.format(line.strip()),
                user_data,
                'value',
                parsed_args,
                config,
                app,
                std_output=True)
        users.extend(user_data)
        print(user_data)

    print(user_data)
    user_details = {}
    for user in users:
        user_details[user["userPrincipalName"]] = user
    if parsed_args.log:
        file_logger.to_file("get_upn_from_id", user_details)
    return user_details
