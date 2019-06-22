'use strict';

var utils = require('../utils/writer.js');
var Movies = require('../service/MoviesService');

module.exports.add_movie = function add_movie (req, res, next) {
  var body = req.swagger.params['body'].value;
  Movies.add_movie(body)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.delete_movie = function delete_movie (req, res, next) {
  var iD = req.swagger.params['ID'].value;
  var api_key = req.swagger.params['api_key'].value;
  Movies.delete_movie(iD,api_key)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.get_movie_by_name = function get_movie_by_name (req, res, next) {
  var iD = req.swagger.params['ID'].value;
  Movies.get_movie_by_name(iD)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.get_movies = function get_movies (req, res, next) {
  Movies.get_movies()
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.update_movie = function update_movie (req, res, next) {
  var body = req.swagger.params['body'].value;
  Movies.update_movie(body)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};
