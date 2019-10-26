import requests
from telebot import TeleBot
from telebot.types import Message

from app.config import SECRET_TOKEN
from app.resources.messages.common import HELLO, HELP
from app.services.requests import get_all_computers

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
    computers = get_all_computers()
    msg = ""
    for computer in computers:
        tmp_domain = ""
        if computer.domain != tmp_domain:
            msg += f"\n In domain {computer.domain}\n\n"
        msg += f"{computer.name} [{computer.username}]\n"
    bot.send_message(message.chat.id, msg)


@bot.message_handler(commands=["joke"])
def joke(message: Message) -> None:
    resp = requests.get(GET_JOKE_API_URL)
    bot.send_message(message.chat.id, resp.json()["value"]["joke"])


bot.polling()
