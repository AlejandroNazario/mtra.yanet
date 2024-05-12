from zeep import Client

cliente = Client('http://localhost:8080/ServidorMio/WSOperaciones?WSDL')

if cliente.service.Login("Leo","123"):
    print("Login Correcto")
else:
    print("Login Incorrecto")
    


if cliente.service.ProcesarPago(5000,100)>=0:
    print("Pago Correcto")
else:
    print("Pago incorrecto")