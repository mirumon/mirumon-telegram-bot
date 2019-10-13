from typing import Any

import requests
from loguru import logger
from telebot import TeleBot
from telebot.types import Message

from app.config import SECRET_TOKEN

bot = TeleBot(SECRET_TOKEN)


@bot.message_handler(commands=["start"])
def start_message(message: Message) -> Any:
    bot.send_message(message.chat.id, "Hello, i'm Viki")


@bot.message_handler(commands=["help"])
def help_message(message: Message) -> Any:
    bot.send_message(message.chat.id, "you can say me: \nhello \njoke")


@bot.message_handler(content_types=["text"])
def send_message(message: Message) -> Any:
    logger.debug(message.from_user.username)
    logger.debug(message.text)
    if message.text.lower() == "joke":
        resp = requests.get("http://api.icndb.com/jokes/random")
        return bot.send_message(message.chat.id, resp.json()["value"]["joke"])
    return bot.send_message(message.chat.id, message.text)


bot.polling()
