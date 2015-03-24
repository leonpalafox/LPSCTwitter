#This library loads the tweets that were saved with the hashtag LPSC
#To run this, you need to have run tweetAnalysis.py first
import sys
import pickle
from pytz import timezone
import datetime, time
import pylab as plt
import string
from nltk.corpus import stopwords
import nltk #Instructions to install nltk
public_tweets = pickle.load( open( "tweets_lpsc.p", "rb" ) ) #Here we load the file that we saved in tweetAnalysis.py
dates = []
stop = stopwords.words('english') + list(string.punctuation)+['rt', 'http', 'co', 'data'] #Here we define the most common stopwords in english
#Stopwords are common frequently used words (and, the, at,...)
#We usually take them out, other way trending words would be boring
for tweet in public_tweets:
    dates.append(tweet.created_at)

ages = []
#Twitter calls come on GMT, so we need to translate it into USA/Cental time.
basetime = 'Etc/Greenwich'
LPSCTime = 'US/Central'
lpsc_tweets = []
#First we need to loalize everything to Houston time, from GT
for idx, d in enumerate(dates):
    d = timezone(basetime).localize(d) #Assign GMT time to tweets
    d = d.astimezone(timezone(LPSCTime)) #Trasform to Central Time
    if d.day >=16 and d.day<=20:
        ages.append(d) # age in seconds, prune only the LPSC week
        lpsc_tweets.append(public_tweets[idx])
data_ = []
#Now we use a dictionary, so each element is a different LPSC day
hist_dict ={}
for age in ages:
    if age.day not in hist_dict:
        hist_dict[age.day] = []
    hist_dict[age.day].append(age.hour + age.minute/60.0)


#Now we do the plots
figure =plt.figure()
#because it is a single for, we need to assign a list of labels
labels_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
#and a list of colors
color_list = ['r', 'g', 'b','c', 'y' ]
#We invert the list, just because I liked it more that way
color_list = color_list[::-1]
axes = figure.add_subplot(1, 1, 1, axisbg='0.8')
axes.grid(color = 'w', linestyle='-', linewidth = 1)
axes.set_axisbelow(True) #This makes all the histograms share the same bins
for idx, keys in enumerate(hist_dict):
    axes.hist(hist_dict[keys], bins = 40, color='r', facecolor = color_list[idx], edgecolor = '0', linewidth = 1, alpha = 0.5, range = (0,24), label = labels_list[idx])
    #This command does the histogram with 40 bins, which were the ones that looked the best for LPSC
axes.set_ylabel('#LPSC2015 Twits', weight = 'bold') #Set X Labels
axes.set_xlabel('Time of the day (24 hr format)', weight = 'bold') #Set Y Labels
axes.legend()


#Generate Figures with the trending words
plt.figure()
data_ = []
for idx, tweet in enumerate(lpsc_tweets):
    data_.append(tweet.text)
final_text = ' '.join(data_)

tokens = nltk.wordpunct_tokenize(final_text) #Tokenize (take out punctuation) each twit
text = nltk.Text(tokens) #Get text out of tokens
text = [w.lower() for w in text if w.isalpha() ] #Check that no weird characters are in the twit
text = [w for w in text if w not in stop] #Check for stopwords
text = [w for w in text if len(w) >= 2 ] #Look only for words longer than 2 characters
fd = nltk.FreqDist(text)  #Get the frequency distribution
fd.plot(20,cumulative=False) #Plot the distribution
#There is some hand tunning to do with the lower part of the plot, which I usually do in the GUI for pyplot