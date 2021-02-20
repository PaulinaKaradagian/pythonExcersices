# Ejercicio 7:
# Crear un programa que pida al usuario dos nÃºmeros enteros y muestre por pantalla la
# <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los nÃºmeros
# introducidos por el usuario, y <c> y <r> son el cociente y el resto de la divisiÃ³n entera
# respectivament.

n = int(input("Enter a number: "))
m = int(input("Enter another number: "))

def operacion():
  c = n // m
  r = n % m
  print("El cociente es", c, "y el resto es", r)

operacion()