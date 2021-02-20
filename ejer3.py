#Ejercicio 3:
#Crear un programa que pida al usuario nombre y edad e #imprima dichos datos en renglones distintos.

def datos():
  name = input("Enter your name: ")
  age = int(input("Enter your age: "))
  print("Your name is", name)
  print("Your are", age, "years old.")

datos()