from flask import Flask
from flask import jsonify
from flask import request
import json
from jsonDB import *

app = Flask(__name__)

secureSafe = readData('DB.txt')

'''
secureSafe = {
    '[234324,34534]' : {
        'public_key' : [234234,234234],
        'accounts' : {
            'Facebook' : [24234,234234,234234]
        }
    }
}
'''

@app.route('/register', methods=['POST'])
def registerUser():
    new_key = request.get_json()
    for key in new_key:
        secureSafe[str(new_key[key])] = {
            'public_key' : new_key[key],
            'accounts' : {}
        }
    saveData('DB.txt',secureSafe)
    return jsonify({'New Public Key' : new_key[key]})

@app.route('/addAccount', methods=['POST'])
def addAccount():
    data = request.get_json()
    keyuser = str(data['public_key'])
    name = data['name']
    password = data['password']
    secureSafe[keyuser]['accounts'][name] = password
    saveData('DB.txt',secureSafe)
    return jsonify({'Status' : 200})

@app.route('/editAccount', methods=['POST'])
def editAccount():
    data = request.get_json()
    keyuser = str(data['public_key'])
    name = data['name']
    password = data['password']
    secureSafe[keyuser]['accounts'][name] = password
    saveData('DB.txt',secureSafe)
    return jsonify({'Status' : 200})

@app.route('/getAccount/<string:name>/<string:token>', methods=['GET'])
def getAccount(name,token):
    data = {}
    if token in secureSafe:
        if name in secureSafe[token]['accounts']:
            data = {
                'name' : name,
                'password' : secureSafe[token]['accounts'][name]
            }
    return jsonify(data)

@app.route('/getAccounts/<string:token>', methods=['GET'])
def getAccounts(token):
    data = {}
    if token in secureSafe:
        data = secureSafe[token]['accounts']
    return jsonify(data)

@app.route('/getList/<string:token>', methods=['GET'])
def getList(token):
    data = {}
    aList = []
    if token in secureSafe:
        for key in secureSafe[token]['accounts']:
            aList.append(key)
        data = {'accounts':aList}
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
