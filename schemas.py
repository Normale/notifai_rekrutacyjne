from pydantic import BaseModel
from pydantic.types import constr


class MessageBase(BaseModel):
    text: constr(min_length=1, max_length=160)


class MessageCreate(MessageBase):
    pass


class Message(MessageBase):
    views: int
    nr: int

    class Config:
        orm_mode = True
