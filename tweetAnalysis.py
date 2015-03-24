#This is a script to analyze the tweets in the LPSC conference
from __future__ import print_function
import tweepy #Installation instructions at https://github.com/tweepy/tweepy 
import pickle
########################################################
#Twitter OAuth credentials
#Get this credentials over at https://apps.twitter.com/
#Instrutions at: https://dev.twitter.com/oauth
#####################################################
consumer_key = 'personal_token'
consumer_secret = 'personal_token'
access_token = 'personal_token'
access_token_secret = 'personal_token'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
public_tweets = []
#This is a hack to get around twitter query limitation of 200 calls per query
#Beware that after 15 minutes you may be over your quota. So you will have to wait
#Because of that I recommend saving everything in a pickle after the first call
last_id = -1
query = '#LPSC2015'
max_tweets = 15000
while len(public_tweets) < max_tweets:
    count = max_tweets - len(public_tweets)
    try:
        new_tweets = api.search(q=query, count=count, max_id=str(last_id - 1), since = "2015-03-15", until = "2015-03-22")
        if not new_tweets:
            break
        public_tweets.extend(new_tweets)
        last_id = new_tweets[-1].id
    except tweepy.TweepError as e:
        # depending on TweepError.code, one may want to retry or wait
        # to keep things simple, we will give up on an error
        break

pickle.dump( public_tweets, open( "tweets_lpsc.p", "wb" ) )#Here we save everything in a file for later use
