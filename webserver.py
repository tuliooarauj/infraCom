from socket import socket, AF_INET, SOCK_STREAM

web_server = socket(AF_INET, SOCK_STREAM)
web_server.bind(('localhost', 12345))
web_server.listen()

print('Servidor esperando por requisições')

for i in range(2):
    client_socket, client_addr = web_server.accept()
    print(f'Servidor irá se comunicar com: {client_addr}')
    req = client_socket.recv(1024)

    print(f'A requisição foi: {req}')

    header_http = 'HTTP/1.1 200 OK \r\n' \
        'Date: Thu, 16 May, 2024 13:15:46 GMT \r\n'\
        'Server: Myserver/0.0.1 (Ubuntu) \r\n' \
        'Content-Type: text/html \r\n' \
        '\r\n'
    
    msg_body  = '<html>' \
              '<head><title>Hello, World</title></head>' \
              '<body><h1> Your first web server!</h1>' \
              '<h3>Congratulation!!</h3>' \
              '</body>' \
              '</html>'
    

    reply = header_http + msg_body


    client_socket.send(reply.encode())
    client_socket.close()

    
