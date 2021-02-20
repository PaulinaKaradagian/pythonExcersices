# Ejercicio 21:
# Crear un programa que almacene las asignaturas de un curso (por ejemplo
# MatemÃ¡ticas, FÃ­sica, QuÃ­mica, Historia y Lengua) en una lista y muestre por pantalla el
# mensaje â€œYo estudio <asignatura>â€, donde <asignatura> es cada una de las
# asignaturas de la lista

materias = ["Matemática", "Física", "Química", "Historia", "Lengua"]

print(materias)

def asignaturas():
  for i in materias:
    print("Yo estudio", i)

asignaturas()