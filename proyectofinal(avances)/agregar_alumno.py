import cv2
import mysql.connector
import io
import numpy as np
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox

# Configuración para conectarse a MySQL
db_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'rostros'
}

# Carga el clasificador Haar para detección de rostros
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


# Función para guardar los datos del alumno en la base de datos
def guardar_datos(nombre, numero_control):
    db = mysql.connector.connect(**db_config)
    cursor = db.cursor()
    query = "INSERT INTO alumnos (nombre, numero_control) VALUES (%s, %s)"
    cursor.execute(query, (nombre, numero_control))
    db.commit()
    cursor.close()
    db.close()
    messagebox.showinfo("Éxito", "Datos del alumno guardados en la base de datos")

# Función para guardar la foto del rostro del alumno en la base de datos
def guardar_foto(id_alumno, foto):
    # Convierte el fotograma a formato JPEG
    pil_image = Image.fromarray(foto)
    img_bytes = io.BytesIO()
    pil_image.save(img_bytes, format='JPEG')
    img_bytes = img_bytes.getvalue()

    # Actualiza la imagen en la base de datos utilizando la misma ID de alumno
    db = mysql.connector.connect(**db_config)
    cursor = db.cursor()
    query = "UPDATE alumnos SET imagen = %s WHERE id = %s"
    cursor.execute(query, (img_bytes, id_alumno))
    db.commit()
    cursor.close()
    db.close()
    messagebox.showinfo("Éxito", "Registro facial agregado con éxito")

# Función para capturar la imagen del rostro del alumno
def capturar_foto(id_alumno):
    ret, frame = cap.read()
    if ret:
        # Convierte el fotograma a RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        guardar_foto(id_alumno, rgb_frame)

# Función para procesar el inicio de sesión del alumno
def iniciar_sesion():
    nombre = entry_nombre.get()
    numero_control = entry_numero_control.get()
    if nombre and numero_control:
        guardar_datos(nombre, numero_control)
        # Obtener el ID del alumno recién insertado
        db = mysql.connector.connect(**db_config)
        cursor = db.cursor()
        cursor.execute("SELECT id FROM alumnos ORDER BY id DESC LIMIT 1")
        id_alumno = cursor.fetchone()[0]
        cursor.close()
        db.close()
        capturar_foto(id_alumno)
    else:
        messagebox.showerror("Error", "Por favor ingrese nombre y número de control")

# Crea la ventana de la interfaz gráfica
ventana = tk.Tk()
ventana.title("Registro Facial de Alumnos")

# Crea y posiciona los campos de entrada (Entry) y etiquetas (Label)
label_nombre = tk.Label(ventana, text="Nombre:")
label_nombre.grid(row=0, column=0, padx=10, pady=5)
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=0, column=1, padx=10, pady=5)

label_numero_control = tk.Label(ventana, text="Número de Control:")
label_numero_control.grid(row=1, column=0, padx=10, pady=5)
entry_numero_control = tk.Entry(ventana)
entry_numero_control.grid(row=1, column=1, padx=10, pady=5)

# Botones para guardar los datos del alumno y agregar el rostro facial
boton_guardar_datos = tk.Button(ventana, text="Guardar Datos", command=iniciar_sesion)
boton_guardar_datos.grid(row=2, column=0, columnspan=2, pady=10)

# Abre la cámara web
cap = cv2.VideoCapture(0)

# Inicia la ventana
ventana.mainloop()
