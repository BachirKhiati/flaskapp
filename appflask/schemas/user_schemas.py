from jsonschema import validate
from jsonschema.exceptions import SchemaError
from jsonschema.exceptions import ValidationError

user_schema = {
    "type": "object",
    "properties": {
        "first_name": {
            "type": "string",
            "maxLength": 50
        },
        "last_name": {
            "type": "string",
            "maxLength": 50
        },
        "email": {
            "type": "string",
            "format": "email",
            "maxLength": 50
        },
        "password": {
            "type": "string",
            "minLength": 5,
            "maxLength": 40
        }
    },
    "required": ["email", "password"],
    "additionalProperties": False
}


def validate_user(data):
    try:
        validate(data, user_schema)
    except ValidationError as e:
        return {'ok': False, 'message': e}
    except SchemaError as e:
        return {'ok': False, 'message': e}
    return {'ok': True, 'data': data}
