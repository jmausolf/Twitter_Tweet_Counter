###################################
###                             ###
###      Joshua G. Mausolf      ###
###   Department of Sociology   ###
###    Computation Institute    ###
###    University of Chicago    ###
###                             ###
###################################

import csv, os, re
import argparse, textwrap
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener


#Insert Your Twitter Credentials Here
from mycredentials import *

#Set Authorization
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

#Utility Functions
def remove_non_ascii_2(text):
    return re.sub(r'[^\x00-\x7F]+', "'", text)

def start_csv():
    with open('streaming_results.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["DATE", "AUTHOR", "TWEET"])


#Tweepy Streaming Listener
class TwitterListener(StreamListener):

    def on_status(self, status):
        try:
            with open('streaming_results.csv', 'a') as f:
                writer = csv.writer(f)

                #Tweet Content
                author = str(status.author.screen_name.encode('utf-8'))
                date = str(status.created_at)
                tweet_raw = str(status.text.encode('utf-8'))
                tweet = remove_non_ascii_2(tweet_raw)
                
                print("{} Tweet: {} ...".format(date, tweet[0:50]))
                writer.writerow([date, author, tweet])

        except Exception as error:
            print(error)

    def on_error(self, status_code):
        print(status_code)


#Wrapper Function
def streaming_tweets(keywords, language=["en"]):
    """
    @keywords   ==  search keywords, e.g. ["ImWithHer", "Trump"]
    @languages  ==  desired language, e.g.: ["en"]

    """

    filename = keywords[0].replace(" ", "").replace("#", "")+".csv"
    print(filename)

    try:
        start_csv()
        while True:
            try:
                #Initialize Tweepy Streamer
                twitterStream = Stream(auth, TwitterListener())
                twitterStream.filter(track=keywords, languages=language)
            except Exception as error:
                print(error)
                print ("[*] saving results to {}".format(filename))
                os.rename("streaming_results.csv", filename)

    except KeyboardInterrupt:
        print ("[*] User KeyboardInterrupt: Tweepy Streamer Haulted")
        print ("[*] saving results to {}".format(filename))
        os.rename("streaming_results.csv", filename)


#INSERT YOUR DESIRED SEARCH TERMS
#streaming_tweets(["#ImWithHer", "#Trump"])

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Prepare input file',
            formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('keywords', nargs='+', type=str, 
        help=textwrap.dedent("""\
            Input one or more keywords to search

            "#ImWithHer"

            or

            "#ImWithHer" "#Hillary"

            The final command takes the following format:

            python Streaming_Tweets.py "#ImWithHer" "#Hillary"

            """
            ))

    args = parser.parse_args()
    streaming_tweets(args.keywords)


