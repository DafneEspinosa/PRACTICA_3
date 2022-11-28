import pandas as pd
import numpy as np
import math

infinito=math.inf

def mostrar_tabla(lista_old,lista_recv,lista_actual):
    listas=[lista_old,lista_recv,lista_actual]
   
    columnas =["A","B","C"]
    get_old={lista_old:columnas for (lista_old,columnas) in zip(lista_old,columnas)}
    get_fuente={lista_recv:columnas for (lista_recv,columnas) in zip(lista_recv,columnas)}

    nombre_colum = ['OLD '+get_old[0],get_fuente[0],'NEW '+get_old[0]+':'+get_old[0]+'<---'+get_fuente[0]]

    vector_tabla = pd.DataFrame(np.array(listas),columns=columnas, index=nombre_colum)
    vector_tabla=vector_tabla.transpose()
    print(vector_tabla)


# Valor de la lista asociadas a los nodos A,B,C de la siguiente forma: [A,B,C]

old=[0,2,infinito]    #lista anterior a actualizarse (Ex. old A)
recv=[2,0,6]   #lista recibida de algun nodo
actual=[0,2,6]   #lista con peso actualizados (Ex. new A)

mostrar_tabla(old, recv, actual)