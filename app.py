from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required, current_identity
from security import authenticate,identity
import datetime
from resources.item import Item,ItemsList
from resources.user import UserRegister
from resources.store import Store, StoreList


app = Flask(__name__)
app.config['SECRET_KEY'] = "E{:#ipAF4AT2V<5'Q_*fme_ZGjJ{~,H+6WSm=Wn>=7)N15[|j-m8rm|K+xex~O+"
app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://vagrant:vagrant@192.168.1.19:5432/flaskapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(days=1800)

api = Api(app)


@app.before_first_request
def create_tables():
    db.create_all()



jwt= JWT(app, authenticate, identity)


api.add_resource(Item,'/item/<string:name>')
api.add_resource(Store,'/store/<string:name>')
api.add_resource(UserRegister,'/register')
api.add_resource(ItemsList,'/items')
api.add_resource(StoreList,'/stores')


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(debug=True, host='0.0.0.0', port=80)

