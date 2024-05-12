import socket

HOST = '192.168.137.1' 
PORT = 65432        

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    
    while True:
        data, addr = s.recvfrom(1024)
        message = input("Escribe mensaje para cliente: ")
        s.sendto(message.encode('utf-8'), addr)
        
        print("Mensaje cliente:", data.decode()) 