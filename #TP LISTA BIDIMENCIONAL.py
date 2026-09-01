#TP LISTA BIDIMENCIONAL
import numpy as np
#10
print("ejercicio 10")
matriz10=np.array([
    [1,2,3],
    [2,4,5],
    [3,5,6]
])
if np.array_equal(matriz10,matriz10.T):
    print("La matriz es simetrica")
else:
    print("La matriz es asimetrica")
#11
print("ejercicio 11")
matriz11=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
rotado=[]
for i in range(len(matriz11)):
    row=[]
    for j in range(len(matriz11)-1,-1,-1):
        row.append(matriz11[j][i])
    rotado.append(row)
print(rotado)
#12
print("ejercicio 12")
notasString="45, 88, -5, 92, 30, 110, 75, 60, 15"
notas=notasString.split(",")

aprobado=[]
reprobado=[]
notasValidas=[]

for notas in notas:
    notas=int(notas)
    if notas<0 or notas>100:
        continue
    notasValidas.append(notas)
    if notas>=60:
        aprobado.append(notas)
    else:
        reprobado.append(notas)

promedio=sum(notasValidas)/len(notasValidas)

print(f"Aprobados: {aprobado}")
print(f"Reprobados: {reprobado}")
print(f"Promedio: {promedio}")
print(f"Ultimos 2 aprobados: {aprobado[-2:]}")
#13
print("ejercicio 13")
tareas13=[]

while True:
    print("1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Ver resumen")
    print("4. Salir")

    opcion=input("Ingrese una opcion: ")

    if opcion=="1":
        tarea=input("Ingrese el nombre de la tarea: ")

        if tarea in tareas13:
            print("La tarea ya esta registrada")
        else:
            tareas13.append(tarea)
            print("Tarea agregada")

    elif opcion=="2":
        tarea=input("Ingrese el nombre de la tarea a eliminar: ")

        if tarea in tareas13:
            tareas13.remove(tarea)
            print("Tarea eliminada")
        else:
            print("La tarea no existe")

    elif opcion=="3":
        print(f"Total de tareas: {len(tareas13)}")
        print(f"Primeras 3 tareas: {tareas13[:3]}")

    elif opcion=="4":
        print("Programa finalizado")
        break

    else:
        print("Opcion invalida")