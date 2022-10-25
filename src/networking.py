import tweepy
import src.account as account

# Code for wrapping network actions, using Tweepy. Adapted from BotBuddy.

# Generic class for poster. Should be subclassed for each platform.
class Poster:
    creds_keys = []
    
    def platform_name(self):
        return "[generic]"

    def account_id(self):
        return ""
    
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
    api_key_key = "api_key"
    api_key_secret_key = "api_key_secret"
    bearer_token_key = "bearer_token"
    access_token_key = "access_token"
    access_token_secret_key = "access_token_secret"
    api_base_url_key = "api_base_url"

# Poster class for sending messages to Twitter
class Birdie(Poster):

    creds_keys = [
        Keys.api_key_key,
        Keys.api_key_secret_key,
        Keys.access_token_key,
        Keys.access_token_secret_key
    ]
    
    def __init__(self, creds, last_time=None):  

        if self.validate_creds(creds):

            # Create API (for legacy actions)
            auth = tweepy.OAuthHandler(
                creds[Keys.api_key_key], 
                creds[Keys.api_key_secret_key]
            )
            auth.set_access_token(
                creds[Keys.access_token_key],
                creds[Keys.access_token_secret_key]
            )
            self.api = tweepy.API(auth)

            # Create client
            self.client = tweepy.Client(
                consumer_key=creds[Keys.api_key_key],
                consumer_secret=creds[Keys.api_key_secret_key],
                access_token=creds[Keys.access_token_key],
                access_token_secret=creds[Keys.access_token_secret_key]
            )

            self.last_time = last_time

    def validate_creds(self, creds):
        missing = []
        for key in self.creds_keys:
            if not key in creds:
                missing.append(key)

        if missing:
            print("Missing creds keys " + str(missing))

        return True
            
    def platform_name(self):
        return "Twitter"

    def account_id(self):
        return account.id
    
    # Follower actions -----

    def get_followers(self):
        return self.client.get_users_followers(self.account_id(), user_auth=True)

    def get_following(self):
        return self.client.get_users_following(id=self.account_id(), user_auth=True)

    def follow(self, userID):
        return self.client.follow_user(target_user_id=userID)

    def unfollow(self, userID):
        return self.client.unfollow_user(target_user_id=userID)

    # Reading posts -----

    def get_timeline(self):
        return self.client.get_home_timeline(start_time=self.last_time)

    def get_mentions(self):
        return self.client.get_users_mentions(
            id=self.account_id(),
            expansions="author_id",
            start_time=self.last_time,
            user_auth=True
        )

    # Making posts -----

    def respond_to(self, post_id, message):
        return self.client.create_tweet(text=message, in_reply_to_tweet_id=post_id)

    # Managing DMs -----

    # Not implemented
    def read_dms(self):
        return

    # Not implemented
    def send_dm(self, recipient, message):
        return

    # Test -----

    def test(self):
        # print(self.client.get_user(username="stock_photo_dog", user_auth=True))
        print(self.get_mentions())
        # print(self.get_timeline())
