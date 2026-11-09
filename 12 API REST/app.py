import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)


# Ejercicio 1: clases y base de datos
class Autor:
    def __init__(self, id_autor, nombre, nacionalidad):
        self.id_autor = id_autor
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def a_diccionario(self):
        return {
            "id": self.id_autor,
            "nombre": self.nombre,
            "nacionalidad": self.nacionalidad
        }


class Libro:
    def __init__(self, id_libro, titulo, anio_publicacion, autor):
        self.id_libro = id_libro
        self.titulo = titulo
        self.anio_publicacion = anio_publicacion
        self.autor = autor

    def a_diccionario(self):
        return {
            "id": self.id_libro,
            "titulo": self.titulo,
            "anio": self.anio_publicacion,
            "autor_id": self.autor.id_autor,
            "autor": self.autor.a_diccionario()
        }


def conectar():
    conexion = sqlite3.connect("biblioteca.db")
    conexion.execute("PRAGMA foreign_keys = ON")
    return conexion


def inicializar_base_datos():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS autores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            nacionalidad TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS libros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            anio INTEGER NOT NULL,
            autor_id INTEGER NOT NULL,
            FOREIGN KEY (autor_id) REFERENCES autores(id)
        )
    """)

    conexion.commit()
    conexion.close()


def obtener_autores_db():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre, nacionalidad FROM autores")
    filas = cursor.fetchall()
    conexion.close()

    autores = []
    for fila in filas:
        autor = Autor(fila[0], fila[1], fila[2])
        autores.append(autor.a_diccionario())
    return autores


def obtener_autor_db(id_autor):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT id, nombre, nacionalidad FROM autores WHERE id = ?", (id_autor,))
    fila = cursor.fetchone()
    conexion.close()

    if fila is None:
        return None

    autor = Autor(fila[0], fila[1], fila[2])
    return autor.a_diccionario()


def insertar_autor_db(nombre, nacionalidad):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO autores (nombre, nacionalidad) VALUES (?, ?)",
        (nombre, nacionalidad)
    )
    id_autor = cursor.lastrowid
    conexion.commit()
    conexion.close()
    return obtener_autor_db(id_autor)


def convertir_libro(fila):
    autor = Autor(fila[3], fila[4], fila[5])
    libro = Libro(fila[0], fila[1], fila[2], autor)
    return libro.a_diccionario()


def obtener_libros_db():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT libros.id, libros.titulo, libros.anio,
               autores.id, autores.nombre, autores.nacionalidad
        FROM libros
        JOIN autores ON libros.autor_id = autores.id
        ORDER BY libros.id
    """)
    filas = cursor.fetchall()
    conexion.close()

    libros = []
    for fila in filas:
        libros.append(convertir_libro(fila))
    return libros


