import datetime
import requests
import os
import random

from dotenv import load_dotenv
from pathlib import Path
from urllib.parse import urlparse


load_dotenv()

def fetch_spacex_last_launch(url):
    filename = "spacex"
    response = requests.get(url)
    response.raise_for_status()
    pictures = response.json()["links"]["flickr"]["original"]
    for picture_number, picture in enumerate(pictures):
        picture_response = requests.get(picture)
        picture_response.raise_for_status()
        with open(f"images/{filename}_{picture_number}.jpg", "wb") as file:
            file.write(picture_response.content)

def split_link(url):
    parsed_url = urlparse(url)
    extension = os.path.splitext(parsed_url.path)
    return extension[1]

def get_apod_pictures(url, token):
    filename = "nasa_apod"
    payload = {
        "api_key": token,
        "count": 30,
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    response_data = response.json()
    photo_url = []
    for urls in response_data:
        photo_url.append(urls["url"])
    for picture_number, picture in enumerate(photo_url):
        picture_response = requests.get(picture)
        picture_response.raise_for_status()
        with open(f"images/{filename}_{picture_number}{split_link(picture)}", "wb") as file:
            file.write(picture_response.content)

def get_epic_picrures(url, token):
    photo_url = []
    filename = "nasa_epic"
    payload = {
        "api_key": token,
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    response_images = response.json()
    for picture in response_images:
        name = picture["image"]
        date = datetime.datetime.fromisoformat(picture["date"]).date().strftime("%Y/%m/%d")
        url = f"https://api.nasa.gov/EPIC/archive/natural/{date}/png/{name}.png"
        photo_url.append(url)
    for picture_number, picture in enumerate(photo_url):
        picture_response = requests.get(picture, params=payload)
        picture_response.raise_for_status()
        with open(f"images/{filename}_{picture_number}{split_link(picture)}", "wb") as file:
            file.write(picture_response.content)

def main():
    Path("./images").mkdir(parents=True, exist_ok=True)
    url = "https://api.nasa.gov/EPIC/api/natural/images"
    token = os.environ['NASA_API_TOKEN']


if __name__=="__main__":
    main()