import requests
from geturl import get_url
from requests.exceptions import SSLError

def check_ssl(url):
    print(f"Webpage: {url}")
    if url.startswith('https://'):
        try:
            response = requests.get(url, timeout = 3)

            if (response.status_code == 200):
                print(f"The page {url} supports the SSL certificate")
            else:
                print(f"The page wasn't found with code {response.status_code}")

        except SSLError as e:
            print(f"Connection error: {e}")

    else:
        print(f"The page {url} doesn't supports the SSL certificate")            


url = get_url()
check_ssl(url)

