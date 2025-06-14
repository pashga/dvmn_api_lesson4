import requests
import os

from pathlib import Path
from urllib.parse import urlparse



def split_link(url):
    parsed_url = urlparse(url)
    extension = os.path.splitext(parsed_url.path)
    return extension[1]


def download_pictures(urls, filename, payload=None):
    Path("./images").mkdir(parents=True, exist_ok=True)
    for picture_number, picture in enumerate(urls):
        picture_response = requests.get(picture, params=payload)
        picture_response.raise_for_status()
        with open(f"images/{filename}_{picture_number}.{split_link(picture)}", "wb") as file:
            file.write(picture_response.content)
