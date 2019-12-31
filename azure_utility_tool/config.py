"""
Author: Miguel Alex Cantu
Email: miguel.can2@gmail.com
Date: 12/21/2019
Description:
    Loads Azure Utility Tool configuration file. The configuration
    file is a blend of what the Microsoft Authentication Library
    requires and some extra directives that the Auzre Utility
    Tool requires. It is a JSON file that is required to be
    stored in ~/.aut/aut_config.json
"""

import json
import sys
import os

from azure_utility_tool.exceptions import ConfigFileNotFound

def get_config():
    CONFIG_PATH = os.path.expanduser("~/.aut/aut_config.json")
    # Ensure the directory exists, if not, then throw an Exception.
    if not os.path.exists(CONFIG_PATH):
        raise ConfigFileNotFound("The configuration file for the Azure"
                                 " Utility Tool was not found in"
                                 " ~/.aut/aut_config.json")
    return json.load(open(CONFIG_PATH))
