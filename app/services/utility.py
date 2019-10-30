import csv
from typing import List

from telebot.types import Message

from app.schemas.response_models import Software


def get_args(message: Message) -> List[str]:
    if len(message.text.split()) > 1:
        return message.text.split(" ")[1:]
    raise ValueError


def save_software_file(software: List[Software]) -> None:
    with open("programs.csv", "w", newline="") as csv_file:
        writer = csv.writer(csv_file, delimiter=",")
        for soft in software:
            writer.writerow([soft.name, soft.vendor, soft.version])
