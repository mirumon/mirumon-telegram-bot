from uuid import UUID

from pydantic import BaseModel


class Computer(BaseModel):
    name: str
    username: str
    domain: str


class EventComputeDetails(BaseModel):
    type: str
    id: UUID


class ComputerDetails(BaseModel):
    event: EventComputeDetails
