from models import Anime, Character
from sqlalchemy.orm import sessionmaker
from config import engine
import logging

db_log_file_name = 'sqla.log'
db_handler_log_level = logging.INFO
db_logger_log_level = logging.INFO

db_handler = logging.FileHandler(db_log_file_name)
db_handler.setLevel(db_handler_log_level)

db_logger = logging.getLogger('sqlalchemy')
db_logger.addHandler(db_handler)
db_logger.setLevel(db_logger_log_level)

# create a configured "Session" class
Session = sessionmaker(bind=engine)

# create a Session
session = Session()
# query = session.query(Anime).all()
# for anime in query:
#     for character in anime.characters:
#         print(character.name)
#         for anime in character.anime:
#             print(anime.id)

print("Next query.")

# query = session.query(Character).all()
# for character in query:
#     for anime in character.anime:
#         print(character.name +  str(anime.id))

query = session.query(Character).filter(Character.name == "Kai Shiden").all()
for character in query:
        for anime in character.anime:
                print(anime.id)