package rmi;

import java.rmi.Naming;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.Scanner;

public class Cliente {
    public static void main(String[] args) {
        try {
            // Obtener una referencia al registro RMI
             Sumador operaciones = (Sumador) Naming.lookup("rmi://192.168.217.66:1099/Operaciones");
         

            // Crear un objeto Scanner para leer la entrada del usuario
            Scanner scanner = new Scanner(System.in);

            while (true) {
                System.out.println("\nSeleccione una operación:");
                System.out.println("1. Sumar");
                System.out.println("2. Restar");
                System.out.println("3. Multiplicar");
                System.out.println("4. Dividir");
                System.out.println("5. Raíz");
                System.out.println("6. Potencia");
                System.out.println("7. Salir");
                System.out.println("Escriba La Opcion A Elegir...");

                int opcion = scanner.nextInt();

                if (opcion == 7) {
                    break;
                }

                switch (opcion) {
                    case 1:
                    case 2:
                    case 3:
                    case 4:
                        System.out.print("Ingrese el primer número: ");
                        int a = scanner.nextInt();
                        System.out.print("Ingrese el segundo número: ");
                        int b = scanner.nextInt();

                        switch (opcion) {
                            case 1:
                                int resultadoSuma = operaciones.sumar(a, b);
                                System.out.println("Resultado de la suma: \n ⌞ " + resultadoSuma + " ⌝");
                                break;
                            case 2:
                                int resultadoResta = operaciones.restar(a, b);
                                System.out.println("Resultado de la resta: \n ⌞ " + resultadoResta + " ⌝");
                                break;
                            case 3:
                                int resultadoMultiplicacion = operaciones.multiplicar(a, b);
                                System.out.println("Resultado de la multiplicación: \n ⌞ " + resultadoMultiplicacion + " ⌝");
                                break;
                            case 4:
                                int resultadoDivision = operaciones.dividir(a, b);
                                System.out.println("Resultado de la división: \n ⌞ " + resultadoDivision + " ⌝");
                                break;
                        }
                        break;
                    case 5:
                        System.out.print("Ingrese el número: ");
                        double c = scanner.nextDouble();
                        double resultadoRaiz = operaciones.calcularRaiz(c);
                        System.out.println("Resultado de la raíz cuadrada: \n ⌞ " + resultadoRaiz + " ⌝");
                        break;
                    case 6:
                        System.out.print("Ingrese la base: ");
                        double d = scanner.nextDouble();
                        System.out.print("Ingrese el exponente: ");
                        double e = scanner.nextDouble();
                        double resultadoPotencia = operaciones.calcularPotencia(d, e);
                        System.out.println("Resultado de la potencia: \n ⌞ " + resultadoPotencia + " ⌝");
                        break;
                    default:
                        System.out.println("Opción inválida.");
                        break;
                }
            }

        } catch (Exception e) {
            System.err.println("Excepción en el cliente: " + e.toString());
            e.printStackTrace();
        }
    }
}