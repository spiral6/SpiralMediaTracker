import connexion
import six
import json
import pymongo

from openapi_server.impl_models.anime import Anime  # noqa: E501
from openapi_server.impl_models.response import Response  # noqa: E501
from openapi_server.controllers.database import initialize_database
from openapi_server import util


def add_anime():  # noqa: E501
    """add_anime

     # noqa: E501

    :param anime: 
    :type anime: dict | bytes

    :rtype: ApiResponse
    """
    
    """
    the actual response will not be following the pre-generated model,
    but rather, something far closer to the response that seems closer to the schema
    defined inside of the openapi.yaml specification

    like so:

    response = {
        "test": "test",
        "fail": "sure",
        "and_so": [1,2,3]
    }
    """
    response = None
    if connexion.request.is_json:
        anime = Anime.create_from_dict(connexion.request.get_json())
        if(anime is None):
            #response = Response(400,"Operation failed. Unable to initialize Anime object.")
            return "Operation failed. Unable to initialize Anime object.", 400
        else:
            try:
                db = initialize_database()
            except:
                #response = Response(400, "Operation failed. Unable to connect to database.")
                return "Operation failed. Unable to connect to database.", 400
            else:
                #TODO: implement MongoDB add document
                anime_collection = db.anime
                search_dict = {"name": 
                {"preferred": anime.name["preferred"]},
                "format": anime.format,
                "release_date": anime.release_date
                }
                check_if_existing = anime_collection.find_one(search_dict)
                if(check_if_existing is None):
                    anime_dict = anime.output_dict()
                    print(anime_dict)
                    try:
                        anime_collection.insert_one(anime.__dict__)
                        return "Operation successful!", 201
                    except pymongo.errors.DuplicateKeyError:
                        return "Operation failed. Data entry already exists.", 400
                else:
                    #response = Response(400, "Operation failed. Data entry already exists. ObjectId = %s" % (check_if_existing["_id"]))
                    return "Operation failed. Data entry already exists.", 400
    else:
        return "Operation failed. Invalid JSON request.", 400


def delete_anime(id, api_key=None):  # noqa: E501
    """delete_anime

    ID of anime to delete. # noqa: E501

    :param id: ID of anime to delete.
    :type id: str
    :param api_key: 
    :type api_key: str

    :rtype: None
    """
    return 'do  magic!'


def get_anime():  # noqa: E501
    """get_anime

    Return a list of anime. # noqa: E501


    :rtype: Anime
    """
    return "yeet"
    


def get_anime_by_id(id):  # noqa: E501
    """get_anime_by_id

    Returns a single anime. # noqa: E501

    :param id: ID of anime to return.
    :type id: str

    :rtype: Anime
    """
    return 'yote!'


def update_anime_patch(id, api_key=None, anime=None):  # noqa: E501
    """update_anime_patch

    Updates a single anime. # noqa: E501

    :param id: ID of anime to update.
    :type id: str
    :param api_key: 
    :type api_key: str
    :param anime: 
    :type anime: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        anime = Anime.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do  magic!'


def update_anime_put(id, api_key=None, anime=None):  # noqa: E501
    """update_anime_put

    Updates a single anime. # noqa: E501

    :param id: ID of anime to update.
    :type id: str
    :param api_key: 
    :type api_key: str
    :param anime: 
    :type anime: dict | bytes

    :rtype: ApiResponse
    """
    if connexion.request.is_json:
        anime = Anime.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do  magic!'