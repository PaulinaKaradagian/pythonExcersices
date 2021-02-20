# Ejercicio 22:
# Crear un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre
# por pantalla su producto escalar.


vector_1 = [1, 2, 3]
vector_2 = [-1, 0, 2]

lista_prod_vect = []
if len(vector_1) == len(vector_2):
    for i in range(len(vector_1)):
        prod_vect = vector_1[i] * vector_2[i]
        lista_prod_vect.append(prod_vect)
        
    prod_esc = sum(lista_prod_vect)
    print(prod_esc)
else:
    print("No se puede proseguir.")


# In[52]:


def producto_escalar(v1, v2):
    lista_prod_vect = []
    if len(v1) == len(v2):
        for i in range(len(v1)):
            prod_vect = v1[i] * v2[i]
            lista_prod_vect.append(prod_vect)

        prod_esc = sum(lista_prod_vect)
        print(prod_esc)
    else:
        print("No se puede proseguir.")
        
vector_1 = [1, 2, 3]
vector_2 = [-1, 0, 2]
producto_escalar(vector_1, vector_2)