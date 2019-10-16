import typing

import requests
from loguru import logger
from telebot import TeleBot
from telebot.types import Message

from app.config import API_BASE_URL, SECRET_TOKEN
from app.resources.const.strings import JOKE
from app.resources.messages.common import HELLO, HELP
from app.schemas.response_models import Computer

typing.cast(str, API_BASE_URL)
typing.cast(str, SECRET_TOKEN)

bot = TeleBot(SECRET_TOKEN)

GET_JOKE_API_URL = "http://api.icndb.com/jokes/random"


@bot.message_handler(commands=["start"])
def start_message(message: Message) -> None:
    bot.send_message(message.chat.id, HELLO)


@bot.message_handler(commands=["help"])
def help_message(message: Message) -> None:
    bot.send_message(message.chat.id, HELP)


@bot.message_handler(commands=["computers"])
def get_computers(message: Message) -> None:
    resp = requests.get(str(API_BASE_URL) + "/computers")
    if resp.status_code != requests.codes.ok:
        logger.error(resp.status_code)
        bot.send_message(message.chat.id, "not ok response")
        return
    computers = [Computer(**computer) for computer in resp.json()]
    computers.sort(key=lambda cmp: cmp.domain)
    msg = ""
    for computer in computers:
        tmp_domain = ""
        if computer.domain != tmp_domain:
            msg += f"\n In domain {computer.domain}\n\n"
        msg += f"{computer.name} [{computer.username}]\n"
    bot.send_message(message.chat.id, msg)


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
