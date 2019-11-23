
import requests
import json
from RSAE import *
'''
RSA_O = RSAE()
keys = RSA_O.GenerateKeys()
public_key = keys[0]
private_key = keys[1]

encrypted_message = RSA_O.encryptM({'Mates compus' : 95, 'Algebra' : 98},public_key,'json')
print(encrypted_message)

print(RSA_O.de_encryptM(encrypted_message,private_key,'json'))
'''

'''
import sqlite3
from sqlite3 import Error

con = sqlite3.connect('secureSafe.db')
db = con.cursor()

db.execute("CREATE TABLE TBL_SAFE(S_KEY text PRIMARY KEY, name text, salary real, department text, position text, hireDate text)")
db.commit()
'''

secureSafe = {
    '[234324,34534]' : {
        'public_key' : [234234,234234],
        'accounts' : {
            'Facebook' : [24234,234234,234234]
        }
    }
}

secureSafe['[234324,34534]']['accounts']['Twitter'] = [23434,23423,34234,23423]

print(secureSafe)