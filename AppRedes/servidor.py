from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

def handle_client():
    for i in range(3):
        
        req = socket_client.recv(1024)

        print(f'A requisição foi {req.decode()}')

        rep = 'Hello, Cliente'

        socket_client.send(rep.encode())

        socket_client.close()

server_socket = socket(AF_INET, SOCK_STREAM)

server_socket.bind(('127.0.0.1', 12345))
server_socket.listen()

print('Servidor esperando por requisições')

while True:

    socket_client, client_addr = server_socket.accept()
    print(f'Cliente com addr {client_addr} estabeleceu a comunicação')
    Thread(target=handle_client, args=(socket_client)).start()

