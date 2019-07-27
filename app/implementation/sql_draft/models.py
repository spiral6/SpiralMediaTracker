from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.types import Float, Unicode
from sqlalchemy.orm import relationship


Base = declarative_base()

class Anime(Base):
    __tablename__ = 'anime'

    id = Column('id', Integer, primary_key=True)
    animename = relationship("AnimeName", back_populates="anime",uselist=False)
    format = Column(String)
    tags = Column(String) #array
    genres = Column(String) #array
    synopsis = Column(String)
    season = Column(String)
    duration = Column(Integer)
    release_date = Column(String)
    studios = Column(String) #array
    episodes = Column(Integer)
    source = Column(String)
    characters = relationship("Character", secondary="character_animes", back_populates="anime")
    rating = Column(Float)


class AnimeName(Base):
    __tablename__ = 'animenames'

    id = Column(Integer, primary_key=True)
    anime_id = Column(Integer, ForeignKey("anime.id"))
    anime = relationship("Anime", back_populates="animename",uselist=False)
    English = Column(String)
    Romaji = Column(String)
    Native =  Column(Unicode)

class Character(Base):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True)

    anime = relationship("Anime", secondary="character_animes", back_populates="characters")
    name = Column(String)
    actor = Column(String)
    picture = Column(String)
    actor_picture = Column(String)

class Character_Anime_Association(Base):
    __tablename__ = 'character_animes'

    id = Column(Integer, primary_key=True)
    anime_id = Column(Integer, ForeignKey("anime.id"))
    character_id = Column(Integer, ForeignKey("characters.id"))