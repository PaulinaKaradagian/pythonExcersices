###Ejercicio 4:
#Crear un programa que pregunte el nombre del usuario y un número entero e imprima
#por pantalla en líneas distintas el nombre del usuario tantas veces como el número
#introducido.###

def datos():
  name = input("Enter your name: ")
  number = int(input("Enter a number: "))
  
  for i in range(number):
    
    print(name)

datos()