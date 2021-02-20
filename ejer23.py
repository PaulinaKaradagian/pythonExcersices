# Ejercicio 23:
# Crear un programa que guarde en un diccionario los precios de las frutas de la tabla,
# pregunte al usuario por una fruta, un nÃºmero de kilos y muestre por pantalla el precio
# de ese nÃºmero de kilos de fruta. Si la fruta no estÃ¡ en el diccionario debe mostrar un
# mensaje informando de ello.
# Fruta Precio (kg)
# Banana 80
# Manzana 100
# Pera 50
# Naranja 70

frutas = {
  "Banana" : 80,
  "Manzana" : 100,
  "Pera" : 50,
  "Naranja" : 70

}

pedido = input("Qué fruta desea llevar?: ").capitalize()

kilos = int(input("Cuántos kilos desea?: "))

def compra():
  if pedido in frutas:
    precio = kilos * frutas[pedido]
    print("El precio es de", precio)
  else: 
    print("No tenemos esa fruta.")

compra()