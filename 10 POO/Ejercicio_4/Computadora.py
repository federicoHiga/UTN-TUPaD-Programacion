class Computadora:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.componentesCPU = []

    def calcularCosto(self):
        total = 0
        for componente in self.componentesCPU:
            total += componente.cantidad * componente.precio
        return total
