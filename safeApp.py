import requests
import json
from RSAE import *
import time
from jsonDB import *
import os

RSA_O = RSAE()

keys = readData('KEYS.txt')
if keys:
    print('Keys detected, loading...')
    time.sleep(3)
else:
    print('Keys not detected, generating new ones...')
    new_keys = RSA_O.GenerateKeys()
    keys = {
        'public_key' : new_keys[0],
        'private_key' : new_keys[1]
    }
    saveData('KEYS.txt',keys)
    time.sleep(2)
    response = requests.post("http://127.0.0.1:5000/register", json={'New Public Key':keys['public_key']})
    print('Keys generated') 

while True:
    print('========================================')
    print('SafeApp v0.1.0')
    print('========================================')
    print('Menu:')
    print('1 - List accounts')
    print('2 - Get all accounts')
    print('3 - Get account')
    print('4 - Add account')
    print('5 - Edit account')
    print('6 - Delete account')
    print('7 - Exit')
    print('========================================')
    command = input('>> ')

    if command == '1':
        print('========================================')
        response = requests.get("http://127.0.0.1:5000/getList/"+str(keys['public_key']))
        data = response.json()
        for value in data['accounts']:
            print(value)
        print('========================================')
        x = input()
        os.system('cls')
    elif command == '2':
        print('========================================')
        response = requests.get("http://127.0.0.1:5000/getAccounts/"+str(keys['public_key']))
        data = response.json()
        for key in data:
            print(key + ' : ' + RSA_O.de_encryptM(data[key],keys['private_key']))
        print('========================================')
        x = input()
        os.system('cls')
    elif command == '3':
        print('========================================')
        print('Get account (Type cancel to cancel)')
        print('========================================')
        name = input('Account name: ')
        if name != 'cancel':
            response = requests.get("http://127.0.0.1:5000/getAccount/"+name+'/'+str(keys['public_key']))
            data = response.json()
            print('========================================')
            print(data['name'] + ' : ' + RSA_O.de_encryptM(data['password'],keys['private_key']))
            print('========================================')
            x = input()
            os.system('cls')
    elif command == '4':
        print('========================================')
        print('Add account (Type cancel to cancel)')
        print('========================================')
        name = input('Name: ')
        if name != 'cancel':
            password = RSA_O.encryptM(input('Password: '),keys['public_key'])
            response = requests.post("http://127.0.0.1:5000/addAccount", json={'public_key':keys['public_key'],'name':name,'password':password})
            print('========================================')
            print('Account Added')
            print('========================================')
            time.sleep(3)
            os.system('cls')
    elif command == '5':
        print('========================================')
        print('Edit account (Type cancel to cancel)')
        print('========================================')
        name = input('Name: ')
        if name != 'cancel':
            password = RSA_O.encryptM(input('New Password: '),keys['public_key'])
            response = requests.post("http://127.0.0.1:5000/editAccount", json={'public_key':keys['public_key'],'name':name,'password':password})
            print('========================================')
            print('Account Edited')
            print('========================================')
            time.sleep(3)
            os.system('cls')
    elif command == '6':
        pass
    elif command == '7':
        print('========================================')
        print('Thanks for using SafeApp!')
        print('========================================')
        time.sleep(3)
        break



# response = requests.get("http://127.0.0.1:5000")
# print(response.json())

# response = requests.get("http://127.0.0.1:5000/warehouse")
# print(response.json())

# response = requests.get("http://127.0.0.1:5000/warehouse/Knife")
# print(response.json())

# response = requests.post("http://127.0.0.1:5000/sendKey", json={'New Public Key':public_key})
# print(response.json())



