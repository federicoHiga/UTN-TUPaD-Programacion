from ComponenteCPU import ComponenteCPU
from Computadora import Computadora


class CostoComputadora:
    @staticmethod
    def main():
        print("EJERCICIO 4")

        while True:
            print("\nCOTIZAR COMPUTADORA")
            marca = input("Marca de la computadora: ")
            modelo = input("Modelo: ")
            computadora = Computadora(marca, modelo)

            while True:
                componente = input("Nombre del componente: ")
                marcaComponente = input("Marca del componente: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio por unidad: "))
                nuevoComponente = ComponenteCPU(componente, marcaComponente, cantidad, precio)
                computadora.componentesCPU.append(nuevoComponente)

                salirComponentes = input("¿Terminó de cargar componentes? (SI/NO): ").upper()
                if salirComponentes == "SI":
                    break

            costo = computadora.calcularCosto()

            # El enunciado no aclara el caso de exactamente $50.000.
            # Aquí se aplica el 30% cuando el costo es igual a $50.000.
            if costo < 50000:
                ganancia = costo * 0.40
            else:
                ganancia = costo * 0.30
            precioVenta = costo + ganancia

            print("\n-----------COMPUTADORA------------")
            print(f"Marca: {computadora.marca}")
            print(f"Modelo: {computadora.modelo}")
            print("Componente | Marca | Cantidad | Precio por unidad | Subtotal")
            for elemento in computadora.componentesCPU:
                subtotal = elemento.cantidad * elemento.precio
                print(f"{elemento.componente} | {elemento.marca} | {elemento.cantidad} | ${elemento.precio:.2f} | ${subtotal:.2f}")

            print(f"Costo total: ${costo:.2f}")
            print(f"Ganancia: ${ganancia:.2f}")
            print(f"Precio sugerido de venta: ${precioVenta:.2f}")

            continuar = input("\n¿Desea cotizar otra computadora? (SI/NO): ").upper()
            if continuar != "SI":
                break


if __name__ == "__main__":
    CostoComputadora.main()
