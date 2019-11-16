from typing import List

import httpx
from httpx import StatusCode
from loguru import logger

from app.config import config
from app.schemas.response_models import Computer, Software
from app.resources import http_client


class BadResponse(Exception):
    def __init__(self, status_code: int) -> None:
        self.status_code = status_code


def get_all_computers() -> List[Computer]:
    resp = http_client.get("/computers")
    if is_error(resp.status_code):
        logger.error(resp.status_code)
        raise BadResponse(resp.status_code)
    computers = [Computer(**computer) for computer in resp.json()]
    computers.sort(key=lambda cmp: cmp.domain)
    return computers


def get_software(mac_address: str) -> List[Software]:
    resp = http_client.get(f"/computers/{mac_address}/installed-programs")
    if is_error(resp.status_code):
        logger.error(resp.status_code)
        raise BadResponse(resp.status_code)
    return [Software(**software) for software in resp.json()]


def is_error(status_code: int) -> bool:
    is_server_error = StatusCode.is_server_error(status_code)
    is_client_error = StatusCode.is_client_error(status_code)
    return is_server_error or is_client_error
