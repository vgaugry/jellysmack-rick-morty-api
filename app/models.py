from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

import database

assoc_characters_episodes = Table('assoc_characters_episodes', database.Base.metadata,
                                  Column('character_id', ForeignKey('characters.id'), primary_key=True),
                                  Column('episode_id', ForeignKey('episodes.id'), primary_key=True)
                                  )


class Character(database.Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(256), nullable=False)
    status = Column(String(256), nullable=True)
    species = Column(String, index=True, nullable=False)
    type = Column(String, default=False)
    gender = Column(String, index=True, nullable=False)
    episode = relationship("Episode", secondary=assoc_characters_episodes, back_populates="character")


class Episode(database.Base):
    __tablename__ = "episodes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(256), nullable=False)
    air_date = Column(String(256), index=True, nullable=False)
    episode = Column(String(256), nullable=False)
    character = relationship("Character", secondary=assoc_characters_episodes, back_populates="episode")


class Comment(database.Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    comment = Column(String(256), nullable=False)
    character_id = Column(Integer, ForeignKey('characters.id'))
    episode_id = Column(Integer, ForeignKey('episodes.id'))
