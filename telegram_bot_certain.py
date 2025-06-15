import random
import telegram
import os
import time
import argparse

from dotenv import load_dotenv

def main():
    load_dotenv()
    bot = telegram.Bot(token=os.environ["TELEGRAM_BOT_TOKEN"])
    parser = argparse.ArgumentParser(description="Publish certain image to Telegram channel")
    parser.add_argument("image_path",
                        help='Please enter image path',
                        type=str,)
    image_path = parser.parse_args().image_path
    with open(image_path, "rb") as photo:
        bot.send_photo(chat_id=os.environ["TELEGRAM_CHAT_ID"], photo=photo)

if __name__ == "__main__":
    main()
