"TP Funciones"
#1
print("ejercicio 1")
def imprimir_hola_mundo():
    print("Hola mundo!")
imprimir_hola_mundo()
#2
print("ejercicio 2")
def saludar_usuario(nombre):
    print(f"Hola {nombre}")
saludar_usuario("leandro paredes")
#3
print("ejercicio 3")
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
nombre=input("Ingrese su nombre: ")
apellido=input("Ingrese su apellido: ")
edad=input("ingrese su edad: ")
residencia=input("ingrese su resindenica: ")
#4
print("ejercicio 4")
pi=3.1416
def calcular_area_circulo(radio):
    print(pi*radio**2)
def calcular_perimetro_circulo(radio):
    print(pi*radio*2)
radio=float(input("Ingrese el radio: "))
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)
#5
print("ejercicio 5")
segundos=float(input("Ingrese la cantidad de segundos: "))
def segundos_a_horas(segundos):
    horas=segundos/3600
    print(f"cantidad de hora/s: {horas}")
segundos_a_horas(segundos)
#6
print("ejercicio 6")
def tabla_multiplicar(numero):
    for i in range(1,11):
        resultado=numero*i
        print(resultado)
numero=int(input("Ingresa un nuemor del 1 al 10: "))
tabla_multiplicar(numero)
#7
print("eje4rciio 7")
def operaciones_basicas(a,b):
    suma=a+b
    resta=a-b
    multiplicacion=a*b
    division=a/b
    print(f"suma: {suma}")
    print(f"resta: {resta}")
    print(f"multiplicacion: {multiplicacion}")
    print(f"division: {division}")
a=float(input("Ingrese el primer numero: "))
b=float(input("Ingrese el segundo numero: "))
operaciones_basicas(a,b)
#8
print("ejercicio 8")
def celcius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print(fahrenheit) 
    return fahrenheit
celsius=float(input("Ingrese los grados celsius: "))
celcius_a_fahrenheit(celsius)
#9
print("ejercicio 9")
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
resultado = calcular_imc(peso, altura)
print(f"Su IMC es: {resultado:.2f}")
#10
print("ejercicio 10")
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))
resultado = calcular_promedio(a, b, c)
print(f"El promedio es: {resultado}")