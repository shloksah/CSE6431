import socket

class server:

    def run(self):
        HOST = '127.0.0.1'
        PORT = 1234

        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))

        server_socket.listen()

        print('Server ready and listening')

        conn, addr = server_socket.accept()
        with conn:
            print('Connection received from: {}'.format(addr))
            while True:
                data = (conn.recv(1024)).decode()
                if(data):
                    print('Received data from client {}'.format(data))
                    response = 'Accept by server'
                    conn.send(response.encode())
                #if data == 'stop':
                   # break
        server_socket.close()
        return
