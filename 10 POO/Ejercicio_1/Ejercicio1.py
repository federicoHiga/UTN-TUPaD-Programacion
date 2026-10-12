# Ejercicio 1 - Celdas y matriz

class Celda:
    def __init__(self, fila, columna, valor):
        self.fila = fila
        self.columna = columna
        self.valor = valor


class Matriz:
    def __init__(self):
        self.celdasMatriz = []

    def agregarCelda(self, celda):
        for celdaGuardada in self.celdasMatriz:
            if celdaGuardada.fila == celda.fila and celdaGuardada.columna == celda.columna:
                return False
        self.celdasMatriz.append(celda)
        return True

    def mostrarCeldas(self):
        print("\nCELDAS CARGADAS")
        for celda in self.celdasMatriz:
            print(f"Fila: {celda.fila} - Columna: {celda.columna} - Valor: {celda.valor}")

    def obtenerValor(self, fila, columna):
        for celda in self.celdasMatriz:
            if celda.fila == fila and celda.columna == columna:
                return celda.valor
        return "La fila y columna indicada no ha sido asignada en ninguna celda"


if __name__ == "__main__":
    print("EJERCICIO 1")
    matriz = Matriz()

    while True:
        valor = input("Ingrese el valor de la celda (FIN para terminar): ")
        if valor == "FIN":
            break

        fila = int(input("Ingrese la fila: "))
        columna = int(input("Ingrese la columna: "))
        celda = Celda(fila, columna, valor)

        if matriz.agregarCelda(celda):
            print("Celda agregada.")
        else:
            print("Esa fila y columna ya tienen una celda cargada.")

    matriz.mostrarCeldas()

    if len(matriz.celdasMatriz) > 0:
        print("\nBUSCAR VALOR")
        fila = int(input("Ingrese la fila a buscar: "))
        columna = int(input("Ingrese la columna a buscar: "))
        print(matriz.obtenerValor(fila, columna))
