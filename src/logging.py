"""Helpers for logging"""

from datetime import datetime

def log(text):
    """Prints the given text, including a timestamp"""
    timestamp = datetime.now()
    print("[%s] %s" % (timestamp, text))
