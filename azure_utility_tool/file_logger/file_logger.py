"""
Author: Miguel Alex Cantu
Email: miguel.can2@gmail.com
Date: 02/19/2020
Description:
    This module provides functions with logic to write data structures
    cleanly to a specific file. It will be used throughout AUT as the
    primary means of logging. Toggling the debug features will be
    availble by means of a flag.
"""
import datetime
import pprint
import os
import json
import pdb


LOG_BASE_PATH = "/var/log/aut/"
TODAY = datetime.datetime.today()

def to_file(filename, data):
    """
    This function writes `data` to the `filename` specified
    """
    # File path and file name is a combination of
    # what is provided in `filename` and the date.
    filepath = "{}{}_{}-{}-{}".format(
            LOG_BASE_PATH,
            filename,
            TODAY.month,
            TODAY.day,
            TODAY.year)

    # Check to make sure file doesn't already exists. If it does
    # then delete it.
    if os.path.isfile(filepath):
        os.remove(filepath)

    # Create a file and write to it.
    with open(filepath, 'w') as fp:
        if data is not None and isinstance(data, dict):
            fp.write(json.dumps(data, indent=4))
        elif isinstance(data, list) and data is not None:
            for item in data:
                if isinstance(item, dict):
                    fp.write(json.dumps(item) + "\n")

