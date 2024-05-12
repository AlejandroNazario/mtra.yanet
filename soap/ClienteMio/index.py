import tkinter as tk
from zeep import Client

# Función para realizar operaciones de acuerdo al signo ingresado
def calcular():
    num1 = int(entrada_num1.get())
    num2 = int(entrada_num2.get())
    signo = entrada_signo.get()

    if signo == '+':
        resultado = cliente.service.sumar(num1, num2)
    elif signo == '-':
        resultado = cliente.service.restar(num1, num2)
    elif signo == '*':
        resultado = cliente.service.multiplicar(num1, num2)
    elif signo == '/':
        resultado = cliente.service.dividir(num1, num2)
    else:
        resultado = "Operación no válida"

    etiqueta_resultado.config(text="Resultado: {}".format(resultado))
    actualizar_contador()

# Función para obtener el contador de peticiones
def obtener_contador():
    contador = cliente.service.getContadorPeticiones()
    etiqueta_contador.config(text="Contador de peticiones: {}".format(contador))

# Función para actualizar el contador de peticiones
def actualizar_contador():
    obtener_contador()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")

# Crear campo de entrada para el primer número
etiqueta_num1 = tk.Label(ventana, text="Primer número:")
etiqueta_num1.grid(row=0, column=0)
entrada_num1 = tk.Entry(ventana)
entrada_num1.grid(row=0, column=1)

# Crear campo de entrada para el segundo número
etiqueta_num2 = tk.Label(ventana, text="Segundo número:")
etiqueta_num2.grid(row=1, column=0)
entrada_num2 = tk.Entry(ventana)
entrada_num2.grid(row=1, column=1)

# Crear campo de entrada para el signo
etiqueta_signo = tk.Label(ventana, text="Signo (+, -, *, /):")
etiqueta_signo.grid(row=2, column=0)
entrada_signo = tk.Entry(ventana)
entrada_signo.grid(row=2, column=1)

# Crear botón para calcular
boton_calcular = tk.Button(ventana, text="Calcular", command=calcular)
boton_calcular.grid(row=3, column=0, columnspan=2)

# Etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.grid(row=4, column=0, columnspan=2)

# Botón para obtener el contador de peticiones
boton_contador = tk.Button(ventana, text="Obtener Contador", command=obtener_contador)
boton_contador.grid(row=5, column=0, columnspan=2)

# Etiqueta para mostrar el contador de peticiones
etiqueta_contador = tk.Label(ventana, text="")
etiqueta_contador.grid(row=6, column=0, columnspan=2)

# Crear cliente para el servicio web SOAP
cliente = Client('http://192.168.227.83:8080/WSSoap/CalculadoraWSService?WSDL')

# Actualizar el contador inicialmente
actualizar_contador()

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
