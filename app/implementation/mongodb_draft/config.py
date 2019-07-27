from pymongo import MongoClient
from umongo import Instance

db = MongoClient('SQLContainer', 27017) #connection initialization
instance = Instance(db.test) #database initialization