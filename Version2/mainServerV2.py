from flask import Flask
from flask import jsonify
from flask import request
from flask import Response
import json
from jsonDB import *
from RSAE import *

app = Flask(__name__)

secureSafe = readData('DB.txt')
RSA_O = RSAE()
keys = RSA_O.GenerateKeys()

@app.route('/getServerKey', methods=['GET'])
def getServerKey():
    data = {'serverpk' : keys[0]}
    return jsonify(data)

@app.route('/register', methods=['POST'])
def registerUser():
    new_key = request.get_json()
    for key in new_key:
        secureSafe[str(new_key[key])] = {
            'public_key' : new_key[key],
            'accounts' : {}
        }
    saveData('DB.txt',secureSafe)
    return jsonify({'serverpk' : keys[0]})

@app.route('/addAccount', methods=['POST'])
def addAccount():
    data = request.get_json()
    keyuser = RSA_O.de_encryptM(data['public_key'],keys[1])
    if keyuser in secureSafe:
        name = RSA_O.de_encryptM(data['name'],keys[1])
        if name not in secureSafe[keyuser]['accounts']:
            password = data['password']
            secureSafe[keyuser]['accounts'][name] = password
            saveData('DB.txt',secureSafe)
            return Response(json.dumps({'message':'Success'}), status=200)
        else:
            return Response(json.dumps({'message':'Account already active'}), status=400)
    else:
        return Response(json.dumps({'message':'User not found'}), status=400)

@app.route('/editAccount', methods=['PUT'])
def editAccount():
    data = request.get_json()
    keyuser = RSA_O.de_encryptM(data['public_key'],keys[1])
    name = RSA_O.de_encryptM(data['name'],keys[1])
    password = data['password']
    if keyuser in secureSafe:
        if name in secureSafe[keyuser]['accounts']:
            secureSafe[keyuser]['accounts'][name] = password
            saveData('DB.txt',secureSafe)
            return Response(json.dumps({'message':'Success'}), status=200)
        else:
            return Response(json.dumps({'message':'Account not found'}), status=400)
    else:
        return Response(json.dumps({'message':'User not found'}), status=400)
    return Response(json.dumps({'message':'Internal Error'}), status=400)

@app.route('/deleteAccount', methods=['DELETE'])
def deleteAccount():
    data = request.get_json()
    keyuser = RSA_O.de_encryptM(data['public_key'],keys[1])
    if keyuser in secureSafe:
        name = RSA_O.de_encryptM(data['name'],keys[1])
        if name in secureSafe[keyuser]['accounts']:
            del secureSafe[keyuser]['accounts'][name]
            saveData('DB.txt',secureSafe)
            return Response(json.dumps({'message':'Success'}), status=200)
        else:
            return Response(json.dumps({'message':'Account not found'}), status=400)
    else:
        return Response(json.dumps({'message':'User not found'}), status=400)
    return Response(json.dumps({'message':'Internal Error'}), status=400)

@app.route('/getAccount', methods=['GET'])
def getAccount():
    rjson = request.get_json()
    name = RSA_O.de_encryptM(rjson['name'],keys[1])
    token = RSA_O.de_encryptM(rjson['data'],keys[1])
    if token in secureSafe:
        if name in secureSafe[token]['accounts']:
            data = {
                'name' : name,
                'password' : secureSafe[token]['accounts'][name]
            }
            return Response(json.dumps(data), status=200)
        else:
            return Response(json.dumps({'message':'Account not found'}), status=400)
    else:
        return Response(json.dumps({'message':'User not found'}), status=400)
    return Response(json.dumps({'message':'Internal Error'}), status=400)

@app.route('/getAccounts', methods=['GET'])
def getAccounts():
    data = request.get_json()
    decryptedToken = RSA_O.de_encryptM(data['data'],keys[1])
    if decryptedToken in secureSafe:
        data = secureSafe[decryptedToken]['accounts']
    return jsonify(data)

@app.route('/getList', methods=['GET'])
def getList():
    data = request.get_json()
    aList = []
    decryptedToken = RSA_O.de_encryptM(data['data'],keys[1])
    if decryptedToken in secureSafe:
        for key in secureSafe[decryptedToken]['accounts']:
            aList.append(key)
        data = {'accounts':aList}
    else:
        return jsonify({'accounts':[]})
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
