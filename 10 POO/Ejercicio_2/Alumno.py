class Alumno:
    def __init__(self, nombreCompleto, legajo):
        self.nombreCompleto = nombreCompleto
        self.legajo = legajo
        self.notas = []

    def calcularPromedio(self):
        suma = 0
        for nota in self.notas:
            suma += nota.notaExamen
        if len(self.notas) > 0:
            return suma / len(self.notas)
        return 0
