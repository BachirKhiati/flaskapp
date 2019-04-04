from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required, current_identity
from userSecurity import authenticate,identity
import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = "E{:#ipAF4AT2V<5'Q_*fme_ZGjJ{~,H+6WSm=Wn>=7)N15[|j-m8rm|K+xex~O+"
app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(days=1800)

api = Api(app)

jwt= JWT(app, authenticate, identity)


items=[]

class Protected(Resource):
    @jwt_required()
    def get(self):
        return '%s' % current_identity

class ItemsList(Resource):
    @jwt_required()
    def get(self):
        return {'items': items}


class Item(Resource):
    def get(self, name):
         item = next(filter( lambda x: x['name'] == name, items), None)
         return {'item': item}, 200 if item else 404


    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {"message": "item '{}' already exist".format(name)}, 400
        data= request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return {'items': items}, 201

    def put(self, name):
        return {'student': name}, 200

    def delete(self, name):
        global items
        items= list(filter(lambda x: x['name'] != name,items))
        return {'message': "deleted the item"}, 202


api.add_resource(Item,'/item/<string:name>')
api.add_resource(Protected,'/protected')
api.add_resource(ItemsList,'/items')




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)


# @app.route("/")
# def hello():
#     return "<h1 style='color:blue'>Hello There!</h1>"
#
#
# @app.route('/store', methods=['POST'])
# def createStore():
#     request_data = request.get_json()
#     new_store = {
#         'name': request_data['name'],
#         'items': []
#     }
#     stores.append(new_store)
#     return jsonify({'store':new_store})
#
#
# @app.route('/store/<string:name>/item', methods=['POST'])
# def create_item_store(name):
#     request_data = request.get_json()
#     for store in stores:
#         if  store['name']== name:
#             new_item = {
#                         'name': request_data['name'],
#                         'price': request_data['price']
#             }
#             store['items'].append(new_item)
#             return jsonify({'store':store})
#     return jsonify({'message':'store not found'})
#
#
#
# @app.route('/store/<string:name>')
# def getStore(name):
#     for store in stores:
#         if name == store['name']:
#             return jsonify(store)
#     return jsonify({'message':'store not found'})
#
#
# @app.route('/store/<string:name>/item')
# def get_item_store(name):
#     for store in stores:
#         if name == store['name']:
#             return jsonify({'items': store['items']})
#     return jsonify({'message':'item empty'})
#
#
# @app.route('/store')
# def get_store():
#     return jsonify({'stores':stores})

