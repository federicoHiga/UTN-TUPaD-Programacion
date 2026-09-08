#3: Interaccion inter clase, metodos de instancia y delegacion
print("Ejercicio 3")

class Notificador:
    def enviar_recibo(self, cliente:str, total:float) -> None:
        print(f"Cliente: {cliente}")
        print(f"Total cobrado: ${total}")

class ProcesadorPagos:
    def __init__(self):
        self.notificador=Notificador()

    def procesar_transaccion(
        self,
        cliente:str,
        items:list[dict],
        descuento_cupon:float=0.0
    ) -> float:
        
        total=0

        for item in items:
            total+=item["precio"]

        total=total-descuento_cupon

        self.notificador.enviar_recibo(cliente, total)

        return total

carrito = [
    {"nombre": "Teclado", "precio": 50.0},
    {"nombre": "Mouse", "precio": 30.0}
]

procesador=ProcesadorPagos()

procesador.procesar_transaccion(
    "Ana Gomez",
    carrito,
    descuento_cupon=10.0
)