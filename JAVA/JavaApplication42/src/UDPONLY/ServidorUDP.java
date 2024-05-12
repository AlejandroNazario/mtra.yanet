/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package UDPONLY;

import java.net.*;
import java.io.*;

public class ServidorUDP {

  public static void main(String[] args) throws IOException {

    DatagramSocket socket = new DatagramSocket(5000);

    byte[] buffer = new byte[1024];

    while(true) {

      DatagramPacket peticion = new DatagramPacket(buffer, buffer.length);
      socket.receive(peticion);

      String mensaje = new String(peticion.getData(), 0, peticion.getLength());
      System.out.println("Mensaje recibido: " + mensaje);

      InetAddress direccion = peticion.getAddress();
      int puerto = peticion.getPort();

      String respuesta = "rHola cliente " + direccion + ":" + puerto;
      buffer = respuesta.getBytes();

      DatagramPacket respuestaPacket = new DatagramPacket(buffer, buffer.length, direccion, puerto);
      socket.send(respuestaPacket);
    }
  }
}