def obtener_libro_db(id_libro):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT libros.id, libros.titulo, libros.anio,
               autores.id, autores.nombre, autores.nacionalidad
        FROM libros
        JOIN autores ON libros.autor_id = autores.id
        WHERE libros.id = ?
    """, (id_libro,))
    fila = cursor.fetchone()
    conexion.close()

    if fila is None:
        return None
    return convertir_libro(fila)


def insertar_libro_db(titulo, anio, autor_id):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO libros (titulo, anio, autor_id) VALUES (?, ?, ?)",
        (titulo, anio, autor_id)
    )
    id_libro = cursor.lastrowid
    conexion.commit()
    conexion.close()
    return obtener_libro_db(id_libro)


def actualizar_libro_db(id_libro, titulo, anio, autor_id):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(
        "UPDATE libros SET titulo = ?, anio = ?, autor_id = ? WHERE id = ?",
        (titulo, anio, autor_id, id_libro)
    )
    conexion.commit()
    conexion.close()
    return obtener_libro_db(id_libro)


def eliminar_libro_db(id_libro):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM libros WHERE id = ?", (id_libro,))
    eliminado = cursor.rowcount
    conexion.commit()
    conexion.close()
    return eliminado


def validar_libro(datos):
    if not isinstance(datos, dict):
        return "Se debe enviar un JSON valido"
    if "titulo" not in datos or "anio" not in datos or "autor_id" not in datos:
        return "Faltan campos obligatorios"
    if not isinstance(datos["titulo"], str) or not datos["titulo"].strip():
        return "El titulo no es valido"
    if type(datos["anio"]) is not int or type(datos["autor_id"]) is not int:
        return "El anio y el autor_id deben ser numeros enteros"
    return None


# Ejercicio 2: rutas de la API
@app.route("/api/autores", methods=["GET"])
def listar_autores():
    return jsonify(obtener_autores_db()), 200


@app.route("/api/autores", methods=["POST"])
def crear_autor():
    datos = request.get_json(silent=True)

    if not isinstance(datos, dict) or not datos.get("nombre") or not datos.get("nacionalidad"):
        return jsonify({"error": "Faltan campos obligatorios"}), 400
    if not isinstance(datos["nombre"], str) or not isinstance(datos["nacionalidad"], str):
        return jsonify({"error": "Los datos deben ser texto"}), 400
    if not datos["nombre"].strip() or not datos["nacionalidad"].strip():
        return jsonify({"error": "Los datos no pueden estar vacios"}), 400

    autor = insertar_autor_db(datos["nombre"], datos["nacionalidad"])
    return jsonify(autor), 201


@app.route("/api/libros", methods=["GET"])
def listar_libros():
    return jsonify(obtener_libros_db()), 200


@app.route("/api/libros/<int:id_libro>", methods=["GET"])
def buscar_libro(id_libro):
    libro = obtener_libro_db(id_libro)
    if libro is None:
        return jsonify({"error": "Libro no encontrado"}), 404
    return jsonify(libro), 200


@app.route("/api/libros", methods=["POST"])
def crear_libro():
    datos = request.get_json(silent=True)
    error = validar_libro(datos)
    if error:
        return jsonify({"error": error}), 400

    if obtener_autor_db(datos["autor_id"]) is None:
        return jsonify({"error": "Autor no encontrado"}), 404

    libro = insertar_libro_db(datos["titulo"], datos["anio"], datos["autor_id"])
    return jsonify(libro), 201


@app.route("/api/libros/<int:id_libro>", methods=["PUT"])
def modificar_libro(id_libro):
    libro = obtener_libro_db(id_libro)
    if libro is None:
        return jsonify({"error": "Libro no encontrado"}), 404

    datos = request.get_json(silent=True)
    if not isinstance(datos, dict) or not datos:
        return jsonify({"error": "Faltan datos para modificar"}), 400

    # Si un campo no se envia, se mantiene el valor anterior
    nuevos_datos = {
        "titulo": datos.get("titulo", libro["titulo"]),
        "anio": datos.get("anio", libro["anio"]),
        "autor_id": datos.get("autor_id", libro["autor_id"])
    }
    error = validar_libro(nuevos_datos)
    if error:
        return jsonify({"error": error}), 400

    if obtener_autor_db(nuevos_datos["autor_id"]) is None:
        return jsonify({"error": "Autor no encontrado"}), 404

    libro_actualizado = actualizar_libro_db(
        id_libro, nuevos_datos["titulo"], nuevos_datos["anio"], nuevos_datos["autor_id"]
    )
    return jsonify(libro_actualizado), 200


@app.route("/api/libros/<int:id_libro>", methods=["DELETE"])
def borrar_libro(id_libro):
    if eliminar_libro_db(id_libro) == 0:
        return jsonify({"error": "Libro no encontrado"}), 404
    return jsonify({"mensaje": "Libro eliminado correctamente", "id": id_libro}), 200


inicializar_base_datos()

if __name__ == "__main__":
    app.run(debug=True)
