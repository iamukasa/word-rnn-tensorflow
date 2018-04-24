import tweepy
from tweepy.streaming import StreamListener
from credentials import *

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
B="@kanyewest"
new_tweets = api.user_timeline(screen_name=B,count=8000)
b=" "
for s in new_tweets:

            reader = open("data/kanye/input.txt", "w")
            b= b+ ". "+ s.text
            print (b)
            reader.writelines(str(b))
            reader.close()
