###################################
###                             ###
###      Joshua G. Mausolf      ###
###   Department of Sociology   ###
###    Computation Institute    ###
###    University of Chicago    ###
###                             ###
###################################

import re, textwrap
import pandas as pd
import numpy as np
import argparse

#NOTE: Must have TwitterAPI Installed
from TwitterAPI import TwitterAPI
from TwitterAPI import TwitterRestPager

#Insert Your Twitter Credentials Here
from mycredentials import *


#API User Authorization
api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)


def remove_non_ascii_2(text):
	return re.sub(r'[^\x00-\x7F]+', "'", text)

def extract_tweet_info(item, count, df, hashtag):
	"""
	Utility to Prevent Code Duplication in Counter
	"""

	n = len(df.index)
	tweet_raw = item['text']
	tweet = remove_non_ascii_2(tweet_raw)

	#Clean up date and time
	date_raw = item['created_at'].split(' ')
	date = date_raw[1]+" "+date_raw[2]+", "+date_raw[5]
	time = date_raw[3]

	#Add Row to Data Frame
	df.loc[n] = 0
	df.ix[n, "DATE"] = date
	df.ix[n, "TIME"] = time
	df.ix[n, "COUNT"] = count
	df.ix[n, "HASHTAG"] = hashtag
	df.ix[n, "TWEET"] = tweet

def counter(hashtag, df, limit=None):
	count = 0

	#Initialize Twitter Rest Pager
	r = TwitterRestPager(api, 'search/tweets', {'q':hashtag, 'count':100})

	#Limit Option
	if limit is not None:
		print("requested tweets for hashtag is limited to {} tweets".format(limit))

		for item in r.get_iterator(wait=6):

			if 'text' in item:
				if count <= limit:
					
					print("collecting tweet {} of {}...".format(count, limit))
					count += 1
					
					#Extract Tweet Info
					extract_tweet_info(item, count, df, hashtag)

				else:
					print("requested tweet limit reached...")
					print("ending query for hashtag...")
					return

			elif 'message' in item and item['code'] == 88:
				print('SUSPEND, RATE LIMIT EXCEEDED: %s' % item['message'])
				break
			

	#No Limit
	else:

		for item in r.get_iterator(wait=6):
			
			if 'text' in item:

				print("collecting tweet {} of all available tweets...".format(count))
				count += 1

				#Extract Tweet Info
				extract_tweet_info(item, count, df, hashtag)

			elif 'message' in item and item['code'] == 88:
				print('SUSPEND, RATE LIMIT EXCEEDED: %s' % item['message'])
				break
	 


def collect_tweets_for_hashtags(hashtags, limit):

	for hashtag in hashtags:

		print ("Collecting tweets for {} ...".format(hashtag))

		#Setup Initial Data Frame
		header = ["DATE", "TIME", "COUNT", "HASHTAG", "TWEET"]
		index = np.arange(0)
		df = pd.DataFrame(columns=header, index = index)

		#Count Tweets
		counter(hashtag, df, limit)

		#Save the Results
		file_name = hashtag.replace('#', '')+"_Tweets.csv"
		print("saving results for {} to {}...".format(hashtag, file_name))
		df.to_csv(file_name, encoding='utf-8')




#INPUT YOUR DESIRED HASHTAGS INTO THE ACTIVE LIST BELOW.
#Or Run from the Command Line
#hashtags = ["#Obama", "#Hilary"]
#collect_tweets_for_hashtags(hashtags)

if __name__=="__main__":
	parser = argparse.ArgumentParser(description='Prepare input file',
	        formatter_class=argparse.RawTextHelpFormatter)
	parser.add_argument('hashtags', nargs='+', type=str, 
		help=textwrap.dedent("""\
			Input a single hashtag or multiple hashtags, e.g.

			'#Hilary' 

			or

			'#Hilary' '#Obama'

			The final command takes the following format:

			python Twitter_Counter.py '#Hilary' '#Obama' '#Biden'

			"""
			))
	parser.add_argument('-l', '--limit', default=None, type=int, help="max desired number of results per hashtag, default=None")

	args = parser.parse_args()
	collect_tweets_for_hashtags(args.hashtags, args.limit)

