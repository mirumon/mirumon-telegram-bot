from telebot import TeleBot
from telebot.types import Message

from app.config import config
from app.resources import messages
from app.services.requests import BadResponse, get_all_computers, get_software
from app.services.utility import get_args, get_string_io_with_software

bot = TeleBot(config.tg_bot_token.get_secret_value())


@bot.message_handler(commands=["help"])
def help_message(message: Message) -> None:
    bot.send_message(message.chat.id, messages.HELP.render())


@bot.message_handler(commands=["computers"])
def computers_handler(message: Message) -> None:
    try:
        computers = get_all_computers()
    except BadResponse as exc:
        bot.reply_to(message, f"bad response ({exc.status_code})")
        return
    msg = messages.INFO_TEMPLATE.render(computers=computers)
    bot.send_message(message.chat.id, msg)


@bot.message_handler(commands=["software"])
def software_handler(message: Message) -> None:
    try:
        mac_address = get_args(message)[0]
    except ValueError:
        bot.reply_to(message, messages.WRONG_ARGUMENTS)
        return
    try:
        software = get_software(mac_address)
    except BadResponse as exc:
        bot.reply_to(message, messages.NOT_RESPONDING)
        return
    if not software:
        bot.reply_to(message, messages.NO_ONE)
        return

    csv_file = get_string_io_with_software(software)
    with open(csv_file.read(), "rb") as sending_csv_file:
        bot.send_document(message.chat.id, sending_csv_file)


bot.polling()
