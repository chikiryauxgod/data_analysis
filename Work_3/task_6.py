from urllib.request import urlopen 
from bs4 import BeautifulSoup as bs 

def get_headers(url):
    try:
        with urlopen(url) as response:
            html = response.read()
            soup = bs(html, "html.parser")
            headers = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])
            for header in headers:
                print(header.text)
    except Exception as e:
        print(f"Error: {e}")
    

url = "https://en.wikipedia.org/wiki/Main_Page"
get_headers(url)