import random
#1
print("ejercicio 1")
for i in range(101):
    if i == 101: break
    print(i)
#2
print("ejercicio 2")
n2=int(input("Ingrese un numero entero: "))
print(f"El numero ingresado tiene {len(str(n2))} digitos")
#3
print("ejercicio 3")
valor1=int(input("Ingrese valor entero numero 1: "))
valor2=int(input("Ingrese valor entero numero 2: "))
suma=0
for i in range(valor1-1,valor2+1):
    suma+=i
    print(suma)
#4
print("ejercicio 4")
suma=0
while True:
    n4=int(input("Ingrese numeros enteros (oprima 0 para finalizar): "))
    if n4==0:
        print(f"A finalizado el programa, el total es: {suma}")
        break
    suma+=n4
#5
print("ejercicio 5")
var5=random.randint(0,9)
intentos=0
while True:
    n5=int(input("Adivina el numero: "))
    intentos+=1
    if n5==var5:
        print("GANASTE!")
        print(f"Tus intentos fueron: {intentos}")
        var5=random.randint(0,9)
        break
#6
print("ejercicio 6")
for i in range(100,0,-2):
    print(i)
#7
print("ejericico 7")
suma7=0
n7=int(input("Ingrese un entero positivo: "))
for i in range(0,n7+1):
    suma7+=i
print(suma7)
#8
print("ejercicio 8")
pares=0
impares=0
negativos=0
positivos=0

for i in range(4):
    n8=int(input("Ingrese numeros enteros: "))
    if n8%2==0:
        pares+=1
    else:
        impares+=1
    if n8>0 and n8!=0:
        positivos+=1
    elif n8<0 and n8!=0:
        negativos+=1
print(f"pares: {pares}")
print(f"impares: {impares}")
print(f"positivos: {positivos}")
print(f"negativos: {negativos}")
#9
print("ejericico 9")
rangoMaximo=4
suma9=0
for i in range(rangoMaximo):
    n9=int(input("Ingrese numeros enteros: "))
    suma9+=n9
media=suma9/rangoMaximo
print(f"La media es {media}")
#10
print("ejericico 10")
n10=int(input("Ingrese un numero: "))
print(str(n10)[::-1])