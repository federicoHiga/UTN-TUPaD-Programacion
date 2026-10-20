import sqlite3


# Ejercicio 1: Modelado de clases (POO)
class Autor:
    def __init__(self, id_autor, nombre, nacionalidad):
        self.id_autor = id_autor
        self.nombre = nombre
        self.nacionalidad = nacionalidad

    def __str__(self):
        return f"Autor {self.id_autor}: {self.nombre} ({self.nacionalidad})"


class Libro:
    def __init__(self, id_libro, titulo, anio_publicacion, autor):
        self.id_libro = id_libro
        self.titulo = titulo
        self.anio_publicacion = anio_publicacion
        self.autor = autor  # Un objeto de la clase Autor

    def __str__(self):
        return f"Libro {self.id_libro}: {self.titulo} ({self.anio_publicacion}) - {self.autor.nombre}"


# Conexion a base
# Se habilitan las claves foraneas para que la relacion se respete.
def conectar():
    conexion = sqlite3.connect("biblioteca.db")
    conexion.execute("PRAGMA foreign_keys = ON")
    return conexion


# Ejercicio 2: Creacion de la base de datos
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


# Ejercicio 3: Funciones CRUD
def registrar_autor(nombre, nacionalidad):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO autores (nombre, nacionalidad) VALUES (?, ?)",
        (nombre, nacionalidad)
    )
    id_autor = cursor.lastrowid
    conexion.commit()
    conexion.close()
    return id_autor


def registrar_libro(titulo, anio, autor_id):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO libros (titulo, anio, autor_id) VALUES (?, ?, ?)",
        (titulo, anio, autor_id)
    )
    id_libro = cursor.lastrowid
    conexion.commit()
    conexion.close()
    return id_libro


def listar_libros():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT libros.id, libros.titulo, libros.anio, autores.nombre
        FROM libros
        JOIN autores ON libros.autor_id = autores.id
        ORDER BY libros.id
    """)
    libros = cursor.fetchall()
    conexion.close()

    if not libros:
        print("No hay libros registrados.")
    else:
        for id_libro, titulo, anio, nombre_autor in libros:
            print(f"ID: {id_libro} | Titulo: {titulo} | Año: {anio} | Autor: {nombre_autor}")


def actualizar_titulo_libro(id_libro, nuevo_titulo):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute(
        "UPDATE libros SET titulo = ? WHERE id = ?",
        (nuevo_titulo, id_libro)
    )
    conexion.commit()
    conexion.close()


def eliminar_libro(id_libro):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM libros WHERE id = ?", (id_libro,))
    conexion.commit()
    conexion.close()


# Ejercicio 4: prueba integral
if __name__ == "__main__":
    inicializar_base_datos()

    # Registramos 2 autores y creamos sus objetos.
    id_autor1 = registrar_autor("Julio Cortazar", "Argentina")
    id_autor2 = registrar_autor("Gabriel Garcia Marquez", "Colombia")
    autor1 = Autor(id_autor1, "Julio Cortazar", "Argentina")
    autor2 = Autor(id_autor2, "Gabriel Garcia Marquez", "Colombia")

    print("AUTORES REGISTRADOS")
    print(autor1)
    print(autor2)

    # Creamos 3 libros, cada uno relacionado con un objeto Autor.
    libro1 = Libro(None, "Rayuela", 1963, autor1)
    libro2 = Libro(None, "Bestiario", 1951, autor1)
    libro3 = Libro(None, "Cien años de soledad", 1967, autor2)

    libro1.id_libro = registrar_libro(libro1.titulo, libro1.anio_publicacion, libro1.autor.id_autor)
    libro2.id_libro = registrar_libro(libro2.titulo, libro2.anio_publicacion, libro2.autor.id_autor)
    libro3.id_libro = registrar_libro(libro3.titulo, libro3.anio_publicacion, libro3.autor.id_autor)

    print("\nEJEMPLO DE OBJETO LIBRO")
    print(libro1)

    print("\nLISTADO INICIAL DE LIBROS")
    listar_libros()

    actualizar_titulo_libro(libro1.id_libro, "Rayuela - Titulo actualizado")
    print("\nLISTADO DESPUES DE ACTUALIZAR UN TITULO")
    listar_libros()

    eliminar_libro(libro2.id_libro)
    print("\nLISTADO DESPUES DE ELIMINAR UN LIBRO")
    listar_libros()
