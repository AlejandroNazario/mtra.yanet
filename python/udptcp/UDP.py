import socket

def main():
    host = '127.0.0.1'
    port = 65432

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            while True:
                try:
                    message = input("Ingrese el mensaje: ")
                    s.sendto(message.encode(), (host, port))
                    data, addr = s.recvfrom(1024)
                    print("Respuesta del servidor:", data.decode())
                except Exception as e:
                    print("Se ha producido un error durante la comunicación con el servidor:", e)
    except Exception as e:
        print("Se ha producido un error al crear el socket:", e)

if __name__ == "__main__":
    main()
