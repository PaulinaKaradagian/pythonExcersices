# Ejercicio 5:
# Crear un programa que pregunte el nombre del usuario y después de que el usuario lo
# introduzca muestre por pantalla <NOMBRE> tiene <n> letras.

def largo():
  name = input("Enter your name: ")
  cantidad= len(name)
  print("Your name has", cantidad, "letters.")

largo()