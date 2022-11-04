"""Helpers related to reading account credentials from a file"""

import json

import src.logging as logging

class Keys:
    """Contains the keystrings used in credentials files."""

    api_key_key = "api_key"
    api_key_secret_key = "api_key_secret"
    bearer_token_key = "bearer_token"
    access_token_key = "access_token"
    access_token_secret_key = "access_token_secret"
    api_base_url_key = "api_base_url"

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
