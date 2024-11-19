import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup as bs
def get_header(url):
    try:
        response = requests.get(url, timeout = 3)
        if (response.status_code == 200):
            soup = bs(response.text, 'html.parser')
            h1 = soup.find('h1')
            if h1:
                print(f"h1 of {url} is:\n {h1.text}")
            else:
                print(f"Failed to h1 header from {url} with status code: {response.status_code} ")
    except RequestException as e:
        print(f"Failed to get h1 header from {url} with error: {e}")

url = 'http://www.example.com/'
get_header(url)