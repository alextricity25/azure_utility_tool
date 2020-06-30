"""
Author(s):
    Miguel Alex Cantu
Date: 02/21/2020
Description:
    This output module will output the results to a csv file
"""
import json
def stdout(filename, result):
    print(json.dumps(result, indent=4))
