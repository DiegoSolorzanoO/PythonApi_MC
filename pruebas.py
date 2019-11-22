import requests
import json
from RSAE import *

RSA_O = RSAE()
keys = RSA_O.GenerateKeys()
public_key = keys[0]
private_key = keys[1]

encrypted_message = RSA_O.encryptM({'Mates compus' : 95, 'Algebra' : 98},public_key,'json')
print(encrypted_message)

print(RSA_O.de_encryptM(encrypted_message,private_key,'json'))