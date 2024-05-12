/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package UDP;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.util.Scanner;

public class ClienteUDP {

    private static final int PORT = 53858; // Use a fixed port

    public static void main(String[] args) throws Exception {
        try (Scanner scanner = new Scanner(System.in);
             DatagramSocket socket = new DatagramSocket(PORT))
            {
            InetAddress address = InetAddress.getByName("0.0.0.0"); // Change this if necessary

            while (true) {
                // Leer mensaje del usuario
                System.out.print("Introduzca un mensaje: ");
                String message = scanner.nextLine();

                // Enviar mensaje al servidor
                byte[] data = message.getBytes();
                DatagramPacket packet = new DatagramPacket(data, data.length, address, PORT);
                socket.send(packet);

                // Recibir respuesta del servidor
                byte[] buffer = new byte[1024];
                packet = new DatagramPacket(buffer, buffer.length);
                try {
                    socket.receive(packet);
                } catch (IOException e) {
                    System.err.println("Error al recibir respuesta: " + e.getMessage());
                    continue;
                }

                // Mostrar la respuesta
                String response = new String(packet.getData(), 0, packet.getLength());
                System.out.println("Respuesta del servidor: " + response);
            }
        } catch (IOException e) {
            System.err.println("Error al crear el socket: " + e.getMessage());
        }
    }
}
