import requests
from geturl import get_url
from requests.exceptions import RequestException

def check_webpage(url):
    print(f"Webpage: {url}")
    try:
        response = requests.get(url, timeout = 3)

        if (response.status_code == 200):
            print(f"The page was found with code: {response.status_code}")
        else:
            print(f"The page wasn't found with code {response.status_code}")

    except RequestException as e:
        print(f'Connection error: {e}')


url = get_url()
check_webpage(url)
