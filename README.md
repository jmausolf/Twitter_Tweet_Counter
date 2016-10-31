# Twitter_Tweet_Counter
Repository builds a pandas database of tweets given a hashtag query or list of hashtags. The results are written to a CSV.

* Code uses dependency of @geduldig TwitterAPI. 
    Download Here: https://github.com/geduldig/TwitterAPI

* Some modifications of @gedulig's original code. 

To run, (1) simply input your Twitter authentication credentials, and (2) modify the list of hashtags to your interest, and (3) save and run `$python Twitter_Counter.py`.

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

## 2. Modify the Hashtags Desired in the Script

## 3. Save and Run in Terminal `$python Twitter_Counter.py`.