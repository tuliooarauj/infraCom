from socket import socket, AF_INET, SOCK_STREAM

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(('127.0.0.1', 12345))

for i in range(3):
    print(f'id da req: {i}')
    data = f'Hellor, server {i}'

    client_socket.send(data.encode())

    rep = client_socket.recv(1024)

    print(f'Reply from server {rep.decode()}')