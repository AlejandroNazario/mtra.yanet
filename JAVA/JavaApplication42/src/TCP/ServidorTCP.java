/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package TCP;
 
import java.io.*;
import java.net.*;
import java.util.ArrayList;
import java.util.List;

public class ServidorTCP {
    private static List<PrintWriter> clientes = new ArrayList<>();

    public static void main(String[] args) {
        try {
            ServerSocket serverSocket = new ServerSocket(12345);
            System.out.println("Servidor esperando conexiones...");

            while (true) {
                Socket clientSocket = serverSocket.accept();
                System.out.println("Cliente conectado desde: " + clientSocket.getInetAddress());

                // Configura los flujos de entrada y salida para este cliente
                BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
                PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true);

                // Agrega el flujo de salida del cliente a la lista
                clientes.add(out);

                // Crea un hilo para manejar las comunicaciones con este cliente
                Thread clientThread = new Thread(new ClientHandler(in, out));
                clientThread.start();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    // Clase interna para manejar las comunicaciones con un cliente específico
    private static class ClientHandler implements Runnable {
        private BufferedReader in;
        private PrintWriter out;

        public ClientHandler(BufferedReader in, PrintWriter out) {
            this.in = in;
            this.out = out;
        }

        @Override
        public void run() {
            try {
                String mensajeCliente;
                while ((mensajeCliente = in.readLine()) != null) {
                    System.out.println("Mensaje recibido: " + mensajeCliente);

                    // Envía el mensaje a todos los clientes conectados
                    for (PrintWriter cliente : clientes) {
                        cliente.println(mensajeCliente);
                        cliente.flush(); // Asegúrate de que los datos se envíen de inmediato
                    }
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}
