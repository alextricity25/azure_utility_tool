"""
Author: Miguel Alex Cantu
Email: miguel.can2@gmail.com
Date: 12/21/2019
Description:
    The main flow of execution for AUT. Azure Utility Tool(AUT), is a
    small command line utility tool and library to perform useful
    functions against Azure Active Directory using the Microsoft
    Graph API
"""
import msal
import os
import logging
import json
import pprint
import importlib
import pdb
from azure_utility_tool import config
from azure_utility_tool.args import get_parser
from azure_utility_tool import apply_filters

# Importing actions
SUPPORTED_ACTIONS = {
        "list_credential_user_registration_details": None,
        "list_directory_audits": None,
        "list_groups_for_user": None,
        "list_all_users": None,
        "list_all_users_mfa": None,
        "get_users_from_enforced_groups": None,
        "get_upn_from_id": None,
        "list_all_applications": None
        }

SUPPORTED_OUTPUTS = {
        "csv": None,
        "stdout": None
}
for action in SUPPORTED_ACTIONS.keys():
    SUPPORTED_ACTIONS[action] = importlib.import_module("actions.{}".format(action), package="azure_utility_tool")

# Importing output modules
for output_module in SUPPORTED_OUTPUTS:
    SUPPORTED_OUTPUTS[output_module] = importlib.import_module("output.{}".format(output_module), package="azure_utility_tool")
# Turn on logging for everything
logging.basicConfig(level=logging.DEBUG)

# Get and build arguments
parsed_args = get_parser().parse_args()

# Get config
config = config.get_config(parsed_args.config)

# Create a long-lived app instance which maintains a token cache.
if not parsed_args.smoke:
    app = msal.ConfidentialClientApplication(
            config["client_id"], authority=config["authority"],
            client_credential={"thumbprint": config["thumbprint"],
            "private_key": open(
                os.path.expanduser(config["private_key_file"])).read()})
else:
    app = None

# Run action
result = getattr(SUPPORTED_ACTIONS[parsed_args.action], parsed_args.action)(parsed_args, config, app)
result = apply_filters.filter_result(result, config)
output = getattr(SUPPORTED_OUTPUTS[parsed_args.output], parsed_args.output)(parsed_args.action, result)
#result = getattr(, parsed_args.action)#(parsed_args, config, app)
#pprint.pprint(result)
#print("FINISHED SUCCESSFULLY!")
#logging.info("FINISHED SUCCESSFULLY!")
