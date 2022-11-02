import re

hotwords = [
    "good dog",
    "good boy",
    "good girl",
    "treat",
    "walk",
    "bone"
]

def hotword_count(text):
    count = 0
    for word in hotwords:
        if re.search("(?i)(^|\W)%s($|\W)" % word, text):
            count += 1

    return count

def mentions_handle(text, handle):
    return re.search("(?i)^@%s" % handle, text)

def requests_start(text):
    return re.search("(?i)(^|\W)start($|\W)", text)

def requests_stop(text):
    return re.search("(?i)(^|\W)stop($|\W)", text)
