# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from openapi_server.models.anime import Anime  # noqa: E501
from openapi_server.test import BaseTestCase


class TestAnimeController(BaseTestCase):
    """AnimeController integration test stubs"""

    def test_add_anime(self):
        """Test case for add_anime

        
        """
        anime = Anime()
        response = self.client.open(
            '/api/v1/anime',
            method='POST',
            data=json.dumps(anime),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_anime(self):
        """Test case for delete_anime

        
        """
        headers = [('api_key', 'api_key_example')]
        response = self.client.open(
            '/api/v1/anime/{ID}'.format(id=3.4),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_anime(self):
        """Test case for get_anime

        
        """
        response = self.client.open(
            '/api/v1/anime',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_anime_by_id(self):
        """Test case for get_anime_by_id

        
        """
        response = self.client.open(
            '/api/v1/anime/{ID}'.format(id=3.4),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_anime_patch(self):
        """Test case for update_anime_patch

        
        """
        anime = {"id":337}
        headers = [('api_key', 'api_key_example')]
        response = self.client.open(
            '/api/v1/anime/{ID}'.format(id=3.4),
            method='PATCH',
            data=json.dumps(anime),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_anime_put(self):
        """Test case for update_anime_put

        
        """
        anime = Anime()
        headers = [('api_key', 'api_key_example')]
        response = self.client.open(
            '/api/v1/anime/{ID}'.format(id=3.4),
            method='PUT',
            data=json.dumps(anime),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
