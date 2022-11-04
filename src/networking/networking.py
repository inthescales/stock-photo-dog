"""Helpers and models for taking network actions"""

import src.logging as logging
import src.networking.credentialing as credentialing

from src.networking.twitter import Birdie

def make_posters(credentials_path, start_time, readonly=False):
    """Creates and returns Poster objects for all credentials stored at the given path.

    Parameters
    ----------
    credentials_path : str
        Relative filepath for the JSON file storing account credentials.

    start_time: datetime
        A starting time before which posts and mentions will be ignored.

    readonly: bool
        If true, no mutating network actions will be taken.
    """

    credentials = credentialing.read_credentials(credentials_path)

    posters = []
    for cred_set in credentials:
        if cred_set["platform"] == "twitter":
            logging.log("Connecting to Twitter")
            posters.append(Birdie(cred_set, start_time, readonly))

    return posters
