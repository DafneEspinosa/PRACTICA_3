import math

#Definición de infinito, infinito es de tipo FLOAT
infinito=math.inf
#Pesos del nodo A-->B y del nodo B-->C
peso_a_b=5
peso_b_c=3

#Vectores iniciales, len de  cada vector=3, posiciones 0,1,2
vector_a=[0,peso_a_b,infinito]
vector_b=[peso_a_b,0,peso_b_c]
vector_c=[infinito,peso_b_c,0]

#Lista donde se añadiran los vecinos del nodo central
vecinos=[]
peso_vecinos=[]
posiciones_vecinos=[]
nodos_restantes=[]
peso_nodos_restantes=[]



def obtener_vecinos_y_pesos(vector_c):
    for i in range(len(vector_c)):
        if vector_c[i]==0:
            posicion_nodo_central=i
            if i==0:
                nodo_central="A"
            if i==1:
                nodo_central="B"
            if i==2:
                nodo_central="C"
        else:
            if i==0:
                vecino="A"
                vecinos.append(vecino)
                peso_vecinos.append(vector_c[i])
            if i==1:
                vecino="B"
                vecinos.append(vecino)
                peso_vecinos.append(vector_c[i])
            if i==2:
                vecino="C"
                vecinos.append(vecino)
                peso_vecinos.append(vector_c[i])
                
    print("Nodo central:",nodo_central,"Posicion del nodo:",posicion_nodo_central)
    return vecinos,peso_vecinos
nodos_restantes,peso_nodos_restantes=obtener_vecinos_y_pesos(vector_c)
print("Nodos restantes:", nodos_restantes)
print("Peso Nodos restantes:", peso_nodos_restantes) 