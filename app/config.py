from pydantic import BaseSettings, HttpUrl, SecretStr


class Settings(BaseSettings):
    tg_api_id: SecretStr
    tg_api_hash: SecretStr
    tg_bot_token: SecretStr
    api_base_url: HttpUrl

    class Config:
        case_sensitive = False


config = Settings()
