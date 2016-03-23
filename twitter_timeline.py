import tweepy
from tweepy import OAuthHandler

# twitter app settings
CONSUMER_KEY = secrets["CONSUMER_KEY"]
CONSUMER_SECRET = secrets["CONSUMER_SECRET"]
OAUTH_TOKEN = secrets["OAUTH_TOKEN"]
OAUTH_TOKEN_SECRET = secrets["OAUTH_TOKEN_SECRET"]

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a tweet
    print(status.text)
