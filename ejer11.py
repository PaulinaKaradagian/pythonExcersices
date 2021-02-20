# Ejercicio 11:
# Crear un programa que almacene la cadena de caracteres contraseña en una variable,
# pregunte al usuario por la contraseña e imprima por pantalla si la contraseña
# introducida por el usuario coincide con la guardada en la variable.

password = "calabaza"

passwd_pedido = input("Enter your password: ").lower()

def pwd():
  if passwd_pedido != password:
    print("La contraseña es incorrecta.")
  else:
    print("La contraseña es correcta.")


#Estudiar este a ver si consigo que pida el input nuevamente.
def contra():
  while passwd_pedido != password:
    print("La contraseña es incorrecta.")
    print(input("Ingrese su contraseña nuevamente: "))
    if passwd_pedido == password:
        print("La contraseña es correcta.")
    
    

pwd()