from pydantic import BaseModel


class EchoRequest(BaseModel):
    message: str


class ItemCreate(BaseModel):
    name: str


class Item(BaseModel):
    id: int
    name: str
