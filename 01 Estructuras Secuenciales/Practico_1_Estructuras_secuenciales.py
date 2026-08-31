"""Práctico 1: Estructuras secuenciales"""
#1
print("ejercicio 1")
print("Hola Mundo!")
#2
print("ejercicio 2")
name=input("Ingrese su nombre: ")
print(f"Hola {name}!")
#3
print("ejercicio 3")
lastName=input("Ingrese su apellido: ")
age=input("Ingrese su edad: ")
country=input("Ingrese pais de residencia: ")
print(f"Soy {name} {lastName}, tengo {age} y vivo en {country} ")
#4
print("ejercicio 4")
radius="Ingrese el radio de su circulo: "
pi=3.14
area=pi*radius*2
perimeter=2*pi*radius
print(f"El area es {area} y el perimetro es {perimeter}")
#5
print("ejercicio 5")
seconds=float(input("Ingrese una cantidad de segundos: "))
hours=seconds/3600
print(f"{seconds} segundos equivalen a {hours} horas")
#6
print("ejercicio 6")
number=int(input("Ingrese un numero: "))
print(f"{number} x 1 = {number*1}")
print(f"{number} x 2 = {number*2}")
print(f"{number} x 3 = {number*3}")
print(f"{number} x 4 = {number*4}")
print(f"{number} x 5 = {number*5}")
print(f"{number} x 6 = {number*6}")
print(f"{number} x 7 = {number*7}")
print(f"{number} x 8 = {number*8}")
print(f"{number} x 9 = {number*9}")
print(f"{number} x 10 = {number*10}")
#7
print("ejercicio 7")
number1=int(input("Ingrese el primer numero: "))
number2=int(input("Ingrese el segundo numero: "))
suma=number1+number2
division=number1/number2
multiplicacion=number1*number2
resta=number1-number2
print(f"Suma: {suma}, division: {division}, multiplicacion: {multiplicacion}, resta: {resta}")
#8
print("ejercicio 8")
height=float(input("Ingrese su altura en metros: "))
weight=float(input("Ingrese su peso en kg: "))
imc=weight/height**2
print(f"Su indice de masa corporal es {imc}")
#9
print("ejercicio 9")
celsius=float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit=9/5*celsius+32
print(f"{celsius} grados Celsius equivalen a {fahrenheit} grados Fahrenheit")
#10
print("ejercicio 10")
num1=float(input("Ingrese el primer numero: "))
num2=float(input("Ingrese el segundo numero: "))
num3=float(input("Ingrese el tercer numero: "))
promedio=(num1+num2+num3)/3
print(f"El promedio de los tres numeros es {promedio}")