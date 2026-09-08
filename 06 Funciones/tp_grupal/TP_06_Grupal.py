#1
print("ejercicio 1")
def calcular_factura_final(monto_base: float, impuesto: float = 21.0, descuento: float = 0.0, envio_prioritario: float | None = None) -> float:
    # 1. Calculamos el monto aplicando el descuento
    subtotal = monto_base * (1 - descuento / 100)
    
    # 2. Aplicamos el impuesto sobre el subtotal descontado
    total = subtotal * (1 + impuesto / 100)
    
    # 3. Si se especificó un envío prioritario (no es None), lo sumamos al total
    if envio_prioritario is not None:
        total = total + envio_prioritario
    
    # 4. Retornamos el resultado final redondeado a 2 decimales
    return round(total, 2)

# --- PRUEBAS OBLIGATORIAS ---
print(calcular_factura_final(1000.0))
print(calcular_factura_final(1000.0, descuento=10.0))
print(calcular_factura_final(1000.0, impuesto=10.0, descuento=5.0, envio_prioritario=150.0))
################################################################################################
#2
print("ejercicio 2")
class ValidadorFinanciero:
    #Utilidades financieras que no necesitan crear objetos.

    @staticmethod
    def es_cuit_valido(cuit: str) -> bool:
        #Devuelve True si el CUIT tiene exactamente 11 dígitos numéricos.
        return len(cuit) == 11 and cuit.isdigit()

    @staticmethod
    def convertir_moneda(monto: float, tasa_cambio: float, comision: float = 0.02) -> float:
        #Convierte un monto y descuenta la comisión indicada.
        return monto * tasa_cambio * (1 - comision)

# Pruebas obligatorias: se llama a la clase, sin crear instancias con ().
print(ValidadorFinanciero.es_cuit_valido("20384920194"))  # True
print(ValidadorFinanciero.es_cuit_valido("20-38492019-4"))  # False
print(ValidadorFinanciero.convertir_moneda(100.0, 1000.0, comision=0.05))  # 95000.0
################################################################################################
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
################################################################################################
#4
print("ejercicio 4")
#modulo: str: Es un parámetro posicional obligatorio. Se utiliza .upper() para garantizar que siempre se formatee en mayúsculas.
#*mensajes: str (*args): Recibe una cantidad variable de argumentos no nombrados (posicionales) en forma de tupla. 
# Usamos enumerate(mensajes, start=1) para numerar cada línea secuencialmente a partir de [1].
def generar_auditoria_sistema(modulo: str, *mensajes: str, **metadatos) -> str:
    lineas = []

    
    # 1. Módulo en mayúsculas
    lineas.append(f"MÓDULO: {modulo.upper()}")
    
    # 2. Procesamiento y numeración de mensajes (*args)
    lineas.append("MENSAJES:")
    if mensajes:
        for i, mensaje in enumerate(mensajes, start=1):
            lineas.append(f"  [{i}] {mensaje}")
    else:
        lineas.append("  (Sin mensajes)")

    #**metadatos (**kwargs): Recibe una cantidad variable de argumentos nombrados (clave-valor) en forma de diccionario. 
    # Recorremos sus ítems convirtiendo la clave a mayúsculas y formateándola como CLAVE: VALOR.   
    # 3. Desglose de metadatos (**kwargs)
    lineas.append("METADATOS:")
    if metadatos:
        for clave, valor in metadatos.items():
            lineas.append(f"  {clave.upper()}: {valor}")
    else:
        lineas.append("  (Sin metadatos)")
        
    # Unión de todas las lineas en un reporte multi-linea
    return "\n".join(lineas)


# ==========================================
# PRUEBA REQUERIDA
# ==========================================
if __name__ == "__main__":
    log = generar_auditoria_sistema(
        "AUTH", 
        "Intento fallido", 
        "Bloqueo de IP", 
        usuario="admin", 
        ip="192.168.1.10"
    )
    
    print(log)