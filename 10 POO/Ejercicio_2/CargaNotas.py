from Nota import Nota
from Alumno import Alumno


class CargaNotas:
    @staticmethod
    def main():
        print("EJERCICIO 2")
        alumnos = []

        while True:
            print("\nINGRESE DATOS DEL ALUMNO")
            nombreCompleto = input("Nombre completo: ")
            legajo = int(input("Legajo: "))
            alumno = Alumno(nombreCompleto, legajo)

            # Este ciclo carga al menos una nota por alumno.
            while True:
                catedra = input("Nombre de la cátedra: ")
                notaExamen = float(input("Nota del examen: "))
                nota = Nota(catedra, notaExamen)
                alumno.notas.append(nota)

                salirNotas = input("¿Desea terminar la carga de notas? (SI/NO): ").upper()
                if salirNotas == "SI":
                    break

            alumnos.append(alumno)
            salirAlumnos = input("¿Desea terminar la carga de alumnos? (SI/NO): ").upper()
            if salirAlumnos == "SI":
                break

        print("\nALUMNOS CARGADOS")
        for alumno in alumnos:
            print(f"\nNombre: {alumno.nombreCompleto}")
            print(f"Legajo: {alumno.legajo}")
            for nota in alumno.notas:
                print(f"Cátedra: {nota.catedra} - Nota: {nota.notaExamen}")
            print(f"Promedio: {alumno.calcularPromedio():.2f}")


if __name__ == "__main__":
    CargaNotas.main()
