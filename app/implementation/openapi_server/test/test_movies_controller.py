# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from openapi_server.models.movie import Movie  # noqa: E501
from openapi_server.test import BaseTestCase


class TestMoviesController(BaseTestCase):
    """MoviesController integration test stubs"""

    def test_add_movie(self):
        """Test case for add_movie

        
        """
        movie = Movie()
        response = self.client.open(
            '/api/v1/movies',
            method='POST',
            data=json.dumps(movie),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_movie(self):
        """Test case for delete_movie

        
        """
        headers = [('api_key', 'api_key_example')]
        response = self.client.open(
            '/api/v1/movies/{ID}'.format(id=3.4),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_movie_by_name(self):
        """Test case for get_movie_by_name

        
        """
        response = self.client.open(
            '/api/v1/movies/{ID}'.format(id=3.4),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_movies(self):
        """Test case for get_movies

        
        """
        response = self.client.open(
            '/api/v1/movies',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_movie_patch(self):
        """Test case for update_movie_patch

        
        """
        movie = {"id":337}
        headers = [('api_key', 'api_key_example')]
        response = self.client.open(
            '/api/v1/movies/{ID}'.format(id=3.4),
            method='PATCH',
            data=json.dumps(movie),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_movie_put(self):
        """Test case for update_movie_put

        
        """
        movie = Movie()
        headers = [('api_key', 'api_key_example')]
        response = self.client.open(
            '/api/v1/movies/{ID}'.format(id=3.4),
            method='PUT',
            data=json.dumps(movie),
            headers=headers,
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
