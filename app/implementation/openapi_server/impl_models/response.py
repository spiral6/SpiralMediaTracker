import flask

class Response():
    def __init__(
        self, 
        code=None, 
        message=None, 
        data=None):

        self._code = code
        self._message = message
        self._data = data

    #creates a dictionary object that outputs JSON with the appropriate HTTP code, message and data for the HTTP body
    def output(self):
        if(self._data is None):
            response_dict = {
                "code": self._code,
                "message": self._message,
            }
        else:
            response_dict = {
                "code": self._code,
                "message": self._message,
                "data": self._data
            }
        return response_dict

    #TODO: ensure response dictionary object is created correctly and converted to JSON response 