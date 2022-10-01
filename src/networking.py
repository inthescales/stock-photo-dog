import tweepy

# Generic class for poster. Should be subclassed for each platform.
class Poster:
    creds_keys = []
    
    def platform_name(self):
        return "[generic]"
    
    def get_followers(self):
        return []

    def get_following(self):
        return []

    def follow(self, user):
        return

    def unfollow(self, user):
        return

    def get_posts(self):
        return []

    def respond_to(self, post):
        return

# Contains keys used in credentials files.
class Keys:
    consumer_key_key = "consumer_key"
    consumer_secret_key = "consumer_secret"
    access_token_key = "access_token"
    access_token_secret_key = "access_token_secret"
    api_base_url_key = "api_base_url"

# Poster class for sending messages to Twitter
class Birdie(Poster):

    creds_keys = [Keys.consumer_key_key,
                  Keys.consumer_secret_key,
                  Keys.access_token_key,
                  Keys.access_token_secret_key]
    
    def __init__(self, creds):    
        if self.validate_creds(creds):
            auth = tweepy.OAuthHandler(creds[Keys.consumer_key_key], 
                                       creds[Keys.consumer_secret_key])
            auth.set_access_token(creds[Keys.access_token_key],
                                  creds[Keys.access_token_secret_key])
            self.api = tweepy.API(auth)
            
    def platform_name(self):
        return "Twitter"
            
    def get_followers(self):
        return []

    def get_following(self):
        return []

    def follow(self, user):
        return

    def unfollow(self, user):
        return

    def get_posts(self):
        return []

    def respond_to(self, post):
        return
