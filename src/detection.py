"""Helpers for detecting whether and how the bot should respond to a given post."""

import re

hotwords = [
    "good dog",
    "good boy",
    "good girl",
    "treat",
    "treats",
    "walk",
    "walks",
    "bone",
    "bones"
]

before_chars = "^|\W|\.|,|!|\?|;|:|-|–|—|\"|'|¿|¡\|"
after_chars = "$|\W|\.|,|!|\?|;|:|-|–|—|\"|'|¿|¡\|"

def hotword_count(text):
    """Returns the number of reaction keywords found in the given text."""

    count = 0
    for word in hotwords:
        # count += len(re.findall("(?i)(^|\W)%s($|\W)" % word, text))
        count += len(re.findall("(?i)(?=(%s)%s(%s))" % (before_chars, word, after_chars), text))

    return count

def mentions_handle(text, handle):
    """Whether the given text contains a reference to the given handle for the purposes of reaction."""

    return re.search("(?i)^@%s($|\W)" % handle, text) != None

def requests_start(text):
    """Whether the text contains a request for the bot to start following."""
    
    return re.search("(?i)(^|\W)start($|\W)", text) != None

def requests_stop(text):
    """Whether the text contains a request for the bot to stop following."""

    return re.search("(?i)(^|\W)stop($|\W)", text) != None
