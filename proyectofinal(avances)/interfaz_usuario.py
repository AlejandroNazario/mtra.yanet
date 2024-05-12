import tkinter as tk
import agregar_alumno
import iniciar_sesion

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Sistema de Control de Alumnos")

# Crear los botones para "Agregar Alumno" e "Iniciar Sesión"
boton_agregar = tk.Button(ventana, text="Agregar Alumno", command=agregar_alumno.agregar_alumno)
boton_agregar.pack(pady=10)

boton_iniciar_sesion = tk.Button(ventana, text="Iniciar Sesión", command=iniciar_sesion.iniciar_sesion)
boton_iniciar_sesion.pack(pady=10)

# Iniciar la interfaz de usuario
ventana.mainloop()
