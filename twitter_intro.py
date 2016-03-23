import json
import tweepy
from tweepy import OAuthHandler



CONSUMER_KEY = secrets["CONSUMER_KEY"]
CONSUMER_SECRET = secrets["CONSUMER_SECRET"]
OAUTH_TOKEN = secrets["OAUTH_TOKEN"]
OAUTH_TOKEN_SECRET = secrets["OAUTH_TOKEN_SECRET"]

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

DUB_WOE_ID = 560743
LON_WOE_ID = 44418
CHICAGO_ID = 2379574

# http://docs.tweepy.org/en/latest/api.html?highlight=trends_place#API.trends_place
dub_trends =  api.trends_place(DUB_WOE_ID)
lon_trends = api.trends_place(LON_WOE_ID)
chi_trends = api.trends_place(CHICAGO_ID)

# for trend in json.dumps(dub_trends)[0]['trends']:
#     print(trend)

# print json.dumps(dub_trends, indent=1)
# print json.dumps(lon_trends, indent=1)
# print json.dumps(chi_trends, indent=1)

dub_trends_set = set([trend['name']
                   for trend in dub_trends[0]['trends']])

lon_trends_set = set([trend['name']
                  for trend in lon_trends[0]['trends']])

chi_trends_set = set([trend['name']
                  for trend in chi_trends[0]['trends']])

common_trends = set.intersection(dub_trends_set, chi_trends_set)

print(common_trends)
