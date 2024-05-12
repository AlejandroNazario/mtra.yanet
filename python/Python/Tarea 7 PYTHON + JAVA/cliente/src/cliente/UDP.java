package cliente;

import java.io.*;
import java.net.*;
import java.util.Scanner;

public class UDP {

    public static void main(String args[]) throws Exception {
    
        Scanner scanner = new Scanner(System.in); 

        DatagramSocket socket = new DatagramSocket();
        InetAddress host = InetAddress.getByName("192.168.137.1");
        int port = 20001;

        while(true) {
            // Solicitar al usuario que ingrese el mensaje
            System.out.print("Ingrese mensaje Pan: ");
            String mensaje = scanner.nextLine();
            byte[] send = mensaje.getBytes(); 

            // Crear el paquete de datos con el mensaje y enviarlo al servidor
            DatagramPacket request = 
                    new DatagramPacket(send, send.length, host, port);
            socket.send(request);
            
            // Preparar el paquete para recibir la respuesta del servidor
            byte[] buffer = new byte[1024];
            DatagramPacket response = 
                    new DatagramPacket(buffer, buffer.length); 

            // Esperar y recibir la respuesta del servidor
            socket.receive(response);

            // Convertir la respuesta a texto y mostrarla
            String text = new String(buffer, 0, response.getLength());     
            System.out.println("Respuesta del servidor: " + text);
        }
   } 
}
