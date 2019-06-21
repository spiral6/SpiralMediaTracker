import connexion
import six

from swagger_server.models.movie import Movie  # noqa: E501
from swagger_server import util


def add_movie(body):  # noqa: E501
    """Add a new movie to the database.

     # noqa: E501

    :param body: Movie object that needs to be added to the database.
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Movie.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_movie(name, api_key=None):  # noqa: E501
    """Deletes a movie.

     # noqa: E501

    :param name: Name of movie to delete.
    :type name: str
    :param api_key: 
    :type api_key: str

    :rtype: None
    """
    return 'do some magic!'


def get_movie_by_name(name):  # noqa: E501
    """Find movie by name.

    Returns a single movie. # noqa: E501

    :param name: Name of movie to return.
    :type name: str

    :rtype: Movie
    """
    return 'do some magic!'


def get_movies():  # noqa: E501
    """Get all movies.

    Return all movies. # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def update_movie(body):  # noqa: E501
    """Update an movie in the database.

     # noqa: E501

    :param body: Movie object that needs to be added to the database.
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Movie.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
