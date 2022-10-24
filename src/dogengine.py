import datetime
import re

import src.account as account
import src.credentialing as credentialing
import src.messages as messages
from src.networking import Birdie

credentials_path = "creds.json"

# Follower updates ==========

def update_followers():
    followers = get_followers()
    following = get_following()

    to_unfollow = []
    to_follow = []

    unfollow(to_unfollow)
    follow(to_follow)

def respond_mentions(birdie):
    mentions = birdie.get_mentions()
    users_handled = []
    for mention in mentions.data:
        text = mention.data["text"]
        author_id = mention.data["author_id"]
        tweet_id = mention.data["id"]
        if author_id not in users_handled:
            respond_mention(birdie, text, author_id, tweet_id)

def respond_mention(birdie, text, user_id, post_id):
    print(text)
    if re.search("(?i)^@%s" % account.handle, text):
        if re.search("(?i)(^|\W)start($|\W)", text):
            print("STARTING")
            birdie.respond_to(post_id, messages.follow)
            birdie.follow(user_id)
        elif re.search("(?i)(^|\W)stop($|\W)", text):
            print("STOPPING")
            birdie.respond_to(post_id, messages.unfollow)
            birdie.unfollow(user_id)
        else:
            print("I'M CONFUSED")
            birdie.respond_to(post_id, messages.unknown)

# Posting ==========

def get_posts():
    return []

def hotword_count(text):
    hotwords = [
        "good dog",
        "good boy",
        "good girl",
        "treat",
        "walk",
        "bone"
    ]

    return 0

def respond(post, level):
    return

def respond_to_posts():
    global hotwords

    posts = get_posts()

    for post in posts:
        hotcount = hotword_count(post, hotwords)
        if counts > 0:
            respond(post, hotcount)

# Control =========

def run():
    global credentials_path
    
    creds = credentialing.read_credentials(credentials_path)
    posters = [Birdie(creds)]

    update_followers()
    respond_to_posts()

# Testing ==========

def test():
    global credentials_path

    creds = credentialing.read_credentials(credentials_path)[0]
    poster = Birdie(creds)
    # poster.test()

    respond_mentions(poster)
