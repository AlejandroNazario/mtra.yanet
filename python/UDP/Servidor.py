from socket import*

mi_puerto = 13000
mi_servidorSocket = socket(AF_INET, SOCK_DGRAM)
mi_servidorSocket.bind(('192.168.1.68', mi_puerto))
print("Servidor Listo...")
while True:
    mensaje, dirCliente = mi_servidorSocket.recvfrom(2048)
    print("cliente ON...")
    print(dirCliente)
    print(mensaje)
    mi_servidorSocket.sendto(mensaje, dirCliente)