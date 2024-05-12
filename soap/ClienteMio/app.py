from flask import Flask, render_template, request, send_file
import zeep
from io import BytesIO
import mysql.connector

app = Flask(__name__)


wsdl_url = 'http://192.168.218.216:8080/ServidorMio/WSOperaciones?WSDL'
client = zeep.Client(wsdl_url)


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="estudiantes"
)

@app.route('/student_photo/<int:student_id>')
def get_student_photo(student_id):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT foto FROM estudiantes WHERE id = %s", (student_id,))
        student_photo = cursor.fetchone()
        if student_photo:
            return send_file(BytesIO(student_photo[0]), mimetype='image/png')
        else:
            return 'Foto no encontrada', 404
    except mysql.connector.Error as e:
        print(f"Error al obtener la foto del estudiante: {e}")
        return 'Error al obtener la foto del estudiante', 500


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_student', methods=['POST'])
def create_student():
    nombre = request.form['nombre']
    edad = int(request.form['edad'])
    carrera = request.form['carrera']
    semestre = int(request.form['semestre'])
    foto = request.files['foto'].read()
    
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO estudiantes (nombre, edad, carrera, semestre, foto) VALUES (%s, %s, %s, %s, %s)",
                       (nombre, edad, carrera, semestre, foto))
        conn.commit()
        return render_template('creado_conf.html')
    except mysql.connector.Error as e:
        print(f"Error al crear estudiante: {e}")
        return 'Error al crear el estudiante', 500

@app.route('/get_students')
def get_students():
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM estudiantes")
        students = cursor.fetchall()
        return render_template('students.html', students=students)
    except mysql.connector.Error as e:
        print(f"Error al obtener estudiantes: {e}")
        return 'Error al obtener estudiantes', 500

@app.route('/update_student/<int:id>', methods=['GET', 'POST'])
def update_student(id):
    # Refrescar la conexión a la base de datos
    try:
        conn.ping(reconnect=True)
    except mysql.connector.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return 'Error al conectar a la base de datos', 500

    if request.method == 'GET':
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM estudiantes WHERE id = %s", (id,))
            student = cursor.fetchone()
            return render_template('update_student.html', student=student)
        except mysql.connector.Error as e:
            print(f"Error al obtener estudiante: {e}")
            return 'Error al obtener estudiante', 500
    else:
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        carrera = request.form['carrera']
        semestre = int(request.form['semestre'])
        foto = request.files['foto'].read()
        
        try:
            cursor = conn.cursor()
            cursor.execute("UPDATE estudiantes SET nombre = %s, edad = %s, carrera = %s, semestre = %s, foto = %s WHERE id = %s",
                           (nombre, edad, carrera, semestre, foto, id))
            conn.commit()
            return render_template('act_conf.html')
        except mysql.connector.Error as e:
            print(f"Error al actualizar estudiante: {e}")
            return 'Error al actualizar el estudiante', 500

@app.route('/delete_student/<int:id>', methods=['POST'])
def delete_student(id):
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM estudiantes WHERE id = %s", (id,))
        conn.commit()
        return render_template('del_conf.html')
    except mysql.connector.Error as e:
        print(f"Error al eliminar estudiante: {e}")
        return 'Error al eliminar el estudiante', 500

if __name__ == '__main__':
    app.run(debug=True)
