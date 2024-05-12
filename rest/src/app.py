from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS

from config import config

app = Flask(__name__, template_folder="templates")
CORS(app, resources={r"/cursos/*": {"origins": "http://localhost"}})

conexion = MySQL(app)

# Rutas para mostrar formularios y operaciones CRUD de cursos
@app.route('/')
def index():
    cursos = obtener_cursos()
    mensaje = request.args.get('mensaje')  # Obtener el mensaje de la URL
    return render_template('index.html', cursos=cursos, mensaje=mensaje)

@app.route('/curso/agregar')
def mostrar_formulario_registro():
    return render_template('registro_curso.html')

@app.route('/cursos/<codigo>/editar')
def mostrar_formulario_edicion(codigo):
    curso = leer_curso_bd(codigo)
    if curso is not None:
        return render_template('edicion_curso.html', curso=curso)
    else:
        return jsonify({'mensaje': "Curso no encontrado.", 'exito': False})

@app.route('/cursos/eliminar/<codigo>/eliminar')
def mostrar_formulario_eliminar(codigo):
    try:
        curso = leer_curso_bd(codigo)
        if curso is not None:
            return render_template('eliminar_curso.html', curso=curso)
        else:
            return jsonify({'mensaje': "Curso no encontrado.", 'exito': False})
    except Exception as ex:
        print("Error:", ex)
        return jsonify({'mensaje': "Error", 'exito': False})

# Funciones para operaciones CRUD de cursos
def obtener_cursos():
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT codigo, nombre, creditos FROM curso ORDER BY nombre ASC"
        cursor.execute(sql)
        datos = cursor.fetchall()
        cursos = []
        for fila in datos:
            curso = {'codigo': fila[0], 'nombre': fila[1], 'creditos': fila[2]}
            cursos.append(curso)
        return cursos
    except Exception as ex:
        return None

@app.route('/cursos', methods=['GET'])
def listar_cursos():
    try:
        cursos = obtener_cursos()
        return jsonify({'cursos': cursos, 'mensaje': "Cursos listados.", 'exito': True})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})

def leer_curso_bd(codigo):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT codigo, nombre, creditos FROM curso WHERE codigo = '{0}'".format(codigo)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos is not None:
            curso = {'codigo': datos[0], 'nombre': datos[1], 'creditos': datos[2]}
            return curso
        else:
            return None
    except Exception as ex:
        raise ex

@app.route('/cursos/<codigo>', methods=['GET'])
def leer_curso(codigo):
    try:
        curso = leer_curso_bd(codigo)
        if curso is not None:
            return jsonify({'curso': curso, 'mensaje': "Curso encontrado.", 'exito': True})
        else:
            return jsonify({'mensaje': "Curso no encontrado.", 'exito': False})
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})

@app.route('/cursos', methods=['POST'])
def registrar_curso():    
    try:
        curso = leer_curso_bd(request.form['codigo'])
        if curso is not None:
            return jsonify({'mensaje': "Código ya existe, no se puede duplicar.", 'exito': False})
        else:
            cursor = conexion.connection.cursor()
            sql = """INSERT INTO curso (codigo, nombre, creditos) 
            VALUES ('{0}', '{1}', {2})""".format(request.form['codigo'], request.form['nombre'], request.form['creditos'])
            cursor.execute(sql)
            conexion.connection.commit()
            return redirect(url_for('index', mensaje='Curso registrado correctamente'))
    except Exception as ex:
        return jsonify({'mensaje': "Error", 'exito': False})

@app.route('/cursos/<codigo>', methods=['PUT', 'POST'])  # Permitir tanto POST como PUT
def actualizar_curso(codigo):
    if request.method == 'POST':
        try:
            curso = leer_curso_bd(codigo)
            if curso is not None:
                # Obtener los datos del formulario
                nombre = request.form.get('nombre')
                creditos = request.form.get('creditos')

                cursor = conexion.connection.cursor()
                sql = """UPDATE curso SET nombre = '{0}', creditos = {1} 
                WHERE codigo = '{2}'""".format(nombre, creditos, codigo)
                cursor.execute(sql)
                conexion.connection.commit()
                # Redirigir a la página principal con un mensaje en la URL
                return redirect(url_for('index', mensaje='Curso actualizado correctamente'))
            else:
                return jsonify({'mensaje': "Curso no encontrado.", 'exito': False})
        except Exception as ex:
            return jsonify({'mensaje': "Errors", 'exito': False})
    else:
        return "Método no permitido", 405  # Método no permitido para otras solicitudes que no sean POST

@app.route('/cursos/eliminar/<codigo>', methods=['DELETE', 'POST'])  # Permitir tanto DELETE como POST
def eliminar_curso(codigo):
    if request.method == 'POST':
        if request.form.get('_method') == 'DELETE':
            try:
                curso = leer_curso_bd(codigo)
                if curso is not None:
                    cursor = conexion.connection.cursor()
                    sql = "DELETE FROM curso WHERE codigo = '{0}'".format(codigo)
                    cursor.execute(sql)
                    conexion.connection.commit()
                    return redirect(url_for('index', mensaje='Curso eliminado correctamente'))
                else:
                    return jsonify({'mensaje': "Curso no encontrado.", 'exito': False})
            except Exception as ex:
                return jsonify({'mensaje': "Error", 'exito': False})
    else:
        return "Método no permitido", 405  # Devolver un error si no se utiliza DELETE

# Manejador de error para páginas no encontradas
def pagina_no_encontrada(error):
    return "<h1>Página no encontrada</h1>", 404

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(host='192.168.216.192')  # Escuchar en todas las interfaces de red
