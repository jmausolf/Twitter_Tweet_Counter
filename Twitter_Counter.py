###################################
###                             ###
###      Joshua G. Mausolf      ###
###   Department of Sociology   ###
###    Computation Institute    ###
###    University of Chicago    ###
###                             ###
###################################

import re
import pandas as pd
import numpy as np
from TwitterAPI import TwitterAPI
from TwitterAPI import TwitterRestPager

#NOTE: Must have TwitterAPI Installed

#Insert Your Twitter Credentials Here
consumer_key = " "
consumer_secret = " "
access_token_key = " "
access_token_secret = " "


api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)


def remove_non_ascii_2(text):
	return re.sub(r'[^\x00-\x7F]+', "'", text)


def counter(hashtag, df):
	count = 0

	r = TwitterRestPager(api, 'search/tweets', {'q':hashtag, 'count':100})
	for item in r.get_iterator(wait=6):
		print count
		if 'text' in item:
			count += 1
			n = len(df.index)

			tweet0 = item['text']
			tweet = remove_non_ascii_2(tweet0)
			
			#Clean up date and time
			date0 = item['created_at'].split(' ')
			date = date0[1]+" "+date0[2]+", "+date0[5]
			time = date0[3]

			#Add Row to Data Frame
			df.loc[n] = 0
			df.ix[n, "DATE"] = date
			df.ix[n, "TIME"] = time
			df.ix[n, "COUNT"] = count
			df.ix[n, "HASHTAG"] = hashtag
			df.ix[n, "TWEET"] = tweet


		elif 'message' in item and item['code'] == 88:
			print('SUSPEND, RATE LIMIT EXCEEDED: %s' % item['message'])
			break
	 

#Setup Initial Data Frame
header = ["DATE", "TIME", "COUNT", "HASHTAG", "TWEET"]
index = np.arange(0)
df = pd.DataFrame(columns=header, index = index)


#INPUT YOUR DESIRED HASHTAGS INTO THE ACTIVE LIST BELOW.
	#Some Examples:
	#hashtags = ["#FeeltheBern", "#Bernie2016", "#DebateWithBernie"]
	#hashtags = ["#OWS", "#OccupyWallStreet"]

hashtags = ["#FeeltheBern", "#Bernie2016", "#DebateWithBernie"]
for hashtag in hashtags:
	print "Collecting tweets for hashtag ", hashtag, "..."
	counter(hashtag, df)
print df

#Save the Results
file_name = hashtags[0].replace('#', '')+"_Tweets.csv"
df.to_csv(file_name, encoding='utf-8')


