'use strict';

var utils = require('../utils/writer.js');
var Anime = require('../service/AnimeService');

module.exports.add_anime = function add_anime (req, res, next) {
  var body = req.swagger.params['body'].value;
  Anime.add_anime(body)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.delete_anime = function delete_anime (req, res, next) {
  var iD = req.swagger.params['ID'].value;
  var api_key = req.swagger.params['api_key'].value;
  Anime.delete_anime(iD,api_key)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.get_anime = function get_anime (req, res, next) {
  Anime.get_anime()
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.get_anime_by_id = function get_anime_by_id (req, res, next) {
  var iD = req.swagger.params['ID'].value;
  Anime.get_anime_by_id(iD)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.update_anime = function update_anime (req, res, next) {
  var body = req.swagger.params['body'].value;
  Anime.update_anime(body)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};
