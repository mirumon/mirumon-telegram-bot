import io
from typing import List

from telebot.types import Message

from app.schemas.response_models import Software


def get_args(message: Message) -> List[str]:
    if len(message.text.split()) > 1:
        return message.text.split(" ")[1:]
    raise ValueError


def get_string_io_with_software(software: List[Software]) -> io.StringIO:
    msg = "\n".join([f"{soft.name},{soft.vendor},{soft.version}" for soft in software])
    return io.StringIO(msg)
