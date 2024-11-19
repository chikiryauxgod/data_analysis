import requests
import random
from bs4 import BeautifulSoup as bs
from requests.exceptions import RequestException

#movies долго делает запросы и только потом выводит результат в терминал, нужно множко подождать 

def get_description(url, headers):
    try:
        response = requests.get(url, headers = headers, timeout = 3)
        soup = bs(response.text, "html.parser")
        movies = []
        film_list = soup.select('li.ipc-metadata-list-summary-item')

        for film in film_list:
            title = film.find("h3", class_="ipc-title__text").get_text()
            link_tags = film.select("a.ipc-lockup-overlay")

            for tag in link_tags:
                film_link = "https://www.imdb.com" + tag.get("href")

            response = requests.get(film_link, headers = headers)
            soup = bs(response.text, "html.parser")

            film_description = soup.find("p", class_="sc-3ac15c8d-3")
            film_description = film_description.find("span", {"class": "sc-3ac15c8d-2 fXTzFP"}).get_text()
            movies.append([title, film_description])

        random.shuffle(movies)

        return movies

    except RequestException as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")


def print_movies():
    url = "https://www.imdb.com/chart/top"
    headers = {'User-Agent':'Mozilla/6.0'}
    movies = get_description(url, headers)
    
    if not movies:
        print("Couldn't get movies.")
        return

    for movie in movies:
        print(movie[0])  
        print(movie[1]) 

print_movies()
