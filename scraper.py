from bs4 import BeautifulSoup
import requests
import pandas as pd

response = requests.get("https://www.filmweb.pl/netflix")
html_soup = BeautifulSoup(response.text, 'html.parser')
movies = []
movies = html_soup.find('section', {"id": "netflixMoviesOfTheMonth"})
mailing = [{'title': '','poster': '','rate': 0, 'description': "", 'review': "", "link": ''}]
mailing.clear()
# titles = movies.find_all('h3',{'class':'simplePoster__heading'})
for movie in movies.find_all('a', class_ ='simplePoster__title'):
    mailing.append({'title': '','poster': '','rate': 0, 'description': "", 'review': "", 'link': "https://www.filmweb.pl"+movie['href']})

    print ("https://www.filmweb.pl"+movie['href'])


# for title in movies.find_all('h3',{'class':'simplePoster__heading'}):
#     mailing.append({'title': title.text,'poster': '','rate': 0, 'description': "", 'review': ""})



