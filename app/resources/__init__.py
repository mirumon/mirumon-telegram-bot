import httpx

from app.config import config

http_client = httpx.Client(base_url=config.api_base_url, timeout=15)
