from loguru import logger
from telebot import TeleBot
from telebot.types import Message

from app.config import config
from app.resources import messages
from app.resources.messages import INFO_TEMPLATE
from app.services.requests import get_all_computers, get_software
from app.services.utility import get_args, save_software_file

bot = TeleBot(config.tg_bot_token.get_secret_value())


@bot.message_handler(commands=["help"])
def help_message(message: Message) -> None:
    bot.send_message(message.chat.id, messages.HELP)


@bot.message_handler(commands=["computers"])
def computers_handler(message: Message) -> None:
    computers = get_all_computers()
    logger.info(computers)
    msg = INFO_TEMPLATE.render(computers=computers)
    bot.send_message(message.chat.id, msg)


@bot.message_handler(commands=["software"])
def software_handler(message: Message) -> None:
    try:
        mac_address = get_args(message)[0]
    except ValueError:
        bot.reply_to(message, "wrong arguments")
        return
    software = get_software(mac_address)
    if not software:
        bot.reply_to(message, "no one")
        return

    logger.debug(f"soft {len(software)}, first : {software[0]}")
    save_software_file(software)
    with open("programs.csv", "rb") as sending_csv_file:
        bot.send_document(message.chat.id, sending_csv_file)


bot.polling()
