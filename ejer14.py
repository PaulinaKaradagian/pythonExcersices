# Ejercicio 14:
# En una determinada empresa, sus empleados son evaluados al final de cada aÃ±o. Los
# puntos que pueden obtener en la evaluaciÃ³n comienzan en 0.0 y pueden ir
# aumentando, traduciÃ©ndose en mejores beneficios. Los puntos que pueden conseguir
# los empleados pueden ser 0.0, 0.4, 0.6 o mÃ¡s, pero no valores intermedios entre las
# cifras mencionadas. A continuaciÃ³n se muestra una tabla con los niveles
# correspondientes a cada puntuaciÃ³n. La cantidad de dinero conseguida en cada nivel
# es de 100000 multiplicada por la puntuaciÃ³n del nivel.
# Nivel PuntuaciÃ³n
# Inaceptable 0.0
# Aceptable 0.4
# Meritorio 0.6 o mÃ¡s
# Crear un programa que lea la puntuaciÃ³n del usuario e indique su nivel de rendimiento,
# asÃ­ como la cantidad de dinero que recibirÃ¡ el usuario.


puntuacion = float(input("Entre una calificación: "))
bono = 100000

def calificacion():
  if puntuacion == 0.0:
    print("Su calificación es Inaceptable")
    print("Su bono conseguido por éste nivel es de", (bono * puntuacion))
  elif puntuacion == 0.4:
    print("Su calificacion es Aceptable")
    print("Su bono conseguido por este nivel es de", (bono * puntuacion))
  elif puntuacion >= 0.6:
    print("Su calificación es Meritorio")
    print("Su bono conseguido por este nivel es de", (bono * puntuacion))
  else:
    print("Puntuación incorrecta.")

calificacion()