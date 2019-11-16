from typing import List

from telebot.types import Message


def get_args(message: Message) -> List[str]:
    if len(message.text.split()) > 1:
        return message.text.split(" ")[1:]
    raise ValueError
