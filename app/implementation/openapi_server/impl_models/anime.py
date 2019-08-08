import json

class Anime():
    """NOTE: This class represents the Anime object schema in the created OpenAPI specification.
    """
    #TODO: ensure models are not generated once these models are implemented

    def __init__(
        self, 
        name={"english":None, "romaji": None, "native": None, "preferred": None, "synonyms":[]},
        format=None, 
        tags=None, 
        genres=None, 
        synopsis=None, 
        season=None, 
        duration=None, 
        release_date=None, 
        studios=None, 
        episodes=None, 
        source=None, 
        characters=None, 
        staff=None, 
        rating=None):

        self.name = name
        self.format = format
        self.tags = tags
        self.genres = genres
        self.synopsis = synopsis
        self.season = season
        self.duration = duration
        self.release_date = release_date
        self.studios = studios
        self.episodes = episodes
        self.source = source
        self.characters = characters
        self.staff = staff
        self.rating = rating

    #ideally, creates an Anime object that can be output into a dictionary for MongoDB
    def create_from_dict(dict):
        
        try:
            if (Anime.validate_anime(dict) is True):
                anime = Anime()
                for k, v in dict.items():
                    setattr(anime, k, v)
            else:
                anime = None
        except KeyError:
            raise AnimeValidationError("Invalid data members.")
            anime = None
        return anime
    
    def create_partial_from_dict(self,dict):
        anime = Anime()
        try:
            if(self.validate_anime_id(dict) is True):
                for k, v in dict.items():
                    setattr(anime, k, v)
        except:
            anime = None
        return anime
    
    def validate_anime(dict):
        #TODO: check to see if these properties exist and are valid before creating, return error otherwise

        try:        
            dict["name"]["preferred"] 
            dict["release_date"] 
            dict["format"]
        except:
            #TODO: Create localized strings for error messages?
            raise AnimeValidationError("Invalid data members, check values of release_date, format and name: preferred.")
            return False
        else:
            return True
    
    def validate_anime_id(dict):
        try:        
            dict["id"]
        except:
            return False
        else:
            return True

    #TODO: make this functional?
    def output_json(self):
        output = json.dumps(self)
        return output

    def output_dict(self):
        anime_dict = self.__dict__
        anime_dict["name"]["native"] = anime_dict["name"]["native"].encode('utf-8')
        return anime_dict

class Error(Exception):
   """Base class for other exceptions"""
   pass

class AnimeValidationError(Error):
    """Exception raised for errors in the input.
    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """
    def __init__(self, message):
        #self.expression = expression
        self.message = message