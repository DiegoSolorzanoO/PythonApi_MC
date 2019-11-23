import socket
import pickle
import time

IP = "127.0.0.1"
PORT = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((IP, PORT))
server_socket.listen()

print('Server online')
clientsocket, address = server_socket.accept()
print(f"Connection from {address} has been established")

isLogged = False
user = None

users = {
    'diego' : {
        'password': 'admin',
        'credentials': {
            'facebook': '3287174',
            'instagram': '237129847'
        }
    }
}

text = ''
while not isLogged:
    clientsocket.send((text+'User: ').encode('utf-8'))
    text = ''
    user = clientsocket.recv(2048).decode('utf-8')
    if user in users:
        clientsocket.send('Password: '.encode('utf-8'))
        password = clientsocket.recv(2048).decode('utf-8')
        if users[user]['password']==password:
            isLogged = True
            user = user
        else:
            text = 'Incorrect password\n'
    else:
        text = 'Incorrect username\n'

print('User Logged')
clientsocket.send(('Welcome back ' + user.upper()).encode('utf-8'))

while True:
    msg = clientsocket.recv(2048).decode('utf-8')
    if isLogged:
        if msg:
            if msg == 'Hi':
                clientsocket.send('Heyy'.encode('utf-8'))
            print(msg)

