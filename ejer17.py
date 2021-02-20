# Ejercicio 17:
# Crear un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

def tablas():


  for i in range(1, 11):
    print("\nTabla del", i, "\n")
    for j in range(10):
      print(i, "x", j, "=", (i*j))
  
tablas()