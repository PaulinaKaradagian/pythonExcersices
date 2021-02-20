# Ejercicio 13:
# Crear un programa que pida al usuario un nÃºmero entero y muestre por pantalla si es
# par o impar

numero = int(input("Ingrese un número: "))

def paridad():
  if numero % 2 == 0:
    print("El número", numero, "es par.")
  else:
    print("El número", numero, "es impar.")

paridad()



#num = int(input("Ingrese un número: "))

#def pares(num):

#  if num % 2 == 0:
#    print("El número es par.")
#  else: 
#    print("El número es impar.")

#pares()


######duda: si le pongo parametro num, por mas q le pongo un 6 cuando llamo, pone al q llamo, pero si lo pngo en el de arriba no.