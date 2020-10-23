"""
Author(s):
    Miguel Alex Cantu
Date: 10/23/2020
Description:
    This output module will output the results as json to a file
"""
import sys
import json as _json
import csv as _csv
import datetime
import os


REPORTS_BASE_PATH = "/mfa_reports/json/"
TODAY = datetime.datetime.today()

def json(filename, result):
    output_file = "{}{}_{}-{}-{}.json".format(
            REPORTS_BASE_PATH,
            filename,
            TODAY.month,
            TODAY.day,
            TODAY.year)
    # Check to make sure file doesn't already exists. If it does,
    # then delete it.
    if os.path.isfile(output_file):
        os.remove(output_file)
    with open(output_file, 'w', encoding='utf-8') as jsonf:
        jsonf.write(_json.dumps(result, indent=4))
