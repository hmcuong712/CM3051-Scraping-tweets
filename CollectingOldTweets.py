from twitterscraper import query_tweets
import datetime
import codecs, json
import pandas as pd
from nltk.tokenize import WordPunctTokenizer
import re
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Reading main CSV file containing movies
MovieData = pd.read_csv(r'C:\Users\Cuong\Desktop\MovieListFinal.csv')

# Defining function for sentiment analysis
sid = SentimentIntensityAnalyzer()

# For tokenizer
tok = WordPunctTokenizer()
part1 = r'@[A-Za-z0-9].+'
part2 = r'https?://[A-Za-z0-9./]+'
part3 = r'pic.twitter\S+'
part4 = r'#'
combined_pat = r'|'.join((part1, part2, part3, part4))

# Defining data frame for sentiment analysis
df_sentiment = pd.DataFrame(columns=['sentiment', 'volume'])

# Iteration over movies
if __name__ == '__main__':
    i = 0
    df_total = []
    for movie in MovieData.tweetSearch:
        release_date = datetime.datetime.strptime(MovieData.Wide[i], "%m/%d/%Y").date()
        start_date = release_date - datetime.timedelta(days=7)
        tweets = query_tweets(movie, limit=20, lang='en', begindate=start_date, enddate=release_date)
        tweet_list = (t.__dict__ for t in tweets)
        df = pd.DataFrame(tweet_list)

        # Defining variables for counting sentiments
        positive = 0
        negative = 0
        neutral = 0

        # Iteration through each tweet for cleaning and analyzing sentiments
        for o, row in df.iterrows():

            # Cleaning each tweet
            tweet = df.at[o, 'text']  # locating tweets
            tweet = re.sub(combined_pat, '', tweet)  # remove all the unnecessary text
            tweet_tokens = tok.tokenize(tweet.lower())  # lowercase the tweets
            tweet = (" ".join(tweet_tokens)).strip()
            df.at[o, 'text'] = tweet

            # sentiment analysis using NLTK Vader
            ss = sid.polarity_scores(tweet)
            compound = float(ss['compound'])
            if compound > 0.05:
                positive += 1
            elif compound < -0.05:
                negative += 1
            else:
                neutral += 1

        # Exporting the data frame into csv files
        sentimentScore = (positive - negative) / (positive + negative + neutral)
        df_sentiment = df_sentiment.append({'sentiment': sentimentScore, 'volume': len(df.index)}, ignore_index=True)
        file_name = movie + ".csv"
        df.to_csv(file_name, index=False, encoding='utf-8')
        df_sentiment.to_csv('sentimentscore.csv', index=False)
        i += 1
