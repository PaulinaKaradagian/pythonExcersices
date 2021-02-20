# Ejercicio 10:
# Crear un programa que pida al usuario su edad y muestra por pantalla si es mayor de
# edad o no, siendo 18 años la mayorí­a de edad.

age = int(input("Enter your age: "))

def mayoria():
  if age >= 18:
    print("Sos mayor de edad.")
  else:
    print("Sos menor de edad.")

mayoria()