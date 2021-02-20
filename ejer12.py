# Ejercicio 12:
# Crear un programa que pida al usuario dos nÃºmeros y muestre por pantalla su divisiÃ³n.
# Si el divisor es cero, el programa debe devolver un mensaje indicando que no se puede
# dividir por 

dividendo = int(input("Ingrese un número: "))
divisor = int(input("Ingrese otro número: "))

def divi():
  if divisor == 0:
    print("No se puede dividir por 0!")
  else:
    print(dividendo / divisor)

divi()