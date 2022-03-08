from pydantic import BaseModel
from typing import List


class Character(BaseModel):
    name: str
    status: str
    species: str
    type: str
    gender: str
    episode: List

    class Config:
        orm_mode = True


class Episode(BaseModel):
    id: int
    name: str
    air_date: str
    episode: str
    character: List

    class Config:
        orm_mode = True
