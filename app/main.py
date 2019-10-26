from typing import List

from telebot import TeleBot
from telebot.types import Message

import app.resources.messages as messages
from app.config import SECRET_TOKEN
from app.services.requests import get_all_computers
from app.services.requests import get_software

bot = TeleBot(SECRET_TOKEN)

GET_JOKE_API_URL = "http://api.icndb.com/jokes/random"


@bot.message_handler(commands=["start"])
def start_message(message: Message) -> None:
    bot.send_message(message.chat.id, messages.HELLO)


@bot.message_handler(commands=["help"])
def help_message(message: Message) -> None:
    bot.send_message(message.chat.id, messages.HELP)


@bot.message_handler(commands=["computers"])
def get_computers(message: Message) -> None:
    computers = await get_all_computers()
    msg = ""
    for computer in computers:
        tmp_domain = ""
        if computer.domain != tmp_domain:
            msg += f"\n In domain {computer.domain}\n\n"
        msg += f"{computer.name} [{computer.username} <{computer.mac_address}>]\n"
    bot.send_message(message.chat.id, msg)


@bot.message_handler(commands=["software"])
def get_software(message: Message) -> None:
    mac_address = get_args(message)[0]
    software = await get_software(mac_address)
    msg = "no one"
    for programme in software:
        msg = "\n".join([
            f"name: {programme.name}",
            f"vendor: {programme.vendor}",
            f"version: {programme.version}",
            ""
        ])
    bot.send_message(message.chat.id, msg)


def get_args(message: Message) -> List[str]:
    return message.text.split()[1:]


bot.polling()
