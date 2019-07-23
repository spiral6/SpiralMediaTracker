from datetime import datetime

from pymongo import MongoClient

from umongo import Instance, Document, fields, validate



db = MongoClient('SQLContainer', 27017)

instance = Instance(db.db1)



@instance.register

class User(Document):

    email = fields.EmailField(required=True, unique=True)

    birthday = fields.DateTimeField(validate=validate.Range(min=datetime(1900, 1, 1)))

    friends = fields.ListField(fields.ReferenceField("User"))



    class Meta:

        collection = db.user



# Make sure that unique indexes are created

User.ensure_indexes()



goku = User(email='goku@sayen.com', birthday=datetime(1984, 11, 20))

goku.commit()

vegeta = User(email='vegeta@over9000.com', friends=[goku])

vegeta.commit()