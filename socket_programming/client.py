import socket

HOST = '127.0.0.1'
PORT = 1234

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

while True:
    data = input('Send message: ')

    client_socket.send(data.encode())
    response = (client_socket.recv(1024)).decode()

    print('Server response: {}'.format(response))

    if data == 'stop':
        break
