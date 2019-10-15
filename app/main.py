import requests
from loguru import logger
from telebot import TeleBot
from telebot.types import Message

from app.config import SECRET_TOKEN, API_BASE_URL
from app.resources.const.strings import JOKE
from app.resources.messages.common import HELLO, HELP
from app.schemas.response_models import Computer

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
    resp = requests.get(API_BASE_URL + "/computers")
    if not resp.status_code == 200:
        logger.error(resp.status_code)
        return
    computers = [Computer(**computer) for computer in resp.json()]
    for computer in computers:
        bot.send_message(message.chat.id,
                         "\n".join([
                             f"In domain '{computer.domain}'",
                             f"{computer.name} [{computer.username}]"
                         ])
                         )


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
