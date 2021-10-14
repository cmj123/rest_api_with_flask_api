# Import required libraries, class
from flask import Flask, jsonify, render_template, request

#Initialise a new flask application
app = Flask(__name__)

stores = [
    {
        'name':'My Wonderful Store',
        'items': [
            {
                'name':'My Item',
                'price':15.99
            }
        ]
    }
]

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# Reference - wen server
# POST - used to receive data
@app.route('/store' , methods=['POST'])
def create_store():
  request_data = request.get_json()
  new_store = {
    'name':request_data['name'],
    'items':[]
  }
  stores.append(new_store)
  return jsonify(new_store)

# GET - used to send data back only
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message':'store not found'})

# GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores':stores})


# POST /store/<string:name>/item {name:. price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()

    for store in stores:
        if store['name'] == name:
            new_item = {
                'name':request_data['name'],
                'price':request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'Message':'Store not found'})

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'item':store['items']})
    return jsonify({'message':'store not found'})

# Run the app
app.run(port=5000, debug=True)
