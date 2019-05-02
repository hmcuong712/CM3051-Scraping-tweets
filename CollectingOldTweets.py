from twitterscraper import query_tweets
import datetime
import codecs, json
import pandas as pd

# reading main CSV file
MovieData = pd.read_csv(r'C:\Users\Cuong\Desktop\MovieListFinal.csv')

# if you want to contain all the tweets in one file, append to the
# existing dataframe.


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

        # Exporting the dataframe into csv files
        file_name = movie + ".csv"
        df.to_csv(file_name, index=False, encoding='utf-8')
        i += 1

