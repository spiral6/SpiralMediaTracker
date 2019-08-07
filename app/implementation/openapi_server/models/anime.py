# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util
from openapi_server.models.anime_characters import AnimeCharacters
from openapi_server.models.anime_name import AnimeName


class Anime(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, name=None, format=None, tags=None, genres=None, synopsis=None, season=None, duration=None, release_date=None, studios=None, episodes=None, source=None, characters=None, staff=None, rating=None):  # noqa: E501
        """Anime - a model defined in OpenAPI

        :param id: The id of this Anime.  # noqa: E501
        :type id: str
        :param name: The name of this Anime.  # noqa: E501
        :type name: AnimeName
        :param format: The format of this Anime.  # noqa: E501
        :type format: str
        :param tags: The tags of this Anime.  # noqa: E501
        :type tags: List[str]
        :param genres: The genres of this Anime.  # noqa: E501
        :type genres: List[str]
        :param synopsis: The synopsis of this Anime.  # noqa: E501
        :type synopsis: str
        :param season: The season of this Anime.  # noqa: E501
        :type season: str
        :param duration: The duration of this Anime.  # noqa: E501
        :type duration: int
        :param release_date: The release_date of this Anime.  # noqa: E501
        :type release_date: date
        :param studios: The studios of this Anime.  # noqa: E501
        :type studios: List[str]
        :param episodes: The episodes of this Anime.  # noqa: E501
        :type episodes: int
        :param source: The source of this Anime.  # noqa: E501
        :type source: str
        :param characters: The characters of this Anime.  # noqa: E501
        :type characters: List[AnimeCharacters]
        :param staff: The staff of this Anime.  # noqa: E501
        :type staff: List[AnimeCharacters]
        :param rating: The rating of this Anime.  # noqa: E501
        :type rating: float
        """
        self.openapi_types = {
            'id': str,
            'name': AnimeName,
            'format': str,
            'tags': List[str],
            'genres': List[str],
            'synopsis': str,
            'season': str,
            'duration': int,
            'release_date': date,
            'studios': List[str],
            'episodes': int,
            'source': str,
            'characters': List[AnimeCharacters],
            'staff': List[AnimeCharacters],
            'rating': float
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'format': 'format',
            'tags': 'tags',
            'genres': 'genres',
            'synopsis': 'synopsis',
            'season': 'season',
            'duration': 'duration',
            'release_date': 'release_date',
            'studios': 'studios',
            'episodes': 'episodes',
            'source': 'source',
            'characters': 'characters',
            'staff': 'staff',
            'rating': 'rating'
        }

        self._id = id
        self._name = name
        self._format = format
        self._tags = tags
        self._genres = genres
        self._synopsis = synopsis
        self._season = season
        self._duration = duration
        self._release_date = release_date
        self._studios = studios
        self._episodes = episodes
        self._source = source
        self._characters = characters
        self._staff = staff
        self._rating = rating

    @classmethod
    def from_dict(cls, dikt) -> 'Anime':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Anime of this Anime.  # noqa: E501
        :rtype: Anime
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this Anime.


        :return: The id of this Anime.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Anime.


        :param id: The id of this Anime.
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Anime.


        :return: The name of this Anime.
        :rtype: AnimeName
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Anime.


        :param name: The name of this Anime.
        :type name: AnimeName
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def format(self):
        """Gets the format of this Anime.

        Broadcast format of anime.  # noqa: E501

        :return: The format of this Anime.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this Anime.

        Broadcast format of anime.  # noqa: E501

        :param format: The format of this Anime.
        :type format: str
        """
        allowed_values = ["ONA", "OVA", "TV", "Movie", "Special", "Music", "TV Short"]  # noqa: E501
        if format not in allowed_values:
            raise ValueError(
                "Invalid value for `format` ({0}), must be one of {1}"
                .format(format, allowed_values)
            )

        self._format = format

    @property
    def tags(self):
        """Gets the tags of this Anime.


        :return: The tags of this Anime.
        :rtype: List[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Anime.


        :param tags: The tags of this Anime.
        :type tags: List[str]
        """

        self._tags = tags

    @property
    def genres(self):
        """Gets the genres of this Anime.


        :return: The genres of this Anime.
        :rtype: List[str]
        """
        return self._genres

    @genres.setter
    def genres(self, genres):
        """Sets the genres of this Anime.


        :param genres: The genres of this Anime.
        :type genres: List[str]
        """

        self._genres = genres

    @property
    def synopsis(self):
        """Gets the synopsis of this Anime.

        Anime synopsis.  # noqa: E501

        :return: The synopsis of this Anime.
        :rtype: str
        """
        return self._synopsis

    @synopsis.setter
    def synopsis(self, synopsis):
        """Sets the synopsis of this Anime.

        Anime synopsis.  # noqa: E501

        :param synopsis: The synopsis of this Anime.
        :type synopsis: str
        """
        if synopsis is None:
            raise ValueError("Invalid value for `synopsis`, must not be `None`")  # noqa: E501

        self._synopsis = synopsis

    @property
    def season(self):
        """Gets the season of this Anime.


        :return: The season of this Anime.
        :rtype: str
        """
        return self._season

    @season.setter
    def season(self, season):
        """Sets the season of this Anime.


        :param season: The season of this Anime.
        :type season: str
        """

        self._season = season

    @property
    def duration(self):
        """Gets the duration of this Anime.

        Duration in minutes.  # noqa: E501

        :return: The duration of this Anime.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this Anime.

        Duration in minutes.  # noqa: E501

        :param duration: The duration of this Anime.
        :type duration: int
        """

        self._duration = duration

    @property
    def release_date(self):
        """Gets the release_date of this Anime.


        :return: The release_date of this Anime.
        :rtype: date
        """
        return self._release_date

    @release_date.setter
    def release_date(self, release_date):
        """Sets the release_date of this Anime.


        :param release_date: The release_date of this Anime.
        :type release_date: date
        """

        self._release_date = release_date

    @property
    def studios(self):
        """Gets the studios of this Anime.


        :return: The studios of this Anime.
        :rtype: List[str]
        """
        return self._studios

    @studios.setter
    def studios(self, studios):
        """Sets the studios of this Anime.


        :param studios: The studios of this Anime.
        :type studios: List[str]
        """

        self._studios = studios

    @property
    def episodes(self):
        """Gets the episodes of this Anime.

        Number of episodes.  # noqa: E501

        :return: The episodes of this Anime.
        :rtype: int
        """
        return self._episodes

    @episodes.setter
    def episodes(self, episodes):
        """Sets the episodes of this Anime.

        Number of episodes.  # noqa: E501

        :param episodes: The episodes of this Anime.
        :type episodes: int
        """

        self._episodes = episodes

    @property
    def source(self):
        """Gets the source of this Anime.

        Original source of anime.  # noqa: E501

        :return: The source of this Anime.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this Anime.

        Original source of anime.  # noqa: E501

        :param source: The source of this Anime.
        :type source: str
        """
        allowed_values = ["Original", "Manga", "Light Novel", "Visual Novel", "Novel", "Video Game", "Doujinshi"]  # noqa: E501
        if source not in allowed_values:
            raise ValueError(
                "Invalid value for `source` ({0}), must be one of {1}"
                .format(source, allowed_values)
            )

        self._source = source

    @property
    def characters(self):
        """Gets the characters of this Anime.


        :return: The characters of this Anime.
        :rtype: List[AnimeCharacters]
        """
        return self._characters

    @characters.setter
    def characters(self, characters):
        """Sets the characters of this Anime.


        :param characters: The characters of this Anime.
        :type characters: List[AnimeCharacters]
        """

        self._characters = characters

    @property
    def staff(self):
        """Gets the staff of this Anime.


        :return: The staff of this Anime.
        :rtype: List[AnimeCharacters]
        """
        return self._staff

    @staff.setter
    def staff(self, staff):
        """Sets the staff of this Anime.


        :param staff: The staff of this Anime.
        :type staff: List[AnimeCharacters]
        """

        self._staff = staff

    @property
    def rating(self):
        """Gets the rating of this Anime.

        Rating out of 100.  # noqa: E501

        :return: The rating of this Anime.
        :rtype: float
        """
        return self._rating

    @rating.setter
    def rating(self, rating):
        """Sets the rating of this Anime.

        Rating out of 100.  # noqa: E501

        :param rating: The rating of this Anime.
        :type rating: float
        """

        self._rating = rating
