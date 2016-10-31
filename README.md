# Twitter Tweet Counter

This code uses the TwitterAPI to return a CSV of tweets and metadata for a given hashtag. One or more hashtags may be specifed at once. 

* Required dependency of [TwitterAPI](https://github.com/geduldig/TwitterAPI)

   If you have pip installed, you can simply `pip install TwitterAPI` in the Shell


To run, (1) simply input your Twitter authentication credentials, and (2) run the query for one or more hashtags.

## 1. Twitter Authentication Credentials

You will first need to setup an "application" from [Twitter](https://apps.twitter.com) to generate your oAuth keys. Once you go through this process, you will end up with four key pieces of information:

* consumer_key
* consumer_secret
* access_token_key
* access_token_secret

Create a "mycredentials.py" file following the format of example_credentials.py:

```
consumer_key = "yoursecretconsumerkey"
consumer_secret = "yoursupersecret_consumer_secret"
access_token_key = "your_access_token_key"
access_token_secret = "your_access_token_secret"
```

## 2. Run the Query for One or More Hashtags

To run the script, open terminal and type a query:

### Example: No Limit (Can Take a Long Time)

```Shell

#One Hashtag
python Twitter_Counter.py '#Obama'

#Two or More Hashtags
python Twitter_Counter.py '#Obama' '#Hilary'
python Twitter_Counter.py '#OccupyWallStreet' '#OWS'

```

For each hashtag, the script will search Twitter using the RestAPI, and return a .csv of the most recent tweets. The CSV will include the following information: DATE, TIME, COUNT, HASHTAG, and TWEET.

** NOTE: The above examples will return all available tweets (going back a week) **
** Some hashtags include hundreds of thousands of tweets, and this will take considerable time **

### Example: Specified Limit (Faster)

```Shell

#One Hashtag
python Twitter_Counter.py '#Obama' --limit 100

#Two or More Hashtags
python Twitter_Counter.py '#Obama' '#Hilary' --limit 100
python Twitter_Counter.py '#OccupyWallStreet' '#OWS' --limit 100

```

