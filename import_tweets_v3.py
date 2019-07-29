import tweepy
import pandas as pd
import datetime

def get_tweets_currency(currency_string):

    # Fill the X's with the credentials obtained by
    # following the above mentioned procedure.
    consumer_key = "ppYzHrFU1kNASe9lSwqKK2V5m"
    consumer_secret = "O3AOhcRQp38tZiDB5kvGNrCR116NVDUZfQGicCmx7LKLMlCyle"
    access_key = "1100766433267630082-UzcE7froIPyVcf9srPh2uKBs3G4FwO"
    access_secret = "jRhNmFwdk3CAlR4F9JnwR46D31GmQPv2z0q8sAvvWSl80"

    # Authorization to consumer key and consumer secret
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    # Access to user's access key and access secret
    auth.set_access_token(access_key, access_secret)

    # Calling api
    api = tweepy.API(auth)

    #searchQuery = 'USDJPY OR USD/JPY' # Keyword
    searchQuery = currency_string
    print(currency_string)

    tweets_all = tweepy.Cursor(api.search,
                               q=searchQuery,
                               include_entities=True,
                               show_user=True,
                               rpp=400,
                               since="2019-05-13",
                               until="2019-05-18",
                               lang="en").items(400)

    message, favorite_count, retweet_count, created_at, user_name = [], [], [], [], []
    for tweet in tweets_all:
        message.append(tweet.text)
        favorite_count.append(tweet.favorite_count)
        retweet_count.append(tweet.retweet_count)
        created_at.append(tweet.created_at)
        user_name.append(tweet.user.name)

    df = pd.DataFrame({'Message': message,
                       'Favorite Count': favorite_count,
                       'Retweet Count': retweet_count,
                       'Created At': created_at,
                       'Source': user_name})
    print(len(df))
    #df = df[(df['Created At'] >= pd.to_datetime(datetime.date(2019,5,3)))]
    print(len(df))

    return df