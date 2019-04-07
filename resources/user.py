from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help="Wrong value: username")
    parser.add_argument('password', type=str, required=True, help="Wrong value: password")
    parser.add_argument('email', type=str, required=True, help="Wrong value: email")
    @jwt_required()
    def get(self,name):
         item = UserModel.find_by_name(name)
         return {'item': item}, 200 if item else 404


    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {"message": "item '{}' already exist".format(data['username'])}, 400
        user = UserModel(**data)
        try:
            user.save_to_db()
        except:
            return {'message': 'User not created'}, 500

        return {'message': 'User created'}, 201



