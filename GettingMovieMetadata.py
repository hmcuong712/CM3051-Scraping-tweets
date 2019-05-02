import requests
import pandas as pd

#API key
api_key = 'f0b53fce'

#Reading the current list of movie
MovieData = pd.read_csv(r'C:\Users\Cuong\Desktop\MovieListFinal.csv')

#Initiate a new table containing metadata
columns = ['Genre', 'Actors', 'Rated', 'imdbRating']
df = pd.DataFrame(columns=columns)

for movie in MovieData.film:
    movie = str(movie)
    response = requests.get('http://www.omdbapi.com/' + '?apikey=f0b53fce' + '&t=' + movie + '&y=2016')
    movieChar = response.json()
    print(movieChar)
    #filling in the previous table
    df.loc[len(df)] = [movieChar['Genre'], movieChar['Actors'], movieChar['Rated'], movieChar['imdbRating']]

    #exporting these metadata to csv file
print(df.head(30))
export_csv = df.to_csv(r'C:\Users\Cuong\Desktop\MovieMetaData.csv')