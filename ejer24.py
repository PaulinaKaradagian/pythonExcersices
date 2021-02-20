# Ejercicio 24:
# Crear un programa que almacene el diccionario con los crÃ©ditos de las asignaturas de
# un curso {'MatemÃ¡ticas': 6, 'FÃ­sica': 4, 'QuÃ­mica': 5} y despuÃ©s muestre por pantalla los
# crÃ©ditos de cada asignatura en el formato <asignatura> tiene <crÃ©ditos> crÃ©ditos,
# donde <asignatura> es cada una de las asignaturas del curso, y <crÃ©ditos> son sus
# crÃ©ditos. Al final debe mostrar tambiÃ©n el nÃºmero total de crÃ©ditos del curso.




asignatura = {
  "Matemática" : 6,
  "Física" : 4,
  "Química" : 5
}


def creditos_materias():
    total_creditos = 0
    
    for materia, credito in asignatura.items():
        print(f"{materia} tiene {credito} créditos")
        total_creditos += credito

    print(f"El total de créditos es {total_creditos}")
    
creditos_materias()