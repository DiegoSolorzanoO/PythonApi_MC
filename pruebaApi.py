from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

public_key = []

warehouse = {
    'Torch' : 'Creates Fire',
    'Knife' : 'Pointy',
    'Rock' : 'Useless Rock',
    'Paper' : 'You can write things here'
}

@app.route('/sendKey', methods=['POST'])
def assignPublic():
    new_key = request.get_json()
    for key in new_key:
        public_key = new_key[key]
    return jsonify({'New Public Key' : new_key[key]})

@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({'message' : 'Hello, World!'})

@app.route('/warehouse', methods=['GET'])
def returnAll():
    return jsonify(warehouse)

@app.route('/warehouse/<string:name>', methods=['GET'])
def returnOne(name):
    return jsonify(warehouse[name])

@app.route('/warehouse', methods=['POST'])
def addOne():
    new_item = request.get_json()
    for key in new_item:
        warehouse[key]=new_item[key]
    return jsonify(warehouse)

@app.route('/quarks/<string:name>', methods=['PUT'])
def editOne(name):
    new_quark = request.get_json()
    for i,q in enumerate(warehouse):
      if q['name'] == name:
        quarks[i] = new_quark    
    qs = request.get_json()
    return jsonify({'quarks' : warehouse})

@app.route('/quarks/<string:name>', methods=['DELETE'])
def deleteOne(name):
    for i,q in enumerate(warehouse):
      if q['name'] == name:
        del warehouse[i]  
    return jsonify({'quarks' : warehouse})

if __name__ == "__main__":
    app.run(debug=True)