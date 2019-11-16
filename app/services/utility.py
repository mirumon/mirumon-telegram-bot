import io
from typing import List

from telebot.types import Message

from app.resources import messages
from app.schemas.mirumon_responses import Software


def get_args(message: Message) -> List[str]:
    if len(message.text.split()) > 1:
        return message.text.split(" ")[1:]
    raise ValueError


def get_file_as_csv(software: List[Software]) -> io.StringIO:
    msg = messages.PROGRAMS_CSV_TEMPLATE.render(software=software)
    return io.StringIO(msg)
