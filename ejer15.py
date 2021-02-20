# Ejercicio 15:
# Crear un programa para una empresa que tiene salas de juegos para todas las edades
# y quiere calcular de forma automÃ¡tica el precio que debe cobrar a sus clientes por
# entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de
# la entrada. Si el cliente es menor de 4 aÃ±os puede entrar gratis, si tiene entre 4 y 18
# aÃ±os debe pagar 500 y si es mayor de 18 aÃ±os, 1000.

age = int(input("Ingrese su edad: "))

def admision():
  if age >= 0 and age < 4:
    print("Usted entra gratis.")
  elif age <= 18:
    print("Usted debe abonar 500.")
  else:
    print("Su entrada tiene un valor de 1000")

admision()