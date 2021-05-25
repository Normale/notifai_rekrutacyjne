from pydantic import BaseModel
from pydantic.types import constr
from typing import List, Dict


class MessageBase(BaseModel):
    text: constr(min_length=1, max_length=160)


class MessageCreate(MessageBase):
    pass


class Message(MessageBase):
    views: int
    nr: int

    class Config:
        orm_mode = True


class JSONDetailedResponse(BaseModel):
    class Config:
        schema_extra = {
            "example": {"detail": "There is detailed description"},
        }


def json_detailed_responses(error_codes: List[int]) -> Dict[int, JSONDetailedResponse]:
    c = {"model": JSONDetailedResponse}
    d = {e: c for e in error_codes}
    return d