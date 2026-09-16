#TP 07
#1
print("ejericcio 1")
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 
precios_frutas['Naranja']=1200
precios_frutas['Manzana']=1500
precios_frutas['Pera']=1200
print(precios_frutas)
#2
print("ejercicio 2")
precios_frutas['Banana']=1330
precios_frutas['Manzana']=1700
precios_frutas['Melón']=2800
print(precios_frutas)
#3
print("ejercicio 3")
print(precios_frutas.keys())
#4
print("ejercicio 4")
contactos={}
for i in range(5):
    name=input(print("Ingrese un nombre (0 para salir): "))

    if name == "0":
        break

    phone=input(print(f"Ingrese el numero de {name}: "))
    contactos[name]=phone
    

print(contactos)
#5
print("ejericio 5")
frase=input("Ingrese una frase: ")
palabras=frase.split() #separo las palabras
palabras_unicas=set(palabras) #set no permite duplicados, asi que puedo guardar las palabras unicas ahi
recuento={} #declaro el dicc

for palabra in palabras: #recorro palabras, if ya esta la sumo en 1 else palabra=1
    if palabra in recuento:
        recuento[palabra]+=1
    else:
        recuento[palabra]=1

print(f"Palabnras unicas: {palabras_unicas}")
print(f"Recuento de palabras: {recuento}")
#6
print("ejercicio 6")
alumnos={}
for i in range(3):

    nombre=input("Ingrese el nombre del alumno (o 0 para salir): ")
    if nombre == "0":
            break
    nota1=input(f"Nota n°1 de {nombre}: ")
    nota2=input(f"Nota n°2 de {nombre}: ")
    nota3=input(f"Nota n°3 de {nombre}: ")

    alumnos[nombre]=(nota1,nota2,nota3)

print(alumnos)
#7
print("ejercico 7")
parcial1={9,3,2,5,6}
parcial2={1,4,7,8,0}

ambos=parcial1 & parcial2
solo_uno=parcial1 ^ parcial2
total=parcial1 | parcial2

print(f"Aprobaron ambos parciales: {ambos}")
print(f"Aprobaron solo uno: {solo_uno}")
print(f"Aprobaron al menos un parcial: {total}")
#8
print("ejercicio 8")
tienda = {
    "chicle": 10,
    "chupetin": 8,
    "caramelos": 5,
}

while True:

    print("""
Bienvenido al sistema oprima una opcion:
1.Ver tienda
2.Consultar stock de producto
3.Agregar unidades
4.Agregar producto
5.Salir
""")

    option = int(input("Ingrese un numero: "))

    if option == 1:
        print(tienda)

    elif option == 2:
        producto = input("Ingrese el producto a consultar: ")

        if producto in tienda:
            print(tienda[producto])
        else:
            print("El producto no existe")

    elif option == 3:
        producto = input("¿A que producto desea sumar unidades?: ")

        if producto in tienda:
            unidades = int(input("¿Cuantas unidades desea agregar?: "))
            tienda[producto] += unidades
            print(tienda)
        else:
            print("El producto no existe")

    elif option == 4:
        producto = input("Ingrese el nuevo producto: ")

        if producto not in tienda:
            unidades = int(input("Ingrese el stock inicial: "))
            tienda[producto] = unidades
            print(tienda)
        else:
            print("El producto ya existe")

    elif option == 5:
        print("Saliendo del sistema...")
        break

#9
print("ejercicio 9")

agenda = {
    ("lunes", "10:00"): "Reunion",
    ("martes", "15:00"): "Clase de ingles",
    ("viernes", "18:00"): "Gimnasio"
}

dia = input("Ingrese el dia: ")
hora = input("Ingrese la hora: ")

consulta = (dia, hora)

if consulta in agenda:
    print(f"Actividad: {agenda[consulta]}")
else:
    print("No hay ninguna actividad en ese dia y horario")

#10
print("ejercicio 10")

original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Peru": "Lima"
}

invertido = {}

for pais in original:
    capital = original[pais]
    invertido[capital] = pais

print(invertido)