from socket import*

mi_socket = socket (AF_INET, SOCK_STREAM)
mi_socket.bind(('192.168.1.68', 12000))
mi_socket.listen(5)
while True:
    conexion, addr = mi_socket.accept()
    print("conexion establecida")
    print(addr)
    peticion = conexion.recv(1024)
    print(peticion)
    conexion.send(("Yo servidor...").encode()) 