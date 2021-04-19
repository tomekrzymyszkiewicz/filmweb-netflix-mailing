from typing import Text
from bs4 import BeautifulSoup
import requests

def get_films_of_month():
    response = requests.get("https://www.filmweb.pl/netflix")
    html_soup = BeautifulSoup(response.text, 'html.parser')
    movies_page = html_soup.find('section', {"id": "netflixMoviesOfTheMonth"})
    movies = [{'title': '','poster': '','rate': 0, 'description': "", 'review': "", "link": '', 'sort_rate': 0}]
    movies.clear()
    for movie in movies_page.find_all('a', class_ ='simplePoster__title'):
        movies.append({'title': '','poster': '','rate': 0, 'description': "", 'link': "https://www.filmweb.pl"+movie['href']})
    
    for movie_number in range(0,len(movies)):
        movie = movies[movie_number]
        response = requests.get(movie['link'])
        html_soup = BeautifulSoup(response.text, 'html.parser')
        movie['title'] = html_soup.find('h1').span.text
        movie['poster'] = html_soup.find('img', id = 'filmPoster')['content']
        movie['rate'] = html_soup.find('span', class_ = 'filmRating__rateValue').text.strip() + " (" + html_soup.find('span', class_ = 'filmRating__count').    text.strip() + ")"
        movie['sort_rate'] = html_soup.find('span', class_ = 'filmRating__rateValue').text.strip()
        movie['description'] = html_soup.find('span', itemprop = 'description').text

    movies.sort(key=lambda item: item.get('sort_rate'),reverse=True)

    return movies
