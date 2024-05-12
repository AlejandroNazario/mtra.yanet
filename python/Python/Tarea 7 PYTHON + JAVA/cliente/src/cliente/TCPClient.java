
package cliente;

import java.io.*;
import java.net.*;

public class TCPClient {
    public static void main(String[] args) {
        String host = "127.0.0.1";
        int port = 12345;

        try {
            Socket socket = new Socket(host, port);

            BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
            PrintWriter writer = new PrintWriter(socket.getOutputStream(), true);

            BufferedReader serverReader = new BufferedReader(new InputStreamReader(socket.getInputStream()));

            String userInput;
            while ((userInput = reader.readLine()) != null) {
                writer.println(userInput);
                System.out.println("Respuesta del servidor: " + serverReader.readLine());
            }

            reader.close();
            writer.close();
            serverReader.close();
            socket.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
