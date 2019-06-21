'use strict';

var utils = require('../utils/writer.js');
var Anime = require('../service/AnimeService');

module.exports.addAnime = function addAnime (req, res, next) {
  var body = req.swagger.params['body'].value;
  Anime.addAnime(body)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.deleteAnime = function deleteAnime (req, res, next) {
  var name = req.swagger.params['name'].value;
  var api_key = req.swagger.params['api_key'].value;
  Anime.deleteAnime(name,api_key)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.getAnime = function getAnime (req, res, next) {
  Anime.getAnime()
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.getAnimeByName = function getAnimeByName (req, res, next) {
  var name = req.swagger.params['name'].value;
  Anime.getAnimeByName(name)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.updateAnime = function updateAnime (req, res, next) {
  var body = req.swagger.params['body'].value;
  Anime.updateAnime(body)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};
