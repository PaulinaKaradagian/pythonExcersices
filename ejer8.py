# Ejercicio 8:
# Crear un programa que pregunte al usuario una cantidad a invertir, el interés anual y el
# número de años, y muestre por pantalla el capital obtenido en la inversón.

inversion = float(input("Ingrese la cantidad a invertir: "))

interes = float(input("Ingrese el interés anual: "))

anos = int(input("Ingrese la cantidad de años: "))

def plazo():
  total1 = (inversion * interes * anos)
  total2 = total1 - inversion
  print("De acuerdo a la información suministrada, usted ganará", total1, "lo que incrementa su capital en", total2)

plazo()