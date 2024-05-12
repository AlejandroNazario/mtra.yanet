package cliente;

import java.io.*;
import java.net.*;

public class UDPServer {
    public static void main(String[] args) {
        int port = 65432;

        try {
            DatagramSocket socket = new DatagramSocket(port);

            byte[] receiveBuffer = new byte[1024];

            while (true) {
                DatagramPacket receivePacket = new DatagramPacket(receiveBuffer, receiveBuffer.length);
                socket.receive(receivePacket);

                String message = new String(receivePacket.getData(), 0, receivePacket.getLength());
                System.out.println("Mensaje del cliente: " + message);

                InetAddress clientAddress = receivePacket.getAddress();
                int clientPort = receivePacket.getPort();
                String responseMessage = "Respuesta al cliente";
                byte[] sendBuffer = responseMessage.getBytes();

                DatagramPacket sendPacket = new DatagramPacket(sendBuffer, sendBuffer.length, clientAddress, clientPort);
                socket.send(sendPacket);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
