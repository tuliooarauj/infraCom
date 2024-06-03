from socket import socket, AF_INET, SOCK_DGRAM

client_socket = socket(AF_INET, SOCK_DGRAM)

server_name = 'localhost'
server_port = 11705

server_adress = (server_name, server_port)

for i in range(3):

    message = input('Digite a mensagem: ')

    client_socket.sendto(message.encode(), server_adress)

    data, server_adress = client_socket.recvfrom(2048)

    reply = data.decode()

    print(f'O servidor respondeu: {reply}')

client_socket.close()