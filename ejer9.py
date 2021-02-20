# Ejercicio 9:
# Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñcas. Suele
# hacer venta por correo y la empresa de logí­stica les cobra por el peso de cada paquete
# así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete
# a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Crear un programa que lea
# el número de payasos y muñecas vendidos en el último pedido y calcule el peso total
# del paquete que será enviado. Mostrar el resultado por pantalla.

payaso = 112
doll = 75

pedidopa = int(input("Ingrese la cantidad de payasos que desea comprar: "))

pedidomu = int(input("Ingrese la cantidad de muñecas que desea comprar: "))

pesopa = pedidopa * payaso
pesomu = pedidomu * doll

def logistica():
  total = pesopa + pesomu
  print("El peso total del pedido de ", pedidopa, "payasos y de", pedidomu, "muñecos, es de", total, "gramos.")
  print("El peso total de los payasos pedidos es de", pesopa, " gramos y el de los muñecos", pesomu)

logistica()