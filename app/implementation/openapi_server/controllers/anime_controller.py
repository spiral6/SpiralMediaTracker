import connexion
import six

from openapi_server.models.anime import Anime  # noqa: E501
from openapi_server.models.api_response import ApiResponse  # noqa: E501
from openapi_server import util


def add_anime(anime):  # noqa: E501
    """add_anime

     # noqa: E501

    :param anime: 
    :type anime: dict | bytes

    :rtype: ApiResponse
    """
    if connexion.request.is_json:
        anime = Anime.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_anime(id, api_key=None):  # noqa: E501
    """delete_anime

    ID of anime to delete. # noqa: E501

    :param id: ID of anime to delete.
    :type id: str
    :param api_key: 
    :type api_key: str

    :rtype: None
    """
    return 'do some magic!'


def get_anime():  # noqa: E501
    """get_anime

    Return a list of anime. # noqa: E501


    :rtype: Anime
    """
    response = ApiResponse(200, "Operation successful!")
    
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
    
    return response


def get_anime_by_id(id):  # noqa: E501
    """get_anime_by_id

    Returns a single anime. # noqa: E501

    :param id: ID of anime to return.
    :type id: str

    :rtype: Anime
    """
    return 'do some magic!'


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
    return 'do some magic!'


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
    return 'do some magic!'
