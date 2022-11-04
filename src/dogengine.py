import datetime

import src.account as account
import src.detection as detection
import src.logging as logging
import src.networking.networking as networking
import src.reactions as reactions
import src.timing as timing

from src.networking.networking import Birdie

# Constants =============================

credentials_path = "creds.json"

# Respond to mentions ===================

def respond_mentions(birdie):
    mentions = birdie.get_mentions()

    users_handled = []

    response_count = 0
    for mention in mentions:
        if mention.author_id not in users_handled:
            respond_mention(birdie, mention.text, mention.author_id, mention.post_id)
            users_handled.append(mention.author_id)
            response_count += 1

    logging.log("Read %d mentions, responded to %d" % (len(mentions), response_count))

def respond_mention(birdie, text, user_id, post_id):
    if detection.mentions_handle(text, account.handle) and detection.hotword_count(text) == 0:
        if detection.requests_start(text):
            birdie.respond_to(post_id, reactions.follow)
            birdie.follow(user_id)
        elif detection.requests_stop(text):
            birdie.respond_to(post_id, reactions.unfollow)
            birdie.unfollow(user_id)
        else:
            birdie.respond_to(post_id, reactions.unknown)

# Respond to posts ======================

def respond_posts(poster):
    posts = poster.get_timeline()

    response_count = 0
    for post in posts:
        hotcount = detection.hotword_count(post.text)
        if hotcount > 0:
            respond(poster, post.post_id, hotcount)
            response_count += 1

    logging.log("Read %d posts, responded to %d" % (len(posts), response_count))

def respond(poster, post_id, level):
    level_index = min(level, reactions.image_max) - 1
    path = reactions.image_path_for_level[level_index]
    poster.respond_to(post_id, message=None, image_path=path)

# Control ===============================

def run(testmode=False):
    """Runs a cycle of the bot's activity.

    In each cycle, the actions taken are:
        1. Fetch mentions, follow or unfollow users per their requests.
        2. Fetch timeline, respond to appropriate posts.
        3. Store the current time.
    """
    global credentials_path
    
    logging.log("Started run (testmode=%s)" % str(testmode))

    start_time = timing.get_last_date()
    logging.log("Read time %s" % start_time)

    posters = networking.make_posters(credentials_path, start_time, readonly=testmode)

    for poster in posters:
        respond_mentions(poster)
        respond_posts(poster)

    if not testmode:
        timing.record_last_date()

    logging.log("Finished run")
