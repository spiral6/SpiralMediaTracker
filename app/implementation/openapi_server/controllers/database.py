from pymongo import MongoClient
import yaml
import os.path

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "..\\..\\config.yaml")

#db = MongoClient()

def initialize_database():
    try:
        # if(os.path.exists(path)):
        #     print("YES I AM")
        # else:
        #     print(False)
        f = open(path)
    except IOError:
        print("Error: could not open config.yaml.")
    else:
        with open(path, 'r') as ymlfile:
            config = yaml.load(ymlfile)

        if(config["mongodb_auth"] == "false"):        
            connection_uri = "mongodb://%s:%s" % (config["mongodb_host"], config["mongodb_port"])
        else:
            connection_uri = "mongodb://%s:%s@%s:%s" % (config["mongodb_user"], config["mongodb_password"],config["mongodb_host"], config["mongodb_port"])
        client = MongoClient(connection_uri) #connection initialization
        db = client[config["mongodb_database"]]
        return db

def initialize_anime_index():
    db.anime.create_index([("name.preferred",pymongo.ASCENDING), ("format",pymongo.ASCENDING),("release_date",pymongo.ASCENDING)], unique=True, name="default")

def close_database():
    db.close()