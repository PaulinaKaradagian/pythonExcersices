import sys

user1 = input("Cómo te llamas?")
user2 = input("Y tu nombre?")
user1_answer = input("%s, qué elegís? Piedra, papel o tijera?" % user1)
user2_answer = input("%s, cuál elegís? Piedra papel o tijera?" % user2)

def compare(u1, u2):
    if u1 == u2:
        return("Es empate!")
    elif u1 == 'piedra':
        if u2 == 'tijera':
            return("Piedra gana!")
        else:
            return("Papel gana!")
    elif u1 == 'tijera':
        if u2 == 'papel':
            return("Gana tijera!")
        else:
            return("Piedra gana!")
    elif u1 == 'papel':
        if u2 == 'piedra':
            return("Papel gana!")
        else:
            return("Gana tijera!")
    else:
        return("Elección inválida! No elegiste piedra, papel o tijera. Probá nuevamente.")
        sys.exit()

print(compare(user1_answer, user2_answer))