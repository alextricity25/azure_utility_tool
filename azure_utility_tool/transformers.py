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

def expand_onPremisesExtensionAttributes(entry):
    """
    entry - a dictionary that must have the "onPremisesExtensionAttributes" key defined

    This transformer takes a dictionary, and returns the same dictionary, but with the
    "onPremisesExtensionAttributes" value expanded into it's own key: value pair.
    This value must initially be a JSON.
    """
    for key, value in entry.get("onPremisesExtensionAttributes", {}).items():
        entry[key] = value
    entry.pop("onPremisesExtensionAttributes", None)
    return entry
