#1
print("ejercicio 1")
numbers=list(range(4,101,4))
print(numbers)
#2
print("ejercicio 2")
movies=["Alien","Gladiator","Interstellar","Jaws","Rocky"]
print(movies[-2])
#3
print("ejercicio 3")
words=[]
words.append("perro")
words.append("gato")
words.append("lobo")
print(words)
#4
print("ejercicio 4")
animals=["perro","gato","conejo","pez"]
animals[1]="loro"
animals[-1]="oso"
print(animals)
#5
print("ejercicio 5")
numbers=[8,15,3,22,7]
numbers.remove(max(numbers))
print(numbers)
#6
print("ejercicio 6")
numbers=list(range(10,31,5))
print(numbers[0])
print(numbers[1])
#7
print("ejercicio 7")
cars=["sedan","polo","suran","gol"]
cars[1]="focus"
cars[2]="corolla"
print(cars)
#8
print("ejercicio 8")
doubles=[]
doubles.append(5*2)
doubles.append(10*2)
doubles.append(15*2)
print(doubles)
#9
print("ejercicio 9")
purchases=[["pan","leche"],["arroz","fideos","salsa"],["agua"]]

purchases[2].append("jugo")
purchases[1][1]="tallarines"
purchases[0].remove("pan")

print(purchases)
#10
print("ejercicio 10")
nestedList=[15,True,[25.5,57.9,30.6],False]
print(nestedList)