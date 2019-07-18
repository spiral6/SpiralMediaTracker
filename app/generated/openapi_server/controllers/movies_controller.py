import connexion
import six

from openapi_server.models.movie import Movie  # noqa: E501
from openapi_server import util


def add_movie(movie):  # noqa: E501
    """add_movie

     # noqa: E501

    :param movie: 
    :type movie: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        movie = Movie.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_movie(id, api_key=None):  # noqa: E501
    """delete_movie

    Deletes a single movie. # noqa: E501

    :param id: ID of movie to delete.
    :type id: float
    :param api_key: 
    :type api_key: str

    :rtype: None
    """
    return 'do some magic!'


def get_movie_by_name(id):  # noqa: E501
    """get_movie_by_name

    Returns a single movie. # noqa: E501

    :param id: ID of movie to return.
    :type id: float

    :rtype: Movie
    """
    return 'do some magic!'


def get_movies():  # noqa: E501
    """get_movies

    Return all movies. # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def update_movie_patch(id, movie, api_key=None):  # noqa: E501
    """update_movie_patch

    Updates a single movie. # noqa: E501

    :param id: ID of movie to update.
    :type id: float
    :param movie: 
    :type movie: dict | bytes
    :param api_key: 
    :type api_key: str

    :rtype: None
    """
    if connexion.request.is_json:
        movie = Movie.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_movie_put(id, movie, api_key=None):  # noqa: E501
    """update_movie_put

    Updates a single movie. # noqa: E501

    :param id: ID of movie to update.
    :type id: float
    :param movie: 
    :type movie: dict | bytes
    :param api_key: 
    :type api_key: str

    :rtype: None
    """
    if connexion.request.is_json:
        movie = Movie.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
