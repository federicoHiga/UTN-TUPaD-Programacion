import requests

url = "http://127.0.0.1:5000/api"


def mostrar_resultado(nombre, respuesta):
    print(f"\n{nombre} - Codigo: {respuesta.status_code}")
    print(respuesta.json())


def probar_api():
    try:
        # 1. Consultar los libros
        respuesta = requests.get(f"{url}/libros", timeout=5)
        mostrar_resultado("GET libros", respuesta)

        # 2. Crear un autor
        datos_autor = {"nombre": "Julio Cortazar", "nacionalidad": "Argentina"}
        respuesta = requests.post(f"{url}/autores", json=datos_autor, timeout=5)
        mostrar_resultado("POST autor", respuesta)
        if respuesta.status_code != 201:
            return
        id_autor = respuesta.json()["id"]

        # Crear un libro con ese autor
        datos_libro = {"titulo": "Rayuela", "anio": 1963, "autor_id": id_autor}
        respuesta = requests.post(f"{url}/libros", json=datos_libro, timeout=5)
        mostrar_resultado("POST libro", respuesta)
        if respuesta.status_code != 201:
            return
        id_libro = respuesta.json()["id"]

        # 3. Modificar el titulo del libro
        respuesta = requests.put(
            f"{url}/libros/{id_libro}", json={"titulo": "Rayuela actualizado"}, timeout=5
        )
        mostrar_resultado("PUT libro", respuesta)

        # 4. Eliminar el libro
        respuesta = requests.delete(f"{url}/libros/{id_libro}", timeout=5)
        mostrar_resultado("DELETE libro", respuesta)
        if respuesta.status_code == 200 and respuesta.json().get("mensaje"):
            print("La eliminacion fue confirmada")

        # Comprobar que el libro ya no existe
        respuesta = requests.get(f"{url}/libros/{id_libro}", timeout=5)
        mostrar_resultado("GET libro eliminado", respuesta)
        if respuesta.status_code == 404:
            print("El libro ya no existe en la base")

    except requests.exceptions.RequestException:
        print("No se pudo conectar con la API. Primero hay que ejecutar app.py")


if __name__ == "__main__":
    probar_api()
