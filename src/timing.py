"""Functions for tracking the bot's previous activity.

This is necessary to avoid replying to the same posts multiple times.
"""

import os

from datetime import datetime, timezone, timedelta

timestamp_path = 'data/timestamp'

def get_iso_timestamp():
    """Returns an ISO timestamp of the current time, formatted for Twitter."""
    
    utc_timezone = timezone(timedelta(hours=0))
    nowtime = datetime.now(utc_timezone)
    nowtime = nowtime.replace(microsecond=0)
    return nowtime.isoformat()

def get_last_date(path=timestamp_path):
    """Reads and returns the stored timestamp for the last activity, if any."""

    if os.path.exists(path):
        with open(path, 'r') as file:
            read_timestamp = file.read()
            return read_timestamp

    return None

def record_last_date(path=timestamp_path, timestamp=get_iso_timestamp()):
    """Records the given timestamp to the given path, for later recall."""

    with open(path, 'w') as file:
        file.write(str(timestamp))
