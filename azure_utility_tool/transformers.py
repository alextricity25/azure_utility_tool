"""
Author: Miguel Alex Cantu
Email: miguel.can2@gmail.com
Date: 12/28/2019
Description:
    The transformers defined here are passed to the paginate function
    defined in the utils.py module. They transform the data that is
    returned by the MS Graph API according to the logic defined here
"""

def make_upn_index(entry):
    """
    entry - a dictionary that must have the 'userPrincipalName' defined
    
    This transofrmer takes a dictionary, and returns another dictionary
    that can be indexed using 'userPrincipalName'
    """
    for key, value in entry.items():
        if key == "userPrincipalName":
            return { value: entry }
    raise Exception("Cannot find userPrincipalName")
