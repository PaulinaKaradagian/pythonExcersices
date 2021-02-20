# Ejercicio 18:
# Crear un programa que pida al usuario una palabra y luego muestre por pantalla una a
# una las letras de la palabra introducida empezando por la Ãºltima.

word = input("Escriba una palabra: ")
def reversa():

  for letra in word[::-1]:
    print(letra)

reversa()
    