import socket

HOST = '192.168.137.1'
PORT = 30000

try:

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()

        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break

                # Descomentar para hardcodear respuesta    
                #conn.send("Mensaje de prueba".encode('utf-8'))  
                
                message = input("Escribe mensaje para cliente: ")
                conn.send(message.encode('utf-8'))
                    
                print("Cliente: " + data.decode('utf-8'))
                
except Exception as e:
    print("Error:", e)