"""
Author: Miguel Alex Cantu
Email: miguel.can2@gmail.com
Date: 12/21/2019
Description:
    Arguments for AUT are defined here
"""

import argparse
import inspect
import pprint
from azure_utility_tool import actions

def get_parser():
    parser = argparse.ArgumentParser(
            usage='%(prog)s',
            description=("You can use AUT to perform several useful things"
                         "against an Azure Active Directory tenant")
            )
    parser.add_argument(
            '-s',
            '--smoke',
            action='store_true',
            required=False,
            help="Run a smoke test, without making API calls")
    action_names = inspect.getmembers(actions, inspect.isfunction)
    parser.add_argument(
            'action',
            choices=[action for action, function in action_names
                     if 'list' in action],
            help="The command to run")
    return parser
