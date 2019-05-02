from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver
import pandas as pd

#define function for getting revenue's URL
def gettingURL(moviename):
    browser = webdriver.Chrome()
    browser.get(('https://www.boxofficemojo.com/'))

    searchFunction = browser.find_element_by_xpath('//form/input[1]')
    searchFunction.send_keys(moviename)

    searchButton = browser.find_element_by_xpath('//form/input[2]')
    searchButton.click()

    #movieLink = browser.find_element_by_xpath('//tr[2]/td[1]/b/font/a')
    movieLink = browser.find_element_by_link_text(moviename)
    movieLink.click()

    try:
        foreignLink = browser.find_element_by_link_text("Foreign")
        foreignLink.click()
    except:
        return 'wrong URL'
    return browser.current_url

#reading csv file
MovieData = pd.read_csv(r'C:\Users\Cuong\Desktop\MovieListFinal.csv')

newFrame = []

for movie in MovieData.film:
    movie = str(movie)
    #Getting the data by BeautifulSoup
    url = gettingURL(movie)

    page = urllib.request.urlopen(url)

    soup = BeautifulSoup(page, 'html.parser')

    #Extracting all information within the 'Foreign' section
    tr = soup.find_all('tr')
    revenue = []
    for i in tr:
            children = i.findChildren("font", recursive=True)
            for child in children:
                revenue.append(child.text)

    #list comprehension to get opening weekend's revenue
    revenue = [x for x in revenue if x[0] == '$' or x[0] == 'n']
    #print(revenue[0])
    newFrame.append({'Opening Weekend Revenue': revenue[0]})
    print(pd.DataFrame(newFrame))
#pd.DataFrame(newFrame).to_csv(index=False)
