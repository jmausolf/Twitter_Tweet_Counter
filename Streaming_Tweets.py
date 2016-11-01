import csv
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener


#Insert Your Twitter Credentials Here
from mycredentials import *

#Set Authorization
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

class TwitterListener(StreamListener):

    def start_csv():
        with open('Clinton.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow(["DATE", "AUTHOR", "TWEET"])


    def on_status(self, status):
        try:
            with open('Clinton.csv', 'a') as f:
                writer = csv.writer(f)
                
                #Tweet Content
                author = str(status.author.screen_name.encode('utf-8'))
                date = str(status.created_at)
                tweet = str(status.text.encode('utf-8'))
                
                print(date, tweet)
                writer.writerow([date, author, tweet])

        except Exception as error:
            print(error)

    def on_error(self, status_code):
        print(status_code)


#So Still streams
twitterStream = Stream(auth, TwitterListener())
twitterStream.filter(track=['#Clinton'])


#while True:
#    try:
#        twitterStream = Stream(auth, TwitterListener())
#        twitterStream.filter(track=['#Clinton'])
#    except Exception as error:
#        print(error)