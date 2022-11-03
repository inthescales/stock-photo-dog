import re

hotwords = [
    "good dog",
    "good boy",
    "good girl",
    "treat",
    "walk",
    "bone"
]

before_chars = "^|\W|\.|,|!|\?|;|:|-|–|—|\"|'|¿|¡\|"
after_chars = "$|\W|\.|,|!|\?|;|:|-|–|—|\"|'|¿|¡\|"

def hotword_count(text):
    count = 0
    for word in hotwords:
        # count += len(re.findall("(?i)(^|\W)%s($|\W)" % word, text))
        count += len(re.findall("(?i)(?=(%s)%s(%s))" % (before_chars, word, after_chars), text))

    return count

def mentions_handle(text, handle):
    return re.search("(?i)^@%s" % handle, text)

def requests_start(text):
    return re.search("(?i)(^|\W)start($|\W)", text)

def requests_stop(text):
    return re.search("(?i)(^|\W)stop($|\W)", text)
