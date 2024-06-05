from socket import socket, AF_INET, SOCK_DGRAM
from threading import Thread

def handle_clientRequest(mserver_socket):
    for j in range(3):
        message, client_adress = server_socket.recvfrom(2048)
        req = message.decode()

        print(f'A mensagem foi recebida do cliente {client_adress}: {req}')
        reply = f'Olá, {client_adress}! Eu sou o servidor!'

        server_socket.sendto(reply.encode(), client_adress)

server_adress = 11705
server_name = 'localhost'

server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind((server_name, server_adress))

print('Servidor pronto para receber mensagens!')

for i in range(3):
    Thread(target=handle_clientRequest, args=(server_socket, )).start()