from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

public_key = {
    'Hola' : 'Mundo'
}

class Hello(Resource):
    def get(self, data):
        #return {"Hello":name}
        return public_key
    def put(self, data):
        public_key[data[0]]=data[1]

api.add_resource(Hello, '/hello/<data>')

if __name__ == '__main__':
 app.run(debug=True)