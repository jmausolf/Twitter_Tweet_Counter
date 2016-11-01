from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener


#Insert Your Twitter Credentials Here
from mycredentials import *

#Set Authorization
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

class TwitterListener(StreamListener):

    def on_status(self, status):
        try:
            print(str(status.text.encode('utf-8')))

        except Exception as error:
            print(error)

    def on_error(self, status_code):
        print(status_code)


while True:
    try:
        twitterStream = Stream(auth, TwitterListener())
        twitterStream.filter(track=['#Clinton'])

    except Exception as error:
        print(error)