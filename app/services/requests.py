from typing import List

import httpx
from httpx.status_codes import StatusCode
from loguru import logger

from app.config import config
from app.schemas.response_models import Computer, Software


class BadResponse(Exception):
    def __init__(self, status_code: int):
        self.status_code = status_code


def get_all_computers() -> List[Computer]:
    resp = httpx.get(f"{config.api_base_url}/computers")
    is_server_error = StatusCode.is_server_error(resp.status_code)
    is_client_error = StatusCode.is_client_error(resp.status_code)
    if is_client_error or is_server_error:
        logger.error(resp.status_code)
        raise BadResponse(resp.status_code)
    computers = [Computer(**computer) for computer in resp.json()]
    computers.sort(key=lambda cmp: cmp.domain)
    return computers


def get_software(mac_adres: str) -> List[Software]:
    resp = httpx.get(f"{config.api_base_url}/computers/{mac_adres}/installed-programs")
    is_server_error = StatusCode.is_server_error(resp.status_code)
    is_client_error = StatusCode.is_client_error(resp.status_code)
    if is_client_error or is_server_error:
        logger.error(resp.status_code)
        raise BadResponse(resp.status_code)
    return [Software(**software) for software in resp.json()]
