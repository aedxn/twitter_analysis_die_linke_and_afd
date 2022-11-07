# twitter_analysis_die_linke_and_afd
**Disclamer**: Work in progress

This project analyses tweets of politicians of the most left, "Die Linke", and most right party, "AfD", of the German bundestag and implements a supervised learning algorithm to classify tweets on the political spectrum as either left or right.

I obtained my data by using snscrape, which is a specialised scraper for social media platforms. Unlike the Twitter API snscrape has no scraping limit and can obain all tweets a user has ever sent.

My work is divided into two notebooks:

1. tweets_over_time_analysis, which includes visualisation of tweets over time
2. linke_afd_analysis

The second notebook inlcudes work on:

1. The hashtags and topics of both parties
2. Word clouds 
3. Left and right wing supervised learning classifier

For the my classification model I used a Naive Bayes model which allows me to predict whether a tweet is about a left win topic (die Linke) or a right win topic (AfD).
