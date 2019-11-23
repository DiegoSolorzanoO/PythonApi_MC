import socket
import pickle
import time
import os

IP = "127.0.0.1"
PORT = 1234

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
client_socket.setblocking(False)

print('Connecting...')
time.sleep(3)
os.system('cls')
print('===============================')
print('Welcome to the password keeper')
print('===============================')

while True:
    try:
        msg_revc = client_socket.recv(2048)
        if msg_revc:
            print(msg_revc.decode('utf-8'))
    except:
        pass
    msg = input('>> ')
    client_socket.send(msg.encode('utf-8'))
    time.sleep(1)