import socket
import time
class client:

    def run(self,ops,timer):
        HOST = '127.0.0.1'
        PORT = 1234
        print('Hello client here!')
        client_socket = socket.socket()
        client_socket.connect((HOST, PORT))
        for i in ops:
            timer+=1
            self.helper(i+str(timer),client_socket)
        client_socket.close()
        return

    def helper(self,data,client_socket):


            #while True:
            #data = input('Send message to server: ')
            client_socket.send(data.encode())
            response = (client_socket.recv(1024)).decode()
            print('Server response: {}'.format(response))
            #client_socket.close()
                #if data == 'stop':
                    #break
            return