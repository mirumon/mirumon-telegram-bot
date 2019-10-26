import requests
from telebot import TeleBot
from telebot.types import Message

from app.config import SECRET_TOKEN
from app.resources.messages.common import HELLO, HELP

bot = TeleBot(SECRET_TOKEN)

GET_JOKE_API_URL = "http://api.icndb.com/jokes/random"


@bot.message_handler(commands=["start"])
def start_message(message: Message) -> None:
    bot.send_message(message.chat.id, HELLO)


@bot.message_handler(commands=["help"])
def help_message(message: Message) -> None:
    bot.send_message(message.chat.id, HELP)


@bot.message_handler(commands=["joke"])
def joke(message: Message) -> None:
    resp = requests.get(GET_JOKE_API_URL)
    bot.send_message(message.chat.id, resp.json()["value"]["joke"])


bot.polling()
