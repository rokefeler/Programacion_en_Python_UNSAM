# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 22:58:10 2021

@author: rokefeler@gmail.com
"""

def busqueda_lineal(lista, e):
    i = len(lista)       #Analizar longitud de lista
    while(i>0):          #ingresar a bucle mientras que longitud sea mayor a cero
        i-=1             #disminuir indice porque Listas empiezan desde 0
        if(lista[i]==e): #comparar
            return i     #si es correcto salir retornando la posicion
    return -1            #si llega aqui significa que no se encontro
#%%
def busqueda_lineal_lordenada(lista, e, verbose = False):
    '''Búsqueda Lineal Ordenada
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''    
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    i = len(lista)       #Analizar longitud de lista
    while(i>0):          #ingresar a bucle mientras que longitud sea mayor a cero
        i-=1             #disminuir indice porque Listas empiezan desde 0
        if verbose:
            print(f'[DEBUG] Buscando {e} ==> i = {i}, lista[i]={lista[i]}')
        if(lista[i]==e): #comparar
            return i     #si es correcto salir retornando la posicion
        elif lista[i]<e: #comparar
            return pos
    return pos            #si llega aqui significa que no se encontro
#%%
def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve valor negativo si x no está en lista
    ese valor negativo es la posible ubicación donde insertarlo para que lista siga ordenada;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    comps = 0 # inicializo en cero la cantidad de comparaciones
    if verbose:
        print('[DEBUG] izq |der |med |Val |Ubi')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    #ubi = -1 #posible ubicación Si no se encuentra
    izq = 0  #posicion Inicial Izquierda, siempre es 0
    der = len(lista) - 1 #posicion FInal Derecha, Long -1
    ubicado = False
    while izq <= der:
        comps += 1 # incrementar cant de comparaciones
        medio = (izq + der) // 2  #Division Entera
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d} | {lista[medio]:3d} | {ubicado}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
            ubicado = True
            break
        
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda

    if not (izq <= der):
        pos = izq*(1 if ubicado else -1)
    return pos,comps
#%%
#Ejercicio 6.14: Búsqueda binaria
def donde_insertar(lista, x):
    pos = busqueda_binaria(lista,x)
    return abs(pos[1])
#%%
#Ejercicio 6.15: Insertar un elemento en una lista
def insertar(lista, x):
    pos,comparaciones = busqueda_binaria(lista, x, verbose = False)
    if pos<0:
        lista.insert(pos*-1,x)
    return abs(pos)
#%%
if __name__ == "__main__":
    L = [1,3,5,7,9,11,13,15,17,19,21,23]
    e = 9
    i = busqueda_lineal(L, e)
    print(f'Se busca {e} en la Lista Ordenada L de {len(L)} elementos->Resultado Posición: {i}')
    #%%
    L = [1,3,5,7,9,11,13,15,17,19,21,23]
    e = 9
    i = busqueda_lineal_lordenada(L, e, verbose=True)
    print(f'Se busca {e} en la Lista Ordenada L de {len(L)} elementos->Resultado Posición: {i}')
    #%%
    L = [1,3,5,7,9,11,13,15,17,19,21,23]
    e = 20
    i = busqueda_binaria(L, e, verbose=True)
    pos = donde_insertar(L, e)
    print(f'Se busca {e} en la Lista Ordenada L de {len(L)} elementos->Resultado {"UBICADO" if i[0]>=0 else "NO UBICADO"} - Posición: {i[0]}')
    print(f'Resultado de llamado funcion donde_insertar(lista,x) : {pos}')
#%%