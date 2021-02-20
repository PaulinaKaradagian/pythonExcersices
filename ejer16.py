# Ejercicio 16:
# Crear un programa que pregunte al usuario su edad y muestre por pantalla todos los
# aÃ±os que ha cumplido (desde 1 hasta su edad).

age = int(input("Ingrese su edad: "))
def cumple():
    for i in range(1, age + 1):
        
        print("Ha cumplido", i, "años.")
        
       


cumple()