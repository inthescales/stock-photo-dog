"""Helpers related to reading account credentials from a file"""

import json

import src.logging as logging

# Reads credentials from a JSON file.
def read_credentials(filename):
    """Reads credentials from the JSON file at the given path, and returns them as a dictionary.

    If no credentials are found at the given path, logs an error.
    """
    
    try:
        with open(filename) as json_data:
            creds = json.load(json_data)
            return creds
    except IOError:
        logging.log("Credentials file '" + filename + "' not found")
        return None

    logging.log("Valid creds file not found")
    return None
