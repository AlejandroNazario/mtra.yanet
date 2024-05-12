from socket import *

nombreServidor = '192.168.1.68'
mi_puerto = 13000
mi_clienteSocket = socket(AF_INET, SOCK_DGRAM)
entrada = input("¿Mensaje?:")
mi_clienteSocket.sendto(entrada.encode(),(nombreServidor, mi_puerto))
mensaje_rec, dirServidor = mi_clienteSocket.recvfrom(2048)
print("Servidor...")
print(dirServidor)
print("Hecho")
print(mensaje_rec)
mi_clienteSocket.close()
