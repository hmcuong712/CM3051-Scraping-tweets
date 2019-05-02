import requests
import locale
import pandas
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

locale.setlocale(locale.LC_ALL, '')

#API Key
api_key = "175390378119bb555087694731fdc1cf"

response = requests.get('https://api.themoviedb.org/3/discover/movie?api_key=' + api_key
                        + '&primary_release_year=2016&sort_by=popularity.desc&page=3')

highest_popularity = response.json()
#viewing json structure

highest_popularity_films = highest_popularity['results']

#define column names
columns = ['film', 'popularity', 'vote score']
df = pandas.DataFrame(columns=columns)

for film in highest_popularity_films:
    film_popularity = requests.get('https://api.themoviedb.org/3/movie/'
                                + str(film['id']) +'?api_key='+ api_key+'&language=en-US')
    film_popularity = film_popularity.json()
    df.loc[len(df)] = [film['title'], film_popularity['popularity'], film_popularity['imdb_id']]
print(df.head(30))

export_csv = df.to_csv(r'C:\Users\Cuong\Desktop\Movielist2.csv')
