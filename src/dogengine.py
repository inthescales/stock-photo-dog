import datetime

import src.account as account
import src.credentialing as credentialing
import src.detection as detection
import src.logging as logging
import src.reactions as reactions
import src.timing as timing

from src.networking import Birdie

# Constants =============================

credentials_path = "creds.json"

# Respond to mentions ===================

def respond_mentions(birdie):
    mentions = birdie.get_mentions()

    users_handled = []
    for mention in mentions:
        if mention.author_id not in users_handled:
            respond_mention(birdie, mention.text, mention.author_id, mention.post_id)
            users_handled.append(mention.author_id)

def respond_mention(birdie, text, user_id, post_id):
    if detection.mentions_handle(text, account.handle):
        if detection.requests_start(text):
            # birdie.respond_to(post_id, reactions.follow)
            # birdie.follow(user_id)
            print("STARTING")
        elif detection.requests_stop(text):
            # birdie.respond_to(post_id, reactions.unfollow)
            # birdie.unfollow(user_id)
            print("STOPPING")
        else:
            print("IDK")
            # birdie.respond_to(post_id, reactions.unknown)

# Respond to posts ======================

def respond_posts(poster):
    posts = poster.get_timeline()

    for post in posts:
        hotcount = detection.hotword_count(post.text)
        if hotcount > 0:
            print(post.text)
            respond(post.post_id, hotcount)

def respond(post, level):
    level = min(level, reactions.image_max)
    print("=== Posting with level %s" % level)
    return

# Control ===============================

def run():
    global credentials_path
    
    logging.log("Started run")

    start_time = timing.get_last_date()
    logging.log("Read time %s" % start_time)

    creds = credentialing.read_credentials(credentials_path)
    posters = make_posters(creds, start_time)

    for poster in posters:
        respond_mentions(poster)
        respond_posts(poster)

    timing.record_last_date()

    logging.log("Finished run")

def test():
    global credentials_path

    start_time = timing.get_last_date()
    creds = credentialing.read_credentials(credentials_path)[0]
    poster = Birdie(creds, start_time)

    creds = credentialing.read_credentials(credentials_path)
    posters = make_posters(creds, start_time)

    for poster in posters:
        respond_mentions(poster)
        respond_posts(poster)

    timing.record_last_date()

def make_posters(credentials, start_time):
    posters = []
    for cred_set in credentials:
        if cred_set["platform"] == "twitter":
            posters.append(Birdie(cred_set, start_time))

    return posters
