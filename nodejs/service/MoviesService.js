'use strict';


/**
 *
 * body Movie 
 * no response value expected for this operation
 **/
exports.add_movie = function(body) {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}


/**
 * Deletes a single movie.
 *
 * iD BigDecimal ID of movie to delete.
 * api_key String  (optional)
 * no response value expected for this operation
 **/
exports.delete_movie = function(iD,api_key) {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}


/**
 * Returns a single movie.
 *
 * iD BigDecimal ID of movie to return.
 * returns Movie
 **/
exports.get_movie_by_name = function(iD) {
  return new Promise(function(resolve, reject) {
    var examples = {};
    if (Object.keys(examples).length > 0) {
      resolve(examples[Object.keys(examples)[0]]);
    } else {
      resolve();
    }
  });
}


/**
 * Return all movies.
 *
 * no response value expected for this operation
 **/
exports.get_movies = function() {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}


/**
 *
 * body Movie 
 * no response value expected for this operation
 **/
exports.update_movie = function(body) {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}

