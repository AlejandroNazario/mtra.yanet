/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.util.ArrayList;
import java.util.List;

public class ServidorUDP {

    private static final int PORT = 53858;
    private static List<InetAddress> clientAddresses = new ArrayList<>();

    public static void main(String[] args) throws Exception {
        try (DatagramSocket serverSocket = new DatagramSocket(PORT)) {
            System.out.println("Servidor UDP esperando datagramas...");

            while (true) {
                // Recibe datagrama
                byte[] buf = new byte[256];
                DatagramPacket packet = new DatagramPacket(buf, buf.length);
                serverSocket.receive(packet);

                // Obtiene la dirección y puerto del cliente
                InetAddress address = packet.getAddress();
                int port = packet.getPort();

                System.out.println("Datagrama recibido desde: " + address + ":" + port);

                // Check if client already connected
                if (!clientAddresses.contains(address)) {
                    clientAddresses.add(address); // Add new client address
                }

                // Procesa y difunde el mensaje
                String received = new String(packet.getData(), 0, packet.getLength());
                System.out.println("Mensaje recibido: " + received);

                // Enviar mensaje de vuelta al cliente
                String response = "Mensaje recibido correctamente";
                byte[] data = response.getBytes();
                packet = new DatagramPacket(data, data.length, address, port);
                serverSocket.send(packet);
            }
        } catch (IOException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
