import os

from datetime import datetime, timezone, timedelta

timestamp_path = 'data/timestamp'

def get_iso_timestamp():
    utc_timezone = timezone(timedelta(hours=0))
    nowtime = datetime.now(utc_timezone)
    nowtime = nowtime.replace(microsecond=0)
    return nowtime.isoformat()

def get_last_date(path=timestamp_path):
    if os.path.exists(path):
        with open(path, 'r') as file:
            read_timestamp = file.read()
            return read_timestamp

    return None

def record_last_date(path=timestamp_path, timestamp=get_iso_timestamp()):
    with open(path, 'w') as file:
        file.write(str(timestamp))
