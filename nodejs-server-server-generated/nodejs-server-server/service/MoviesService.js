'use strict';


/**
 * Add a new movie to the database.
 * 
 *
 * body Movie Movie object that needs to be added to the database.
 * no response value expected for this operation
 **/
exports.addMovie = function(body) {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}


/**
 * Deletes a movie.
 * 
 *
 * name String Name of movie to delete.
 * api_key String  (optional)
 * no response value expected for this operation
 **/
exports.deleteMovie = function(name,api_key) {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}


/**
 * Find movie by name.
 * Returns a single movie.
 *
 * name String Name of movie to return.
 * returns Movie
 **/
exports.getMovieByName = function(name) {
  return new Promise(function(resolve, reject) {
    var examples = {};
    examples['application/json'] = {
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
  "directors" : [ "directors", "directors" ],
  "name" : "The Godfather",
  "rating" : 6.0274563,
  "synopsis" : "synopsis",
  "writers" : [ "writers", "writers" ],
  "tags" : [ "tags", "tags" ]
};
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}


/**
 * Get all movies.
 * Return all movies.
 *
 * no response value expected for this operation
 **/
exports.getMovies = function() {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}


/**
 * Update an movie in the database.
 * 
 *
 * body Movie Movie object that needs to be added to the database.
 * no response value expected for this operation
 **/
exports.updateMovie = function(body) {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}

