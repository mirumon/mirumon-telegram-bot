from typing import Any

from telebot import TeleBot
from telebot.types import Message
import requests

from app.config import SECRET_TOKEN

bot = TeleBot(SECRET_TOKEN)


@bot.message_handler(commands=["start"])
def start_message(message: Message) -> Any:
    bot.send_message(message.chat.id, "Hello, i'm Viki")


@bot.message_handler(commands=["help"])
def start_message(message: Message) -> Any:
    bot.send_message(message.chat.id, "you can say me: \nhello \njoke")


@bot.message_handler(content_types=["text"])
def send_message(message: Message) -> Any:
    print(message.from_user.username)
    print(message.text)
    if message.text.lower() == "joke":
        r = requests.get("http://api.icndb.com/jokes/random")
        return bot.send_message(message.chat.id, r.json()["value"]["joke"])
    elif message.from_user.username.lower() == "nsidnev":
        with open("doggo.jpg", "rb") as file:
            return bot.send_photo(message.chat.id, file)
    else:
        return bot.send_message(message.chat.id, message.text)


bot.polling()
