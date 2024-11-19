import requests
from requests.exceptions import RequestException

def get_details(url):
    try:
        response = requests.get(url, timeout = 3)
        print(f"Status code: {response.status_code}")
        print(f"Headers: {response.headers}")
        print(f"Url: {response.url}")
        print(f"History: {response.history}")
        print(f"Encoding: {response.encoding}")
        print(f"Reason: {response.reason}")
        print(f"Cookies: {response.cookies}")
        print(f"Elapsed: {response.elapsed}")
        print(f"Request: {response.request}")
        print(f"Content: {response.text[:500]}...") # первые 500, чтобы в консоли не было бардака

    except RequestException as e:
        print(f"Request exception: {e}")




url = "https://python.org/"
get_details(url)