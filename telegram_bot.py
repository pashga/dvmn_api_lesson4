import random
import telegram
import os
import time
import argparse

from dotenv import load_dotenv

def main():
    load_dotenv()
    bot = telegram.Bot(token=os.environ["TELEGRAM_BOT_TOKEN"])
    list_images = os.listdir("images")
    random.shuffle(list_images)
    parser = argparse.ArgumentParser(description="Publish images to Telegram channel")
    parser.add_argument("post_delay",
                        help='Posting delay in hours',
                        type=float,
                        nargs='?',
                        default=4)
    post_delay = parser.parse_args().post_delay
    while True:
        for picture in list_images:
            with open(f"images/{picture}", "rb") as photo:
                bot.send_photo(chat_id=os.environ["TELEGRAM_CHAT_ID"], photo=photo)
                time.sleep(post_delay * 3600)
        random.shuffle(list_images)

if __name__ == "__main__":
    main()
