from socket import*

mi_socket = socket (AF_INET, SOCK_STREAM)
mi_socket.connect(('192.168.1.68', 12000))
mi_socket.send(("Hola, soy cliente").encode())
respues = mi_socket.recv(1024)
print(respues)
mi_socket.close()