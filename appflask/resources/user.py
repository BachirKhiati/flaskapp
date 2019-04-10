from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_refresh_token_required,
                                get_jwt_identity)
from flask_restful import Resource, reqparse

from appflask import bcrypt
from appflask.models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help="Wrong value: username")
    parser.add_argument('password', type=str, required=True, help="Wrong value: password")
    parser.add_argument('email', type=str, required=True, help="Wrong value: email")
    parser.add_argument('first_name', type=str, required=True, help="Wrong value: first name")
    parser.add_argument('last_name', type=str, required=True, help="Wrong value: last name")

    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.find_by_email(data['email']):
            return {"message": "User '{}' already exist".format(data['email'])}, 400

        data['password'] = bcrypt.generate_password_hash(data['password']).decode('utf-8')
        user = UserModel(**data)
        try:
            user.save_to_db()
        except:
            return {'message': 'User not ‰‰created'}, 500

        return {'message': 'User created'}, 201


class UserAuth(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('password', type=str, required=True, help="Wrong value: password")
    parser.add_argument('email', type=str, required=True, help="Wrong value: email")

    def post(self):
        data = UserAuth.parser.parse_args()
        user = UserModel.find_by_email(data['email'])
        if user:
            if user.check_password_database(user.password, data['password']):
                user = {}
                access_token = create_access_token(identity=data)
                refresh_token = create_refresh_token(identity=data)
                user['token'] = access_token
                user['refresh'] = refresh_token
                return {'ok': True, 'data': user}, 200
            else:
                return {'ok': False, 'message': 'invalid email or password'}, 401
        else:
            return {'ok': False, 'message': 'user not found'}, 401


class UserAuthTokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        ret = {
            'token': create_access_token(identity=current_user)
        }
        return {'ok': True, 'token': ret}, 200
