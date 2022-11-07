# twitter_analysis_die_linke_and_afd
**Disclamer**: Work in progress

This project analyses tweets of politicians of the most left, "Die Linke", and most right party, "AfD", of the German bundestag. 

I obtained my data by connecting to Twitter's API and using python's Tweepy library. The file twitter_scraper.py shows the code on how I did it. Note that since I do not have a research account at Twitter I am limit at the amount of tweets I was able to gather.

My work is divided into two notebooks:

1. tweets_over_time_analysis, which includes visualisation of tweets over time
2. linke_afd_analysis

The second notebook inlcudes work on:

1. The hashtags and topics of both parties
2. Word clouds 
3. Left and right wing supervised learning classifier

For the my classification model I used a Naive Bayes model which allows me to predict whether a tweet is about a left win topic (die Linke) or a right win topic (AfD).
