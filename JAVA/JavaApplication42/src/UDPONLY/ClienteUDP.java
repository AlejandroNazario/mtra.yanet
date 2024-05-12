/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package UDPONLY;

import java.net.*;
import java.io.*;

public class ClienteUDP {

  public static void main(String[] args) throws IOException {
    
    DatagramSocket socket = new DatagramSocket();

    InetAddress direccionServidor = InetAddress.getByName("192.168.225.88");
    int puertoServidor = 5000;

    BufferedReader entrada = new BufferedReader(new InputStreamReader(System.in));

    String mensaje;

    while(true) {
      
      System.out.print("Mensaje a enviar: ");
      mensaje = entrada.readLine();

      byte[] buffer = mensaje.getBytes();

      DatagramPacket peticion = new DatagramPacket(buffer, buffer.length, direccionServidor, puertoServidor);
      socket.send(peticion);

      byte[] buffer2 = new byte[1024];
      DatagramPacket respuesta = new DatagramPacket(buffer2, buffer2.length);
      socket.receive(respuesta);

      String respuestaString = new String(respuesta.getData(), 0, respuesta.getLength());
      System.out.println(respuestaString);
    }
  } 
}
