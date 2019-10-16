from pydantic import BaseModel


class Computer(BaseModel):
    name: str
    username: str
    domain: str
    mac_address: str
