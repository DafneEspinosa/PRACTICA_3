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
    
    i=0
    while(i<len(lista)):
        if float(lista[i])>(float(constante)+ float(lista_2[i])):
            new_lista.insert(i,float(constante)+float(lista_2[i]))
            print(new_lista)
        else:  
            new_lista.insert(i,float(lista[i]))
            print(new_lista)
        i+=1
    return new_lista

actualizar_pesos(lista, lista_2)

