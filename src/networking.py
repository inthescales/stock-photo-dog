"""Helpers and models for taking network actions"""

import tweepy
import src.account as account

import src.logging as logging

# Code for wrapping network actions, using Tweepy. Adapted from BotBuddy.

class Poster:
    """Generic class for taking social media actions.

    Should be subclassed for each network that the bot will be implemented for.
    """

    creds_keys = [] 
    """Dictionary keys needed for this """
    
    def validate_creds(self):
        """Indicates whether the credentials this object was initialized with are complete."""

        return False

    def platform_name(self):
        """The name of the social platform this object will post to."""

        return "[generic]"

    def account_id(self):
        """The ID of the account that this object will be taking action for."""

        return ""
    
    def get_followers(self):
        """Returns a list of accounts following the bot's account."""

        return []

    def get_following(self):
        """Returns a list of accounts that the bot is following."""

        return []

    def follow(self, user):
        """Follow the given user."""

        return

    def unfollow(self, user):
        """Unfollow the given user."""

        return

    def get_timeline(self):
        """Returns a list of Post objects from the account's timeline."""

        return []

    def get_mentions(self):
        """Returns a list of Mention objects from this account's mention feed."""

        return []

    def respond_to(self, post_id, message, image_path=None):
        """Responds to the given post, with the given mention and image, if any."""

        return

class Keys:
    """Contains the keystrings used in credentials files."""

    api_key_key = "api_key"
    api_key_secret_key = "api_key_secret"
    bearer_token_key = "bearer_token"
    access_token_key = "access_token"
    access_token_secret_key = "access_token_secret"
    api_base_url_key = "api_base_url"

class Birdie(Poster):
    """Performs remote actions on the bot's Twitter account

    Uses Twitter API v2, with OAuth 1
    """

    creds_keys = [
        Keys.api_key_key,
        Keys.api_key_secret_key,
        Keys.access_token_key,
        Keys.access_token_secret_key
    ]
    
    def __init__(self, creds, last_time=None, readonly=False):  
        """Initialize using the given account credentials.

        Ignores posts and mentions from before last_time, if set.
        """

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
            self.readonly = readonly

    def validate_creds(self, creds):
        """Indicates whether the credentials this object was initialized with are complete."""

        missing = []
        for key in self.creds_keys:
            if not key in creds:
                missing.append(key)

        if missing:
            logging.log("Missing creds keys " + str(missing))

        return True
            
    def platform_name(self):
        """The name of the social platform this object will post to."""

        return "Twitter"

    def account_id(self):
        """The ID of the account that this object will be taking action for."""
        return account.id
    
    # Follower actions -----

    def get_followers(self):
        """Returns a list of accounts following the bot's account."""

        return self.client.get_users_followers(self.account_id(), user_auth=True)

    def get_following(self):
        """Returns a list of accounts that the bot is following."""
        return self.client.get_users_following(id=self.account_id(), user_auth=True)

    def follow(self, userID):
        """Follow the given user."""

        if self.readonly:
            return

        return self.client.follow_user(target_user_id=userID)

    def unfollow(self, userID):
        """Unfollow the given user."""
        
        if self.readonly:
            return
        
        return self.client.unfollow_user(target_user_id=userID)

    # Reading posts -----

    def get_timeline(self):
        """Returns a list of Post objects from the account's timeline."""

        timeline = self.client.get_home_timeline(
            exclude="retweets",
            start_time=self.last_time
        )

        if not timeline.data:
            return []

        return [Post(post.id, post.text) for post in timeline.data]

    def get_mentions(self):
        """Returns a list of Mention objects from this account's mention feed."""

        mentions = self.client.get_users_mentions(
            id=self.account_id(),
            expansions="author_id",
            start_time=self.last_time,
            user_auth=True
        )

        if not mentions.data:
            return []

        return [Mention(mention["author_id"], mention["id"], mention["text"]) for mention in mentions.data]

    # Making posts -----

    def respond_to(self, post_id, message, image_path=None):
        """Responds to the given post, with the given mention and image, if any."""

        if self.readonly:
            return
        
        media_ids = None
        if image_path != None:
            media_ids = [self.upload_image(image_path)]

        return self.client.create_tweet(
            text=message,
            media_ids=media_ids,
            in_reply_to_tweet_id=post_id
        )

    def upload_image(self, image_path):
        """Uploads the image at the given path to Twitter, so that it can be attached to tweets."""
        if self.readonly:
            return
        
        image_file = open(image_path, 'rb')
        media = self.api.media_upload(filename=image_path, file=image_file, chunked=False)
        return media.media_id

class Post:
    """Model representing a post in the bot account's timeline."""
    
    def __init__(self, post_id, text):
        self.post_id = post_id
        self.text = text

class Mention:
    """Model representing a post that mentions the bot's account."""

    def __init__(self, author_id, post_id, text):
        self.author_id = author_id
        self.post_id = post_id
        self.text = text