from typing import List

import requests
from loguru import logger

from app.config import config
from app.schemas.response_models import Computer, Software


def get_all_computers() -> List[Computer]:
    resp = requests.get(config.api_base_url + "/computers")
    if resp.status_code != requests.codes.ok:
        logger.error(resp.status_code)
        return []
    computers = [Computer(**computer) for computer in resp.json()]
    computers.sort(key=lambda cmp: cmp.domain)
    return computers


def get_software(mac_adres: str) -> List[Software]:
    resp = requests.get(
        config.api_base_url + f"/computers/{mac_adres}/installed-programs"
    )
    if resp.status_code != requests.codes.ok:
        logger.error(resp.status_code)
        return []
    return [Software(**software) for software in resp.json()]
