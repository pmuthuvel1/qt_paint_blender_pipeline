from socket import *
from time import ctime
from threading import Thread

class ClientHandler(Thread):
    """Handles a client request."""
    def __init__(self, client):
        Thread.__init__(self)
        self._client = client

    def run(self):
        #self._client.send(bytes(ctime() + '\nHave a nice day!' , 'ascii'))
        while True:
            # receive data stream. it won't accept data packet greater than 1024 bytes
            data = self._client.recv(1024).decode()
            print("data received from client is :"+data)
            if not data:
                # if data is not received break
                break


HOST = "127.0.0.1"
PORT = 5555 # Port number was changed here
BUFSIZE = 1024
ADDRESS = (HOST, PORT)

server = socket(AF_INET, SOCK_STREAM)
server.bind(ADDRESS)
server.listen(5)

# The server now just waits for connections from clients
# and hands sockets off to client handlers
while True:
    print('Waiting for connection')
    client, address = server.accept()
    print('...connected from:', address)
    handler = ClientHandler(client)
    handler.start()
