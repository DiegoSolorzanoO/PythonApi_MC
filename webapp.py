import requests
import json

info = requests.post('http://localhost:5000/pk/hla',data=json.dumps({'Adios':'Mundo'}))
info = requests.get('http://localhost:5000/hello/hla')

print(info.json())
