from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [{
    'name': 'dell',
    'item': [{
        'name': 'My item',
        'price': 15.99
    }]
}]


@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"


@app.route('/store', methods=['POST'])
def createStore():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'item': []
    }
    stores.append(new_store)
    return jsonify({'store':new_store})


@app.route('/store/item', methods=['POST'])
def create_item_store():
    request_data = request.get_json()
    new_item = {
        'item': [
            {
                'name': 'Book 1',
                'price': 14.99
            }
        ]
    }
    stores[request_data['name']].append(new_item)
    return jsonify(stores[request_data['name']])


@app.route('/store/<string:name>')
def getStore(name):
    for store in stores:
        if name == store['name']:
            return jsonify(store)
    return jsonify({'message':'store not found'})


@app.route('/store/<string:name>/item')
def get_item_store(name):
    for store in stores:
        if name == store['name']:
            return jsonify({'items': store['item']})
    return jsonify({'message':'item empty'})





if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
