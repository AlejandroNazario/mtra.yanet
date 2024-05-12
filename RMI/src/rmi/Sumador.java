package rmi;

import java.rmi.Remote;
import java.rmi.RemoteException;

public interface Sumador extends Remote {
    int sumar(int a, int b) throws RemoteException;
    int restar(int a, int b) throws RemoteException;
    int multiplicar(int a, int b) throws RemoteException;
    int dividir(int a, int b) throws RemoteException;
    double calcularRaiz(double c) throws RemoteException; 
    double calcularPotencia(double d, double e) throws RemoteException; 
}