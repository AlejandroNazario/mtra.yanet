import cv2
import mysql.connector
import io
import numpy as np
from PIL import Image

# Configuración para conectarse a MySQL
db_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'rostros'
}

# Carga el clasificador Haar para detección de rostros
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def iniciar_sesion(numero_control):
    # Conectar a la base de datos y obtener la imagen del alumno por su número de control
    db = mysql.connector.connect(**db_config)
    cursor = db.cursor()
    cursor.execute("SELECT imagen FROM alumnos WHERE numero_control = %s", (numero_control,))
    row = cursor.fetchone()
    cursor.close()
    db.close()

    if row is not None:
        imagen_guardada = np.frombuffer(row[0], np.uint8)
        imagen_guardada = cv2.imdecode(imagen_guardada, cv2.IMREAD_COLOR)

        # Capturar la imagen actual de la cámara
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cap.release()

        if ret:
            # Convertir la imagen actual a escala de grises para la detección de rostros
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detectar rostros en la imagen actual
            faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            for (x, y, w, h) in faces:
                roi_gray = gray_frame[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]

                # Comparar la imagen actual con la imagen guardada
                if comparar_imagenes(imagen_guardada, roi_gray):
                    print("Inicio de sesión exitoso")
                    # Aquí podrías mostrar los datos del alumno
                    break
            else:
                print("Inicio de sesión fallido: No se encontró el rostro")

def comparar_imagenes(imagen_guardada, imagen_actual):
    # Implementa tu lógica de comparación de imágenes aquí
    # Por ejemplo, podrías usar algoritmos de comparación de imágenes como SSIM o Histograma de Gradientes Orientados (HOG)
    # En este ejemplo, simplemente comparamos el tamaño de las imágenes
    return imagen_guardada.shape == imagen_actual.shape

# Iniciar sesión con un número de control específico (aquí deberías obtener el número de control del usuario)
numero_control = "123456"
iniciar_sesion(numero_control)
