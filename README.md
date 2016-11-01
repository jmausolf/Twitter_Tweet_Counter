# Twitter Tweet Counter

This code uses Twitter's REST and STREAMING API's to return a CSV of tweets for given criteria.

### Required Dependencies:

* [TwitterAPI](https://github.com/geduldig/TwitterAPI) : `pip install TwitterAPI` in the Shell
* [Tweepy](http://tweepy.readthedocs.io/en/v3.5.0/): `pip install tweepy` in Shell

---

# Running the Code

* ####1. Clone the repository `git clone https://github.com/jmausolf/Twitter_Tweet_Counter`

* ####2. Input Your Twitter Authentication

* ####3. Run Either (A) REST API or (B) STREAMING API

---

## 1. Clone the Repo

**Using the Shell: `git clone https://github.com/jmausolf/Twitter_Tweet_Counter`**

---

## 2. Twitter Authentication Credentials

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

---

## 3A. REST API: Run the Query for One or More Hashtags

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

**NOTE: The above examples will return all available tweets (going back a week)**

**Some hashtags include hundreds of thousands of tweets, and this will take considerable time**

### Example: Specified Limit (Faster)

```Shell

#One Hashtag
python Twitter_Counter.py '#Obama' --limit 100

#Two or More Hashtags
python Twitter_Counter.py '#Obama' '#Hilary' --limit 100
python Twitter_Counter.py '#OccupyWallStreet' '#OWS' --limit 100

```

## 3B. STREAMING API: Run the Query for Particular Search Terms

This script will initialize Twitter's STREAMING API using [Tweepy](http://tweepy.readthedocs.io/en/v3.5.0/).

### Example: Streaming for Hillary Tweets

```
#One Keyword
python Streaming_Tweets.py "Hillary"

#Two or More Keywords
python Streaming_Tweets.py "#ImWithHer" "#Hillary"
```

Once executed, this script will run until the users haults the script. To exit the script use your keyboard to interupt using `Control`+`C`.

---
