import os
#from config import db
from models import Anime, AnimeName, Base, Character
from config import engine
from example_data import ANIME_EXAMPLE_DATA
from sqlalchemy.orm import sessionmaker

# create a configured "Session" class
Session = sessionmaker(bind=engine)

# create a Session
session = Session()

# Create the database
Base.metadata.create_all(engine)

# Iterate over the PEOPLE structure and populate the database
for ANIME_EXAMPLE in ANIME_EXAMPLE_DATA:
    anime_name = AnimeName(English=ANIME_EXAMPLE["name"]["english"],
                            Romaji=ANIME_EXAMPLE["name"]["romaji"],
                            Native=ANIME_EXAMPLE["name"]["native"])
    characters = []
    for character in ANIME_EXAMPLE["characters"]:
        characters.append(Character(name=character["name"],
                                    actor="",
                                    picture="",
                                    actor_picture=""))
    p = Anime(
        id=ANIME_EXAMPLE["id"],
        animename=anime_name,
        format=ANIME_EXAMPLE["format"],
        tags=ANIME_EXAMPLE["tags"],
        genres=ANIME_EXAMPLE["genres"],
        synopsis=ANIME_EXAMPLE["synopsis"],
        season=ANIME_EXAMPLE["season"],
        duration=ANIME_EXAMPLE["duration"],
        release_date=ANIME_EXAMPLE["release_date"],
        studios=ANIME_EXAMPLE["studios"],
        episodes=ANIME_EXAMPLE["episodes"],
        characters=characters,
        rating=ANIME_EXAMPLE["rating"],
        source=ANIME_EXAMPLE["source"]
    )
    session.add(p)

session.commit()