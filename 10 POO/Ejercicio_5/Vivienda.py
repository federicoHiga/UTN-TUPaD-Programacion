class Vivienda:
    def __init__(self, calle, numero, manzana, nroCasa, superficieTerreno):
        self.calle = calle
        self.numero = numero
        self.manzana = manzana
        self.nroCasa = nroCasa
        self.superficieTerreno = superficieTerreno
        self.habitaciones = []

    def getMetrosCuadradosCubiertos(self):
        total = 0
        for habitacion in self.habitaciones:
            total += habitacion.metrosCuadrados

        if total > self.superficieTerreno:
            raise ValueError("La superficie cubierta no puede ser mayor a la superficie del terreno")

        return total
