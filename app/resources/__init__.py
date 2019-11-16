import httpx as httpx

from app.config import config

http_client = httpx.AsyncClient(base_url=config.api_base_url)