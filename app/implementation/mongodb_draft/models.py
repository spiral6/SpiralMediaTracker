from datetime import datetime
import pymongo
from pymongo import IndexModel
from umongo import Document, fields, validate
from config import db, instance

print("Initializing models.")

@instance.register
class User(Document):
    email = fields.EmailField(required=True, unique=True)
    birthday = fields.DateTimeField(validate=validate.Range(min=datetime(1900, 1, 1)))
    friends = fields.ListField(fields.ReferenceField("User"))

    class Meta:
        collection = db.user

@instance.register
class Anime(Document):
    animename = fields.DictField(required=True)
    format = fields.StrField(validate=validate.OneOf(["ONA","OVA","TV","Movie","Special","Music","TV Short"]))
    tags =  fields.ListField(fields.StrField()) #array
    genres = fields.ListField(fields.StrField()) #array
    synopsis = fields.StrField()
    season = fields.StrField()
    duration = fields.IntField()
    release_date = fields.StrField()
    studios = fields.ListField(fields.StrField()) #array
    episodes = fields.IntField()
    source = fields.StrField(validate=validate.OneOf(["Original","Manga","Light Novel","Visual Novel","Novel","Video Game","Doujinshi"]))
    #characters = fields.ListField(fields.ReferenceField("Character"))
    rating = fields.FloatField()
    cover = fields.ReferenceField("Image")

    class Meta:
        collection = db.anime
        #indexes = ({"key": ["animename", "format","release_date"], "unique": True})

@instance.register
class Character(Document):
    anime = fields.ListField(fields.ReferenceField("Anime"))
    name = fields.StrField(required=True)
    actor = fields.StrField()
    picture = fields.ReferenceField("Image")
    actor_picture = fields.ReferenceField("Image")

    class Meta:
        collection = db.character

@instance.register
class Image(Document):
    type = fields.StrField(required=True, validate=validate.OneOf(["character_image","actor_image"]))
    character = fields.ReferenceField("Character")

    class Meta:
        collection = db.image

#Indexing is very broken in the umongo library.
instance.db.anime.create_index([("animename.english",pymongo.ASCENDING), ("format",pymongo.ASCENDING),("release_date",pymongo.ASCENDING)], unique=True)

# # Make sure that unique indexes are created
# User.ensure_indexes()

# goku = User(email='goku@sayen.com', birthday=datetime(1984, 11, 20))
# goku.commit()

# vegeta = User(email='vegeta@over9000.com', friends=[goku])
# vegeta.commit()