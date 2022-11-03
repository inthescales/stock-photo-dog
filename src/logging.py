from datetime import datetime

def log(text):
    timestamp = datetime.now()
    print("[%s] text" % timestamp)
