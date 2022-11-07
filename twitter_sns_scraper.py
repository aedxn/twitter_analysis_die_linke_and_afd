import pandas as pd
import snscrape.modules.twitter as sntwitter

# politicians to scrape
query = '(from:lgbeutin, OR from:SusanneHennig, OR from:PetraPauMaHe, OR from:DietmarBartsch, OR from:Amira_M_Ali, ' \
        'OR from:schirdewan, OR from:bodoramelow, OR from:GregorGysi, OR from:dieLinke, OR from:Linksfraktion, ' \
        'OR from:Janine_Wissler, OR from:katjakipping, OR from:SWagenknecht, OR Alice_Weidel, ' \
        'OR from:Tino_Chrupalla,OR from:Beatrix_vStorch, OR from:Frohnmaier_AfD, OR from:AfD, OR, from:StBrandner, ' \
        'OR from:AfDimBundestag, OR from:AfDProtschka, OR from:BjoernHoecke, OR from:P_Plattform, ' \
        'OR from:M_HarderKuehnel, OR from:AndreasKalbitz)'

tweets = []
limit = 200000

# looping through each politicians tweets and appending them to tweets
for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.user.username, tweet.content])

# creating a pandas df
columns = ['Date', 'User', 'Tweet']
df = pd.DataFrame(tweets, columns=columns)

# saving to csv
df.to_csv(r'sns_twitter_data.csv')
