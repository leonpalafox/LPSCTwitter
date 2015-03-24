# LPSCTwitter
This small code generates plots that describe the twitter activity at LPSC 2015, held in Houtson, TX in March 2015

#Description

During the last LPSC, the hastag #LPSC2015 was used by the microbloggers to describe everything that was happening during the event.

I found this interesting and decided to do some simple plots that described the activity day by day.

At the end, I posted pictures on Twitter on the overall activity as well as the most trending topics.

#Recommendations

In the file ```tweetAnalysis.py``` you need to add the fields ```consumer_key```, ```consumer_secret```, ```access_token``` and ```access_token_secret```.

You can find those in https://apps.twitter.com/ by generating your own app, I usually just do a dummy app to generate the fields. These access codes are personalized, so that is the reason I'm not putting them in my code.


#Requirements

Both tweepy and nltk are required to do the plots. Also matplotlib to do the plots

##Tweepy

Tweepy is a python implementation of the Twitter API, is just a handy way to write queries without actually doing it by hand on Python.

Tweepy Installation: https://github.com/tweepy/tweepy

##NLTK

NLTK is an uber powerful NLP library that is probably being underutilized here, you will have to download the stopword corpus before running this using the instruction nltk.download()

NLTK Installation: http://www.nltk.org/install.html

##Matplotlib

The best library by far to do plots in Python, an incredibly convenient to do more advanced stuff.

Matplotlib installation: http://matplotlib.org/users/installing.html


#How to Use

This is a really ad-hoc version to generate plots like the one here: https://twitter.com/leonpalafox/status/580170949925814272

First run the file ```tweetAnalysis.py```, you'll need User tokens from twitter, which can be obtained here:  https://apps.twitter.com/. 

The call is really personalized for the LPSC week, if you wish to look other dates, you'll have to modify the ```since``` and ```until``` fileds in the query.

If you wish to look for other hastags, just change ```query = #LPSC2015``` to whatever you want.

After running it, you'll get a file called ```tweets_lpsc.p``` which has all the twits that you called (about 80 MB), I recommend running this once every 15 minutes, since twitter gets picky if you make too many calls.

Then, you can run ```analyse_lpsc_tweets.py``` which generates the plots, everything is really hard coded for the LPSC week, like the day flag, which checks for particular days of the month.

Let me know if you have any questions

