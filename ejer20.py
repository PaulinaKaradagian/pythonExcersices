# Ejercicio 20:
# Crear un programa que muestre el eco de todo lo que el usuario introduzca hasta que
# el usuario escriba â€œsalirâ€ que terminarÃ¡.



def eco(rta):
    
    while rta != "salir":
        print(respuesta)
        rta = input("Ingrese una palabra o escriba salir para terminar: ")
        
respuesta = input("Ingrese una palabra o escriba salir para terminar: ")
eco(respuesta)