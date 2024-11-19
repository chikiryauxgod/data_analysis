import requests
from requests.exceptions import RequestException
def rows_counter(url):
    try: 
        response = requests.get(url, timeout = 3)
        csv = response.text.strip().split("\n")
        print(f"Total rows: {len(csv)}")

    except RequestException as e:
        print(f"Error: {e}")

url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_month.csv"
rows_counter(url)