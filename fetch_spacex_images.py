import argparse
import requests

from help_scripts import download_pictures

def fetch_spacex_last_launch(url):
    filename = "spacex"
    response = requests.get(url)
    response.raise_for_status()
    pictures = list(response.json()["links"]["flickr"]["original"])
    download_pictures(pictures,filename)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("user_input", nargs='?', type=str, help="Enter ID launch")
    args = parser.parse_args()
    if args.user_input:
        url = f"https://api.spacexdata.com/v5/launches/{args.user_input}"
    else:
        url = f"https://api.spacexdata.com/v5/launches/latest"
    fetch_spacex_last_launch(url)

if __name__ == "__main__":
    main()
