"""
Author: Miguel Alex Cantu
Email: miguel.can2@gmail.com
Date: 12/21/2019
Description:
    Some useful functions for AUT are defined here
"""
import logging
import requests
import json
import time
import pdb

def paginate(endpoint, data, key, parsed_args, config, app, transformer=None, test_data=None, std_output=True, payload={}, throttle=0):
    """
    This methods takes and endpoint, and continues to make a get request
    so long as the @odata.nextLink entry is returned.
    Parameters:
        endpoint - The Microsoft endpoint to perform a get request on
        data - The datastructure used to store the returned data
        key - The key to use to retrieve data from the response
        parsed_args - Program arguments passed from the main program
        config - The application configuration
        app - The application object returned from msal
        transformer - A method that is invoked against the data parameter
                      for transformation
        test_data - If test_data is provided, then no API calls are made
                    and the response is assumed to be test_data. This is
                    for smoke tests
        std_output - Boolean. Will print results as they are retrieved. Set
                     to false otherwise.
        payload - Used for POST requests on an endpoint
        throttle - How to long to wait, in seconds, between each API call.
    """
    # Make the first request
    if not parsed_args.smoke:
        # Authenticate. Handles token refreshes as well
        result = app.acquire_token_silent(config["scope"], account=None)
        if not result:
            logging.info(
            "No suitable token exists in cache. Let's get a new one"
            " from AAD")
            result = app.acquire_token_for_client(scopes=config["scope"])

        if "access_token" in result:
            if payload:
                graph_data_response = requests.post(
                        endpoint,
                        headers={
                            "Authorization": "Bearer " + result["access_token"],
                            "Content-Type": "application/json"
                        },
                        data=json.dumps(payload))
                #pdb.set_trace()
            else:
                graph_data_response = requests.get(
                        endpoint,
                        headers={
                            "Authorization": "Bearer " + result["access_token"]
                        })
        graph_data = graph_data_response.json()
    else:
        graph_data = test_data

    # Print users as they are retrieved. Default is to retrieve 100 users
    # at a time.
    # TODO: Implement output drivers for different output options such as:
    # * CSV
    # * JSON
    # * Write to file
    # * Write to stdout
    for entry in graph_data.get(key,''):
        # Transformation would happen here
        # transformer(asdf)
        if transformer:
            entry = transformer(entry)
        if std_output:
            print(json.dumps(entry))

    # Shove the data returned from the endpoint into the data variable
    data.extend(graph_data.get(key, ""))

    # Recursively follow nextLink
    if graph_data.get("@odata.nextLink", ""):
        time.sleep(throttle)
        return paginate(
                graph_data["@odata.nextLink"],
                data,
                key,
                parsed_args,
                config,
                app,
                transformer=transformer,
                test_data=test_data,
                std_output=std_output,
                payload=payload)
    return data
