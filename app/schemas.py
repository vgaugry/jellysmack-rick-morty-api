from pydantic import BaseModel
from typing import List, Optional


class Character(BaseModel):
    name: str
    status: str
    species: str
    type: str
    gender: str
    episode: List
    comment: Optional[List]

    class Config:
        orm_mode = True


class Episode(BaseModel):
    id: int
    name: str
    air_date: str
    episode: str
    character: List
    comment: Optional[List]

    class Config:
        orm_mode = True


class CommentCreate(BaseModel):
    comment: str
    character_id: int = None
    episode_id: int = None


class Comment(CommentCreate):
    id: int

    class Config:
        orm_mode = True


