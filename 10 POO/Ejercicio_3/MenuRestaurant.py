from Ingrediente import Ingrediente
from Plato import Plato


class MenuRestaurant:
    @staticmethod
    def main():
        print("EJERCICIO 3")
        platosMenu = []

        while True:
            print("\nCARGA DE PLATOS")
            nombreCompleto = input("Nombre del plato o bebida: ")
            precio = float(input("Precio: "))
            esBebida = input("¿Es bebida? (SI/NO): ").upper() == "SI"
            plato = Plato(nombreCompleto, precio, esBebida)

            if not plato.esBebida:
                # Se carga obligatoriamente al menos un ingrediente.
                while True:
                    nombre = input("Nombre del ingrediente: ")
                    cantidad = float(input("Cantidad: "))
                    unidadMedida = input("Unidad de medida: ")
                    ingrediente = Ingrediente(nombre, cantidad, unidadMedida)
                    plato.ingredientes.append(ingrediente)

                    salirIngredientes = input("¿Terminó de cargar ingredientes? (SI/NO): ").upper()
                    if salirIngredientes == "SI":
                        break

            platosMenu.append(plato)
            salirPlatos = input("¿Terminó de cargar platos? (SI/NO): ").upper()
            if salirPlatos == "SI":
                break

        print("\n-----------MENÚ----------------")
        for plato in platosMenu:
            print(plato.nombreCompleto)
            print(f"Precio: $ {plato.precio:.2f}")

            if not plato.esBebida:
                print("Ingredientes:")
                print("Nombre | Cantidad | Unidad de medida")
                for ingrediente in plato.ingredientes:
                    print(f"{ingrediente.nombre} | {ingrediente.cantidad:g} | {ingrediente.unidadMedida}")

            print("--------------------------------")


if __name__ == "__main__":
    MenuRestaurant.main()
