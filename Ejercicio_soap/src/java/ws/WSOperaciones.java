/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package ws;

import javax.jws.WebService;
import javax.jws.WebMethod;
import javax.jws.WebParam;

/**
 *
 * @author alexc
 */
@WebService(serviceName = "WSOperaciones")
public class WSOperaciones {

    /**
     * Web service operation
     */
    @WebMethod(operationName = "Login")
    public Boolean Login(@WebParam(name = "usuario") String usuario, @WebParam(name = "contrasena") String contrasena) {
        //TODO write your implementation code here:
        //return null;
        if(usuario.equals("alex") && contrasena.equals("alex123")){
            return true;
        }else{
            return false;
        }
    }

    /**
     * Web service operation
     */
    @WebMethod(operationName = "Procesos")
    public int Procesos(@WebParam(name = "variable1") int variable1, @WebParam(name = "variable2") int variable2) {
        //TODO write your implementation code here:
        //return 0;
        if(variable1>=variable2){
            return variable1-variable2;
        }else{
            return -1;
        }
    }

    /**
     * This is a sample web service operation
     */
    /*
    @WebMethod(operationName = "hello")
    public String hello(@WebParam(name = "name") String txt) {
        return "Hello " + txt + " !";
    }*/
    
}
