from bs4 import BeautifulSoup as bs
import urllib.request
import pandas as pd
import requests
import lxml

url = 'https://www.boxofficemojo.com/yearly/chart/?yr=2016&p=.htm'
html = urllib.request.urlopen(url).read()
soup = bs(html, 'html.parser')

getTable = soup.find_all('table', attrs={'cellspacing':'1'})
print(getTable)