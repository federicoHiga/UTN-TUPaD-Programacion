from Habitacion import Habitacion
from Vivienda import Vivienda
from Barrio import Barrio


class PruebaBarrio:
    @staticmethod
    def main():
        print("EJERCICIO 5")

        barrio = Barrio("Los Olivos", "Constructora del Sol")

        vivienda1 = Vivienda("San Martín", 100, "A", 1, 200)
        vivienda1.habitaciones.append(Habitacion("Cocina", 15))
        vivienda1.habitaciones.append(Habitacion("Dormitorio", 40))

        vivienda2 = Vivienda("San Martín", 120, "A", 2, 250)
        vivienda2.habitaciones.append(Habitacion("Living", 45))
        vivienda2.habitaciones.append(Habitacion("Dormitorio", 20))

        vivienda3 = Vivienda("Belgrano", 300, "B", 3, 300)
        vivienda3.habitaciones.append(Habitacion("Living", 50))
        vivienda3.habitaciones.append(Habitacion("Dormitorio", 25))

        barrio.viviendas.append(vivienda1)
        barrio.viviendas.append(vivienda2)
        barrio.viviendas.append(vivienda3)

        print(f"Barrio: {barrio.nombre}")
        print(f"Empresa constructora: {barrio.empresaConstructora}")
        print(f"Superficie total de terreno: {barrio.getSuperficieTotalTerreno()} m²")
        print(f"Superficie de terreno de manzana A: {barrio.getSuperficieTotalTerrenoXManzana('A')} m²")
        print(f"Superficie cubierta de vivienda 1: {vivienda1.getMetrosCuadradosCubiertos()} m²")
        print(f"Superficie cubierta total del barrio: {barrio.getSuperficieTotalCubierta()} m²")

        # Comprobación de la excepción que pide la consigna.
        viviendaIncorrecta = Vivienda("Mitre", 50, "C", 4, 20)
        viviendaIncorrecta.habitaciones.append(Habitacion("Habitación", 25))
        try:
            viviendaIncorrecta.getMetrosCuadradosCubiertos()
        except ValueError as error:
            print(f"Validación: {error}")


if __name__ == "__main__":
    PruebaBarrio.main()
