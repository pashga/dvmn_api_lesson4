import datetime
import requests
import os

from help_scripts import download_pictures
from dotenv import load_dotenv


def get_epic_picrures(token):
    photo_url = []
    filename = "nasa_epic"
    url = "https://api.nasa.gov/EPIC/api/natural/images"
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
    download_pictures(photo_url,filename, payload=payload)

def main():
    load_dotenv()
    token = os.environ['NASA_API_TOKEN']
    get_epic_picrures(token)

if __name__ == "__main__":
    main()