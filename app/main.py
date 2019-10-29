from telebot import TeleBot
from telebot.types import Message

import app.resources.messages as messages
from app.config import config
from app.services.requests import get_all_computers, get_software
from app.services.utility import get_args


bot = TeleBot(config.tg_bot_token.get_secret_value())


@bot.message_handler(commands=["help"])
def help_message(message: Message) -> None:
    bot.send_message(message.chat.id, messages.HELP)


@bot.message_handler(commands=["computers"])
def get_computers(message: Message) -> None:
    computers = get_all_computers()
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
    software = get_software(mac_address)
    msg = messages.SOFTWARE_TEMPLATE.render(software=software) if software else "no one"
    bot.send_message(message.chat.id, msg)



bot.polling()
