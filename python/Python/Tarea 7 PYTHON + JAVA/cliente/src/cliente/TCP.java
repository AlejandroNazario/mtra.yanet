/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package cliente;



import java.io.*;
import java.net.*;
import java.util.Scanner;

public class TCP {

    public static void main(String[] args) throws IOException {
      try {  

        Socket socket = new Socket("192.168.137.1", 5000);    

        InputStream input = socket.getInputStream();
        BufferedReader reader = new BufferedReader(new InputStreamReader(input));
    
        OutputStream output = socket.getOutputStream();
        PrintWriter writer = new PrintWriter(output, true);
        
        Scanner scanner = new Scanner(System.in);
        
        String message, response;
        
        do {
            message = scanner.nextLine(); 
            writer.println(message);
            writer.flush(); 

            response = reader.readLine();
            System.out.println("Servidor: " + response); 

        } while (!message.equals("chao"));
        
        socket.close();
      
      } catch (Exception e) {
        e.printStackTrace();  
      }
    } 
}