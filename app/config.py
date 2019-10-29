import os

from pydantic import BaseSettings, BaseConfig, SecretStr
from pydantic.fields import Field

TG_API_ID = str(os.getenv("TG_API_ID"))
TG_API_HASH = str(os.getenv("TG_API_HASH"))
TG_BOT_TOKEN = str(os.getenv("TG_BOT_TOKEN"))

API_BASE_URL = str(os.getenv("API_BASE_URL"))


class Config(BaseSettings):
    tg_api_id: SecretStr
    tg_api_hash: SecretStr
    tg_bot_token: SecretStr
    api_base_url: str

    class Config:
        case_sensitive = False


config = Config()
