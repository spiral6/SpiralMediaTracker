import os
from models import Anime, Character, Image
from example_data import ANIME_EXAMPLE_DATA, CHARACTER_EXAMPLE_DATA
from pymongo.errors import DuplicateKeyError

# Iterate over the PEOPLE structure and populate the database
for ANIME_EXAMPLE in ANIME_EXAMPLE_DATA:
    anime_name = {
        "english":ANIME_EXAMPLE["name"]["english"],
        "romaji":ANIME_EXAMPLE["name"]["romaji"],
        "native":ANIME_EXAMPLE["name"]["native"],
        "preferred":"",
        "synonyms":[""],
    }

    anime = Anime(
        #id=ANIME_EXAMPLE["id"],
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
        source=ANIME_EXAMPLE["source"],
        rating=ANIME_EXAMPLE["rating"],  
    )

    #debug_dump = anime.dump()
    try:
        anime.commit()
    except DuplicateKeyError as e:
        print("Record already exists.")
        print(e)
        pass

for CHARACTER_EXAMPLE in CHARACTER_EXAMPLE_DATA:
    character_document = Character(
        name=CHARACTER_EXAMPLE["name"],
        actor="",
        #picture="",
        #actor_picture=""
    )
    character_document.commit()