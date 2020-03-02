"""
Author(s):
    Miguel Alex Cantu
Date: 02/21/2020
Description:
    This output module will output the results to a csv file
"""
import sys
import json
import csv as _csv
import datetime
import os


REPORTS_BASE_PATH = "/mfa_reports/csv/"
TODAY = datetime.datetime.today()

def csv(filename, result):
    output_file = "{}{}_{}-{}-{}.csv".format(
            REPORTS_BASE_PATH,
            filename,
            TODAY.month,
            TODAY.day,
            TODAY.year)
    # Check to make sure file doesn't already exists. If it does,
    # then delete it.
    if os.path.isfile(output_file):
        os.remove(output_file)
    output_fp = open(output_file, 'w', encoding='utf-8')
    csv_writer = _csv.writer(output_fp)
    count = 0


    for upn, details in result.items():
        if count == 0:
            header = details.keys()
            csv_writer.writerow(header)
            count += 1
        csv_writer.writerow(details.values())
    output_fp.close()
