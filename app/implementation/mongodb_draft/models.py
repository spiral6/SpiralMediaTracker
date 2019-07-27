from datetime import datetime
import pymongo
from pymongo import IndexModel
from umongo import Document, fields, validate
from config import db, instance

print("Initializing models.")

#TODO: Media parent object model

@instance.register
class Anime(Document):
    name = fields.DictField(required=True)
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
    
    #TODO: controller logic will have to implement String ID to ObjectID from bson.objectid.ObjectId for queries
    id = fields.StrField() 
    #TODO: client facing JSON response in API controller will have to output characters with proper structure/dictionary
    #TODO: client facing JSON request in API controller will have to parse through characters and make separate queries for them. 
    #TODO: frontend will use the same API
    #TODO: same goes with staff, as in their pictures, names, roles
    rating = fields.FloatField()
    cover = fields.ReferenceField("Image")

    class Meta:
        collection = db.anime
        #indexes = ({"key": ["animename", "format","release_date"], "unique": True})

@instance.register
class Character(Document):
    #TODO: implement fields.ReferenceField("Media")
    #anime = fields.ListField(fields.ReferenceField("Anime"))
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
instance.db.anime.create_index([("name.english",pymongo.ASCENDING), ("format",pymongo.ASCENDING),("release_date",pymongo.ASCENDING)], unique=True, name="default")
