from urllib.request import urlopen 
from bs4 import BeautifulSoup as bs 

def get_links(url):
    try:
        with urlopen(url) as response:
            html = response.read()
            soup = bs(html, "html.parser")
            links = soup.find_all('a', href = True)
            list_links = [link['href'] for link in links]
            for link in list_links:
                print(link)

    except Exception as e:    
        print(f"Error: {e}")

url = "https://en.wikipedia.org/wiki/Python"
get_links(url)