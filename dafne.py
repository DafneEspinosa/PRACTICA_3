import math
#definición de infinito
infinito = math.inf

#lista_2 = [0,2,infinito]
lista = [2,0,4] 
lista_2 = [infinito,4,0]
############ QUIEN ES EL QUE MANDA ##################
def autor_index(lista):
    autor = lista.index(0)
    return autor

#lista es old_lista
#lista_2 es la lista que se le manda para actualizar lista
########### CONSTANTE PARA SUMAR ###################

def constante_suma(lista,lista_2):
    autor = autor_index(lista)
    constante = lista_2[autor]
    return constante


################ OPERACIÓN ####################
def actualizar_pesos(lista, lista_2):
    
    constante = constante_suma(lista,lista_2)
    
    new_lista=[]
    
    for old_lista, update_lista in zip (lista,lista_2):
        update_lista_cte = float(constante)+float(update_lista)
        if float(old_lista)> update_lista_cte:
            new_lista.append(update_lista_cte)
        else:
            new_lista.append(old_lista)

    print(new_lista)
    
    return new_lista

actualizar_pesos(lista, lista_2)

