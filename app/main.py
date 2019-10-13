import requests
from loguru import logger
from telebot import TeleBot
from telebot.types import Message

from app.config import SECRET_TOKEN
from app.resurses.const.strings import JOKE
from app.resurses.messages.common import HELLO, HELP

bot = TeleBot(SECRET_TOKEN)

GET_JOKE_API_URL = "http://api.icndb.com/jokes/random"


@bot.message_handler(commands=["start"])
def start_message(message: Message) -> None:
    bot.send_message(message.chat.id, HELLO)


@bot.message_handler(commands=["help"])
def help_message(message: Message) -> None:
    bot.send_message(message.chat.id, HELP)


@bot.message_handler(content_types=["text"])
def send_message(message: Message) -> None:
    logger.debug(f"from: {message.from_user.username}")
    logger.debug(f"text: {message.text}")
    if message.text.lower() == JOKE:
        resp = requests.get(GET_JOKE_API_URL)
        bot.send_message(message.chat.id, resp.json()["value"]["joke"])
    else:
        bot.send_message(message.chat.id, message.text)


bot.polling()
