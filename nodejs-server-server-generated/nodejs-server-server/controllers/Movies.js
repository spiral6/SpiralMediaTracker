'use strict';

var utils = require('../utils/writer.js');
var Movies = require('../service/MoviesService');

module.exports.addMovie = function addMovie (req, res, next) {
  var body = req.swagger.params['body'].value;
  Movies.addMovie(body)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.deleteMovie = function deleteMovie (req, res, next) {
  var name = req.swagger.params['name'].value;
  var api_key = req.swagger.params['api_key'].value;
  Movies.deleteMovie(name,api_key)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.getMovieByName = function getMovieByName (req, res, next) {
  var name = req.swagger.params['name'].value;
  Movies.getMovieByName(name)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.getMovies = function getMovies (req, res, next) {
  Movies.getMovies()
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.updateMovie = function updateMovie (req, res, next) {
  var body = req.swagger.params['body'].value;
  Movies.updateMovie(body)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};
