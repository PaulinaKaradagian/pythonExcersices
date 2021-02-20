# Ejercicio 19:
# Crear un programa en el que se pregunte al usuario por una frase y una letra, y
# muestre por pantalla el nÃºmero de veces que aparece la letra en la frase.


frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra a buscar: ")

def busqueda():

  
  print("La letra", letra, "aparece", frase.count(letra), "veces.")

busqueda()