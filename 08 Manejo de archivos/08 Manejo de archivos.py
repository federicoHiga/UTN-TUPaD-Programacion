#1
with open("productos.txt","w") as archivo:

    archivo.write("Lapicera,$120.5,5\n")
    archivo.write("Cuaderno,$1000,10\n")
    archivo.write("Lapiz,$100,9\n")
    
#2
with open("productos.txt", "r") as archivo:

    for linea in archivo:
        linea=linea.strip()
        linea=linea.split(",")
        print(linea)
#3
with open("productos.txt", "a") as archivo:

    nombre=input("Ingrese el nombre: ").capitalize()
    precio=input("Ingrese el precio: ")
    cantidad=input("Ingrese la cantidad: ")

    archivo.write(f"{nombre},${precio},{cantidad}\n")

print("Producto guardado")

#4
productos=[]

with open("productos.txt", "r") as archivo:

    for linea in archivo:
        linea=linea.strip()
        linea=linea.split(",")
        datos={
            "nombre":linea[0],
            "precio":linea[1],
            "cantidad":linea[2]
        }
        productos.append(datos)

for i in productos:        
    print(i)

#5

while (True):

    filtro=input("Que producto desea buscar? (oprima x para salir): ").capitalize()

    if filtro =="X":
        break

    encontrado = False

    for i in productos:
        if filtro == i["nombre"]:
            print(i)
            encontrado = True

    if encontrado == False:
        print("Producto no encontrado")

#6

with open ("productos.txt", "w") as archivo:
    for i in productos:
        archivo.write(f"{i['nombre']},{i['precio']},{i['cantidad']}\n")

with open("productos.txt", "r") as archivo:

    for linea in archivo:
        linea=linea.strip()
        linea=linea.split(",")
        print(linea)



