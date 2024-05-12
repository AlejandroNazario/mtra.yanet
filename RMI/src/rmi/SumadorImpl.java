package rmi;

import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class SumadorImpl extends UnicastRemoteObject implements Sumador {
    public SumadorImpl() throws RemoteException {
        super();
    }

    public int sumar(int a, int b) throws RemoteException {
        return a + b;
    }

    public int restar(int a, int b) throws RemoteException {
        return a - b;
    }

    public int multiplicar(int a, int b) throws RemoteException {
        return a * b;
    }

    public int dividir(int a, int b) throws RemoteException {
        return a / b;
    }
    
      public double calcularRaiz(double c) throws RemoteException { 
        return Math.sqrt(c);
    }

    public double calcularPotencia(double d, double e) throws RemoteException { 
        return Math.pow(d, e);
    }
}