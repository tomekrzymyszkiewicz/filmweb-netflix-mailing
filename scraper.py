from bs4 import BeautifulSoup
import requests
import pandas as pd

response = requests.get("https://www.filmweb.pl/netflix")
html_soup = BeautifulSoup(response.text, 'html.parser')
movies = []
movies = html_soup.find('section', {"id": "netflixMoviesOfTheMonth"})
titles = []
titles = movies.find_all('h3',{'class':'simplePoster__heading'})
for title in titles:
    title = title.text
    print (title)