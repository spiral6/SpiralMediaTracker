# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.movie import Movie  # noqa: E501
from swagger_server.test import BaseTestCase


class TestMoviesController(BaseTestCase):
    """MoviesController integration test stubs"""

    def test_add_movie(self):
        """Test case for add_movie

        Add a new movie to the database.
        """
        body = Movie()
        response = self.client.open(
            '/api/movies',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_movie(self):
        """Test case for delete_movie

        Deletes a movie.
        """
        headers = [('api_key', 'api_key_example')]
        response = self.client.open(
            '/api/movies/{name}'.format(name='name_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_movie_by_name(self):
        """Test case for get_movie_by_name

        Find movie by name.
        """
        response = self.client.open(
            '/api/movies/{name}'.format(name='name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_movies(self):
        """Test case for get_movies

        Get all movies.
        """
        response = self.client.open(
            '/api/movies',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_movie(self):
        """Test case for update_movie

        Update an movie in the database.
        """
        body = Movie()
        response = self.client.open(
            '/api/movies',
            method='PUT',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
