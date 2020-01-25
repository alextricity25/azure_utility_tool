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
import pdb
from azure_utility_tool import actions
from argparse import RawTextHelpFormatter

def get_parser():
    parser = argparse.ArgumentParser(
            usage='%(prog)s',
            formatter_class=RawTextHelpFormatter,
            description=("You can use AUT to perform several useful things"
                         "against an Azure Active Directory tenant")
            )
    parser.add_argument(
            '-s',
            '--smoke',
            action='store_true',
            required=False,
            help="Run a smoke test, without making API calls")
    parser.add_argument(
            '-u',
            '--user',
            required=False,
            help="The userPrincipalName of a user")
    action_names = inspect.getmembers(actions, inspect.isfunction)
    parser.add_argument(
            'action',
            choices=[action for action, function in action_names
                     if 'list' in action],
            help=_build_action_help_string())
    return parser

def _build_action_help_string():
    help_string = ""
    action_names = inspect.getmembers(actions, inspect.isfunction)
    #pdb.set_trace()
    for action, function in action_names:
        if 'list' in action:
            help_string = help_string + "{} - {}\n".format(
                        action,
                        function.__doc__.replace('\n', '').strip().
                            replace('    ', ' '))
    return help_string
