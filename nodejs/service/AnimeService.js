'use strict';


/**
 *
 * body Anime 
 * no response value expected for this operation
 **/
exports.add_anime = function(body) {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}


/**
 * ID of anime to delete.
 *
 * iD BigDecimal ID of anime to delete.
 * api_key String  (optional)
 * no response value expected for this operation
 **/
exports.delete_anime = function(iD,api_key) {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}


/**
 * Return all anime.
 *
 * no response value expected for this operation
 **/
exports.get_anime = function() {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}


/**
 * Returns a single anime.
 *
 * iD BigDecimal ID of anime to return.
 * returns Anime
 **/
exports.get_anime_by_id = function(iD) {
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
 *
 * body Anime 
 * no response value expected for this operation
 **/
exports.update_anime = function(body) {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}

