hotwords = [
    "good dog",
    "good boy",
    "good girl",
    "treat",
    "walk"
]

# Follower updates ==========

def get_followers():
    return []

def get_following():
    return []

def unfollow(users):
    return

def follow(users):
    return

def update_followers():
    followers = get_followers()
    following = get_following()

    to_unfollow = []
    to_follow = []

    unfollow(to_unfollow)
    follow(to_follow)

# Posting ==========

def get_posts():
    return []

def hotword_count(text, hotwords):
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
    update_followers()
    respond_to_posts()
