'use strict';


/**
 * Add a new anime to the database.
 * 
 *
 * body Anime Anime object that needs to be added to the database.
 * no response value expected for this operation
 **/
exports.addAnime = function(body) {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}


/**
 * Deletes an anime.
 * 
 *
 * name String Name of anime to delete.
 * api_key String  (optional)
 * no response value expected for this operation
 **/
exports.deleteAnime = function(name,api_key) {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}


/**
 * Get all anime.
 * Return all anime.
 *
 * no response value expected for this operation
 **/
exports.getAnime = function() {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}


/**
 * Find anime by name.
 * Returns a single anime.
 *
 * name String Name of anime to return.
 * returns Anime
 **/
exports.getAnimeByName = function(name) {
  return new Promise(function(resolve, reject) {
    var examples = {};
    examples['application/json'] = {
  "studios" : [ "studios", "studios" ],
  "format" : "ONA",
  "rating" : 1.4658129,
  "synopsis" : "synopsis",
  "source" : "Original",
  "tags" : [ "tags", "tags" ],
  "duration" : 0,
  "characters" : [ {
    "actor" : "actor",
    "name" : "name",
    "picture" : "picture",
    "actor_picture" : "actor_picture"
  }, {
    "actor" : "actor",
    "name" : "name",
    "picture" : "picture",
    "actor_picture" : "actor_picture"
  } ],
  "release_date" : "2000-01-23",
  "genres" : [ "genres", "genres" ],
  "name" : {
    "romanji" : "Hagane no Renkinjutsushi: Fullmetal Alchemist",
    "native" : "鋼の錬金術師 FULLMETAL ALCHEMIST",
    "english" : "Fullmetal Alchemist: Brotherhood"
  },
  "season" : "season",
  "episodes" : 6
};
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}


/**
 * Update an anime in the database.
 * 
 *
 * body Anime Anime object that needs to be added to the database.
 * no response value expected for this operation
 **/
exports.updateAnime = function(body) {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}

