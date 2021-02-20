# Ejercicio 25:
# Crear un programa que, a partir de una lista con todas las letras del abecedario, haga
# un copia y borre de esta Ãºltima todas las vocales. Luego imprimir por pantalla ambas
# listas, la completa y la sin vocales.
# Para crear la lista del abecedario se puede importar la variable ascii_lowercase del
# mÃ³dulo string:

from string import ascii_lowercase

lista_abc = list(ascii_lowercase)
# print(lista_abc)
lista_abc2 = lista_abc.copy()
def letras_abc(lista_abecedario):
    lista_abc2 = lista_abecedario.copy()

    for letra in lista_abc2:
        for vocal in "aeiou":
            if letra == vocal:
                lista_abc2.remove(letra)

    print(lista_abecedario)
    print(lista_abc2)
    
lista_abc = list(ascii_lowercase)
letras_abc(lista_abc)