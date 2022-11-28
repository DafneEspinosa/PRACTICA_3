import math

#Definición de infinito, infinito es de tipo FLOAT
infinito=math.inf
print((infinito+1000))

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

###############################cambiar variable vector_
def obtener_vecinos(vector_c):
    for i in range(0,3):
###############################cambiar variable vector_
        if vector_c[i]!=0:
###############################cambiar variable vector_
            #peso de los vecinos cercanos
            peso_vecinos.append(vector_c[i])
            #poscion con indice de los vecinos
            posiciones_vecinos.append(i)
###############################cambiar variable vector_ 
        if vector_c[i]==0:
            #Nodo central
            print("El nodo central se encuentra en la posicion:",i)
            if i==0:
                nodo_principal="A"
                print("Nodo principal:", nodo_principal)
            if i==1:
                nodo_principal="B"
                print("Nodo principal:", nodo_principal)
            if i==2:
                nodo_principal="C"
                print("Nodo principal:", nodo_principal)


    for ii in posiciones_vecinos:
        if ii==0:
            vecinos.append("A")
        if ii==1:
            vecinos.append("B")
        if ii==2:
            vecinos.append("C")

    print("Vecinos",vecinos)
    print("posiciones de los vecinos",posiciones_vecinos)
    print("peso hacia los vecinos:",peso_vecinos)

    #DATOS A RETORNAR POR DEFINIR!!!!!!

 ###############################cambiar variable vector_
obtener_vecinos(vector_c)
