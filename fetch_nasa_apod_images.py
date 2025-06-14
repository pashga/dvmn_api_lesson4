import requests
import os

from help_scripts import download_pictures
from dotenv import load_dotenv

load_dotenv()

def get_apod_pictures(token):
    photo_url = []
    filename = "nasa_apod"
    url = "https://api.nasa.gov/planetary/apod"
    payload = {
        "api_key": token,
        "count": 50,
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    response_data = response.json()

    for urls in response_data:
        photo_url.append(urls["url"])
    download_pictures(photo_url,filename)


token = os.environ['NASA_API_TOKEN']
get_apod_pictures(token)