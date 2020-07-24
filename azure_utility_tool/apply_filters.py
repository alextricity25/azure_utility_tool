"""
Author(s):
    Miguel Alex Cantu
Date: 06/30/2020
Description:
    This module contains methods relevant to filtering the result returned
    by the action modules
"""

def filter_result(result, config):
    """
    Applies all filters
    """
    filters = config['filters']
    for key, value in filters.items():
        globals()[key](result, value)
    return result
        

def remove_columns(result, filter_data):
    if not isinstance(filter_data, list):
        raise Exception("Must pass a list as filter_data when using remove_columns()!")
    for userPrincipalName, data in result.items():
        for column in filter_data:
            data.pop(column, "No column found")


def filter_out(result, filter_data):
    result_copy = result.copy()
    if not isinstance(filter_data, dict):
        raise Exception("Must pass a dictionary as filter_data when using filter_out")
    for userPrincipalName, data in result_copy.items():
        for attribute, values in filter_data.items():
            if data.get(attribute, '') in values:
                result.pop(userPrincipalName, "Not found")


