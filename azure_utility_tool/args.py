"""
Author: Miguel Alex Cantu
Email: miguel.can2@gmail.com
Date: 12/21/2019
Description:
    Arguments for AUT are defined here
"""

import argparse
import importlib
import pprint
import pdb
from argparse import RawTextHelpFormatter

SUPPORTED_ACTIONS = {
        "list_credential_user_registration_details": None,
        "list_directory_audits": None,
        "list_groups_for_user": None,
        "list_all_users": None,
        "list_all_users_mfa": None,
        "get_users_from_enforced_groups": None,
        "get_upn_from_id": None,
        }

# Importing supported actions
for action in SUPPORTED_ACTIONS.keys():
    SUPPORTED_ACTIONS[action] = importlib.import_module("actions.{}".format(action), package="azure_utility_tool")
    
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
    parser.add_argument(
            '-l',
            '--log',
            required=False,
            action='store_true',
            help="Log the contents of internal data structures in /var/log/aut/")
    parser.add_argument(
            'action',
            choices=SUPPORTED_ACTIONS.keys(),
            help=_build_action_help_string())
    parser.add_argument(
            '-o',
            '--output',
            required=True,
            help="The output module to use")
    parser.add_argument(
            '-i',
            '--input-file',
            required=False,
            help="The input file. Currently only supports one column of data")
    return parser

def _build_action_help_string():
    help_string = ""
    for action, module in SUPPORTED_ACTIONS.items():
        help_string = help_string + "{} - {}\n".format(
                    action,
                    getattr(module, action).__doc__.replace('\n', '').strip().
                        replace('    ', ' '))
    return help_string
