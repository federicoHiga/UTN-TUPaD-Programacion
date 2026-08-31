import statistics
import random
#1
print("ejercicio 1")
edad=int(input("Ingrese su edad:"))
validacion1=print("Es mayor de edad") if edad>=18 else print("No es mayor de dead")
#2
print("ejercicio 2")
nota=float(input("Ingrese su nota:"))
validacion2=print("Aprobado") if nota>=6 else print("Desaprobado")
#3
print("ejercicio 3")
par=int(input("Ingrese un numero par:"))
validacion3=print("Ha ingresado un numero par") if par%2==0 else print("Por favor ingrese un numero par")
#4
print("ejercicio 4")
edad4=int(input("Ingrese su edad:"))
if edad4<12:
    print("Niño/a")
elif edad4<18:
    print("Adolescente")
elif edad4<30:
    print("Adulto/a joven")
else:
    print("Adulto/a")
#5
print("ejercicio 5")
password=input("Ingrese una contraseña de entre 8 y 14 caracteres: ")
validacion5=print("Contraseña valida") if len(password)>=8 and len(password)<=14 else print("Ingrese una contraseña de entre 8 y 14 caracteres")
#6
print("ejercicio 6")
randomNum=[random.randint(1,100) for i in range(50)]
print(f"El promedio de la lista random es: {statistics.mean(randomNum)}")
print(f"La media de la lista random es: {statistics.median(randomNum)}")
print(f"La moda de la lista random es: {statistics.mode(randomNum)}")
#7
print("ejercicio 7")
frase=input("Ingrese una palabra o frase: ")
if frase[-1] in "aeiou":
    frase+="!"
print(frase)
#8
print("ejercicio 8")
name=input("Ingrese su nombre y la opcion que desee: ")
option=int(input("\n1. Si quiere su nombre en mayúscula" 
"\n2. Si quiere su nombre en minúsculas." 
"\n3. Si quiere su nombre con la primera letra mayúscula\n"))
match option:
    case 1:
        print(f"{name.upper()}")
    case 2:
        print(name.lower())
    case 3:
        print(name.title())
#9
print("ejercicio 9")
magnitud=float(input("Ingrese la magnitud del terremoto: "))
if  magnitud<3:
    print("Muy leve")
elif magnitud>=3 and magnitud<4:
    print("Leve")
elif magnitud>=4 and magnitud<5:
    print("Moderado")
elif magnitud>=5 and magnitud<6:
    print("Fuerte")
elif magnitud>=6 and magnitud<7:
    print("Muy fuerte")
else:
    print("Exremo")
#10
print("ejercicio 10")
print("Ingrese los siguientes datos: ")
hemisferio=input("Hemisferio (N/S): ")
mes=int(input("Mes del año: "))
dia=int(input("Dia del mes: "))
if (mes==12 and 21<=dia<=31) or (1<=mes<=3 and dia<=20) and hemisferio=="n": 
    print("Invierno")
elif (mes==12 and 21<=dia<=31) or (1<=mes<=3 and dia<=20) and hemisferio=="s":
    print("Verano")
elif (mes==3 and 21<=dia<=31) or (4<=mes<=6 and dia<=20) and hemisferio=="n":
    print("Primavera")
elif (mes==3 and 21<=dia<=31) or (4<=mes<=6 and dia<=20) and hemisferio=="s":
    print("Otoño")
elif (mes==6 and 21<=dia<=31) or (7<=mes<=9 and dia<=20) and hemisferio=="n":
    print("Verano")
elif (mes==6 and 21<=dia<=31) or (7<=mes<=9 and dia<=20) and hemisferio=="s":
    print("Invierno")
elif (mes==9 and 21<=dia<=31) or (10<=mes<=12 and dia<=20) and hemisferio=="n":
    print("Otoño")
elif (mes==9 and 21<=dia<=31) or (10<=mes<=12 and dia<=20) and hemisferio=="s":
    print("Primavera")