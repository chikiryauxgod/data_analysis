import requests
from requests.exceptions import RequestException

def get_doc(url):
    try:
        response = requests.get(url, timeout = 3)
        if (response.status_code == 200):
            print(f"Content of {url} is:\n {response.text}")
        else:
            print(f"Failed to get robots.txt from {url} with status code: {response.status_code}    ")
    except RequestException as e:
        print(f"Failed to get robots.txt from {url} with error: {e}")

url = 'https://en.wikipedia.org/robots.txt'
get_doc(url)