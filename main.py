import tweepy
import configparser
import pandas as pd

# read config
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_tokens = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# authentification
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_tokens, access_token_secret)

api = tweepy.API(auth)

# creating empty list to store out tweets in
data = []
columns = ['Time', 'User', 'Tweet', 'Favorites', 'Retweets']

# creating a list of all the users we want to scrape
user = ['AndreasKalbitz', 'M_HarderKuehnel', 'AfDProtschka', 'StBrander', 'P_Plattform', 'BjoernHoecke', 'Alice_Weidel',
        'Tino_Chrupalla', 'Beatrix_vStorch', 'Frohnmaier_AfD', 'Janine_Wissler', 'katjakipping', 'SWagenknecht',
        'GregorGysi', 'DietmarBartsch', 'Amira_M_Ali', 'schirdewan', 'bodoramelow', 'lgbeutin', 'SusanneHennig',
        'PetraPauMaHe']

# make sure to set the limit high enough
limit = 2800000

# looping through the user list
for i in range(len(user)):
    tweets = tweepy.Cursor(api.user_timeline, screen_name=user[i], count=limit, tweet_mode='extended').items(limit)

    for tweet in tweets:
        data.append([tweet.created_at, tweet.user.screen_name, tweet.full_text, tweet.favorite_count,
                     tweet.retweet_count])

df = pd.DataFrame(data, columns=columns)

df.to_csv(r'afd_linke_tweets.csv')
