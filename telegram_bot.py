import telegram
import os

from dotenv import load_dotenv

load_dotenv()
bot = telegram.Bot(token=os.environ["TELEGRAM_BOT_TOKEN"])
bot.send_photo(chat_id=os.environ["TELEGRAM_CHAT_ID"], photo=open("images/spacex_2.jpg", "rb"))

