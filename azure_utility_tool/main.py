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
from azure_utility_tool import config
from azure_utility_tool.args import get_parser
from azure_utility_tool import actions

# Turn on logging for everything
logging.basicConfig(level=logging.DEBUG)

# Get config
config = config.get_config()

# Get and build arguments
parsed_args = get_parser().parse_args()

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
getattr(actions, parsed_args.action)(parsed_args, config, app)
