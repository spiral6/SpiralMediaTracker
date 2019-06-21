# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.anime import Anime  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAnimeController(BaseTestCase):
    """AnimeController integration test stubs"""

    def test_add_anime(self):
        """Test case for add_anime

        Add a new anime to the database.
        """
        body = Anime()
        response = self.client.open(
            '/api/anime',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_anime(self):
        """Test case for delete_anime

        Deletes an anime.
        """
        headers = [('api_key', 'api_key_example')]
        response = self.client.open(
            '/api/anime/{name}'.format(name='name_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_anime(self):
        """Test case for get_anime

        Get all anime.
        """
        response = self.client.open(
            '/api/anime',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_anime_by_name(self):
        """Test case for get_anime_by_name

        Find anime by name.
        """
        response = self.client.open(
            '/api/anime/{name}'.format(name='name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_anime(self):
        """Test case for update_anime

        Update an anime in the database.
        """
        body = Anime()
        response = self.client.open(
            '/api/anime',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
