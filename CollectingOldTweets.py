from twitterscraper import query_tweets
import datetime
import codecs, json
import pandas as pd
from nltk.tokenize import WordPunctTokenizer
import re

# reading main CSV file
MovieData = pd.read_csv(r'C:\Users\Cuong\Desktop\MovieListFinal.csv')

# if you want to contain all the tweets in one file, append to the
# existing data frame.

# For tokenizer
tok = WordPunctTokenizer()
part1 = r'@[A-Za-z0-9].+'
part2 = r'https?://[A-Za-z0-9./]+'
part3 = r'pic.twitter\S+'
part4 = r'#'
combined_pat = r'|'.join((part1, part2, part3, part4))


# Iteration over movies
if __name__ == '__main__':
    i = 0
    df_total = []
    for movie in MovieData.tweetSearch:
        release_date = datetime.datetime.strptime(MovieData.Wide[i], "%m/%d/%Y").date()
        start_date = release_date - datetime.timedelta(days=7)
        tweets = query_tweets(movie, lang='en', begindate=start_date, enddate=release_date)
        tweet_list = (t.__dict__ for t in tweets)
        df = pd.DataFrame(tweet_list)

        # Space for cleaning dataframe (of each movie's tweet)
        for o, row in df.iterrows():
            tweet = df.at[o, 'text']
            tweet = re.sub(combined_pat, '', tweet)
            tweet_tokens = tok.tokenize(tweet.lower())
            tweet = (" ".join(tweet_tokens)).strip()
            df.at[o, 'text'] = tweet

        # Exporting the data frame into csv files
        file_name = movie + ".csv"
        df.to_csv(file_name, index=False, encoding='utf-8')
        i += 1

