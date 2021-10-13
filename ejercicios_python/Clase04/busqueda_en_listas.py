# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 09:06:41 2021

@author: rokefeler@gmail.com
"""
def buscar_u_elemento(lista,e):
    i = len(lista)       #Analizar longitud de lista
    while(i>0):          #ingresar a bucle mientras que longitud sea mayor a cero
        i-=1             #disminuir indice porque Listas empiezan desde 0
        if(lista[i]==e): #comparar
            return i     #si es correcto salir retornando la posicion
    return -1            #si llega aqui significa que no se encontro



#%% 
# Ejercicio 4.4: Búsqueda de máximo y mínimo
def maximo(lista):
    '''Devuelve el máximo de una lista, 
    la lista debe ser no vacía y de números positivos.
    '''
    # m guarda el máximo de los elementos a medida que recorro la lista. 
    m = None # Lo inicializo en 0
    for e in lista: # Recorro la lista y voy guardando el mayor
        if m == None or e>m:
            m=e
    return m

def minimo(lista):
    '''Devuelve el máximo de una lista, 
    la lista debe ser no vacía y de números positivos.
    '''
    # m guarda el máximo de los elementos a medida que recorro la lista. 
    m = None # Lo inicializo en 0
    for e in lista: # Recorro la lista y voy guardando el mayor
        if m == None or e<m:
            m=e
    return m

#%%
# Ejercicio 4.5: Invertir una lista
def invertir_lista(lista):
    invertida = []
    for e in lista: # Recorro la lista
        invertida.insert(0, e)       #metodo utilizando insert
    return invertida



#%%
def buscar_n_elemento(lista,e):
    numeroveces = 0
    for n in lista:
        if(n==e):
            numeroveces += 1
    return numeroveces    

if __name__ == "__main__":
    print( buscar_u_elemento([1,2,3,2,3,4],1) )
    print( buscar_u_elemento([1,2,3,2,3,4],2) )
    print( buscar_u_elemento([1,2,3,2,3,4],3) )
    print( buscar_u_elemento([1,2,3,2,3,4],5) )
    print( buscar_u_elemento([1,2,3,2,3,4],4) ) #prueba adicional
    
    print( maximo([1,2,7,2,3,4]) )
    #7
    print( maximo([1,2,3,4]) )
    #4
    print( maximo([-5,4]) )
    #4
    print( maximo([-5,-4]) )
    #-4 
    print( maximo([]) )
    #----------------------------
    print( minimo([1,2,7,2,3,4]) )
    #1
    print( minimo([1,2,3,4]) )
    #1
    print( minimo([-5,4]) )
    #-5
    print( minimo([-5,-4]) )
    #-5
    #------------------------------
    print( invertir_lista([1,2,7,2,3,4]) )