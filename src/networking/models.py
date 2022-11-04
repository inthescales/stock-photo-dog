"""Contains the base models for networking."""

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