from flask_restful import Resource, reqparse

from appflask.models.item import ItemModel


class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help="Wrong value: price")
    parser.add_argument('picture_uri', type=str, required=True, help="Wrong value: picture_uri")
    parser.add_argument('store_id', type=int, required=True, help="Wrong value: store_id")
    def get(self,name):
         item = ItemModel.find_by_name(name)
         return {'item': item}, 200 if item else 404


    def post(self,name):

        if ItemModel.find_by_name(name):
            return {"message": "item '{}' already exist".format(name)}, 400

        data = Item.parser.parse_args()
        item = ItemModel(name, **data)
        try:
            item.save_to_db()
        except:
            return {'message': 'An Error occurred wheninserting the item'}, 500

        return item.json(), 201

    def put(self,name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)

        if item is None:
            item = ItemModel(name, **data)
        else:
            item.price = data['price']

        try:
            item.save_to_db()
        except:
            return {'message': 'An Error occurred wheninserting the item'}, 500

        return item.json(), 200

    def delete(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        return {'message': "deleted the item"}, 202



class ItemsList(Resource):
    def get(self):
         return {'items': [item.json() for item in ItemModel.query.all()]}, 200
