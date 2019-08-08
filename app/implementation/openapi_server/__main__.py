#!/usr/bin/env python3

import connexion

from openapi_server import encoder

# from connexion.decorators.validation import RequestBodyValidator
# from connexion.problem import problem
# from connexion.utils import is_null
# from jsonschema.validators import validator_for

# class CustomRequestBodyValidator(RequestBodyValidator):
#     def validate_schema(self, data):
#         if self.is_null_value_valid and is_null(data):
#             return None

#         cls = validator_for(self.schema)
#         cls.check_schema(self.schema)
#         errors = tuple(cls(self.schema).iter_errors(data))

#         if errors:
#             error_list = [ e.message for e in errors ]
#             return problem(400, 'Bad Request', {'errors': error_list}, type='validation')

#         return None


# validator_map = {
#     'body': CustomRequestBodyValidator,
# }

def main():
    app = connexion.App(__name__, specification_dir='./openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml', arguments={'title': 'Spiral Media Tracker'})
    app.run(port=8080, debug=True)


if __name__ == '__main__':
    main()

