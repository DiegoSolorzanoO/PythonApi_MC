import requests
import json
from RSAE import *

RSA_O = RSAE()
keys = RSA_O.GenerateKeys()
public_key = keys[0]
private_key = keys[1]

# response = requests.get("http://127.0.0.1:5000")
# print(response.json())

# response = requests.get("http://127.0.0.1:5000/warehouse")
# print(response.json())

response = requests.get("http://127.0.0.1:5000/warehouse/Knife")
print(response.json())

response = requests.post("http://127.0.0.1:5000/sendKey", json={'New Public Key':public_key})
print(response.json())



