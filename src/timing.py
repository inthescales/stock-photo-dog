import os

from datetime import datetime

timestamp_path = 'data/timestamp'

def get_iso_timestamp():
    nowtime = datetime.now()
    nowtime = nowtime.replace(microsecond=0)
    return nowtime.isoformat()

def get_last_date():
    if os.path.exists(timestamp_path):
        with open(timestamp_path, 'r') as file:
            read_timestamp = file.read()
            return read_timestamp

    return None

def record_last_date():
    with open(timestamp_path, 'w') as file:
        timestamp = get_iso_timestamp()
        file.write(str(timestamp))

