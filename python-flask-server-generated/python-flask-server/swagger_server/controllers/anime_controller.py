import connexion
import six

from swagger_server.models.anime import Anime  # noqa: E501
from swagger_server import util


def add_anime(body):  # noqa: E501
    """Add a new anime to the database.

     # noqa: E501

    :param body: Anime object that needs to be added to the database.
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Anime.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_anime(name, api_key=None):  # noqa: E501
    """Deletes an anime.

     # noqa: E501

    :param name: Name of anime to delete.
    :type name: str
    :param api_key: 
    :type api_key: str

    :rtype: None
    """
    return 'do some magic!'


def get_anime():  # noqa: E501
    """Get all anime.

    Return all anime. # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def get_anime_by_name(name):  # noqa: E501
    """Find anime by name.

    Returns a single anime. # noqa: E501

    :param name: Name of anime to return.
    :type name: str

    :rtype: Anime
    """
    return 'do some magic!'


def update_anime(body):  # noqa: E501
    """Update an anime in the database.

     # noqa: E501

    :param body: Anime object that needs to be added to the database.
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Anime.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
