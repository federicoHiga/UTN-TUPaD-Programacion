import numpy as np
#TP LISTA DIMENCIONAL
#10
print("ejercicio 10")
num10=list(map(int,input("Ingrese numeros separados por espacios: ").split()))
index=int(input("Ingrese el indice que desea eliminar: "))
num10.pop(index)
print(num10)
#11
print("ejercicio 11")
nums11=list(map(int,input("Ingrese numeros separados por espacios: ").split()))
num11=int(input("Ingrese el numero que desea contar: "))
quantity=nums11.count(num11)
print(f"El numero {num11} aparece {quantity} veces")
#12
print("ejercicio 12")
list_a_12=list(map(int,input("Ingrese los numeros de la primera lista: ").split()))
list_b_12=list(map(int,input("Ingrese los numeros de la segunda lista: ").split()))
result=[]
for i in range(len(list_a_12)):
    result.append(list_a_12[i]+list_b_12[i])
print(result)
#13
print("ejercicio 13")
# NumPy es una librería de Python utilizada para trabajar con datos numéricos, arrays y matrices.
# Permite realizar operaciones matemáticas sobre todos los elementos de un array de manera sencilla.
# También permite crear matrices de varias dimensiones, acceder a sus elementos y realizar operaciones como sumas, multiplicaciones y otros cálculos matemáticos.

#arrays con numpy
numbers13=np.array([10,20,30,40])
print(numbers13)
result13=numbers13*2
print(result13)

#matrices con numpy
matriz13=np.array([
    [1,2,3],
    [4,5,6]
])
print(matriz13)
#acceso
print(matriz13[0][1])

#suma de matrices
matriz_b_13=np.array([
    [5,6],
    [7,8]
])
result13=matriz13+matriz_b_13
print(result13)


