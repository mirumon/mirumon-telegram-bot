from pydantic import BaseModel


class Computer(BaseModel):
    mac_address: str
    name: str
    username: str
    domain: str
    mac_address: str


class Software(BaseModel):
    name: str
    vendor: str
    version: str
