import datetime
import json
from uuid import UUID

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_restful import Api


class JSONEncoder(json.JSONEncoder):
    ''' extend json-encoder class'''

    def default(self, o):
        if isinstance(o, UUID):
            return str(o)
        # if isinstance(o, ObjectId):
        #     return str(o)
        if isinstance(o, set):
            return list(o)
        if isinstance(o, datetime.datetime):
            return str(o)
        return json.JSONEncoder.default(self, o)


# create the flask object
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config['SECRET_KEY'] = "E{:#ipAF4AT2V<5'Q_*fme_ZGjJ{~,H+6WSm=Wn>=7)N15[|j-m8rm|K+xex~O+"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://app:Qaz123Wsx456Edc789@127.0.0.1:5432/app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(days=31)
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = datetime.timedelta(days=31)
jwt = JWTManager(app)
app.json_encoder = JSONEncoder
api = Api(app)

from appflask.resources.item import Item, ItemsList
from appflask.resources.store import Store, StoreList
from appflask.resources.user import UserRegister, UserAuth, UserAuthTokenRefresh

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(ItemsList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')
api.add_resource(UserAuth, '/auth')
api.add_resource(UserAuthTokenRefresh, '/refresh')


@jwt.unauthorized_loader
def unauthorized_response(callback):
    return {
               'ok': False,
               'message': 'Missing Authorization Header'
           }, 401
