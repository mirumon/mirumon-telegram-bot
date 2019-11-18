from pydantic import BaseSettings, HttpUrl, SecretStr


class Settings(BaseSettings):
    tg_app_id: SecretStr = ""
    tg_hash: SecretStr = ""
    tg_bot_token: SecretStr = ""
    api_base_url: HttpUrl = "https://google.com"

    class Config:  # noqa: WPS431
        case_sensitive = False


config = Settings()
