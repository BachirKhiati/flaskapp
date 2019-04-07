from flask_restful import Resource, reqparse
from flask_jwt import JWT, jwt_required
from models.store import StoreModel


class Store(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=float, required=True, help="Wrong value: name")

    @jwt_required()
    def get(self,name):
         store = StoreModel.find_by_name(name)
         return store.json(), 200 if store else 404


    def post(self,name):
        if StoreModel.find_by_name(name):
            return {"message": "item '{}' already exist".format(name)}, 400
        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message': 'An Error occurred wheninserting the item'}, 500

        return store.json(), 201


    def delete(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        return {'message': "deleted the item"}, 202


class StoreList(Resource):
    @jwt_required()
    def get(self):
        return {'store_items': list(map(lambda x: x.json(), StoreModel.query.all()))}


