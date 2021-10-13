# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 12:56:36 2021
Ejercicio 4.6: Propagación
@author: rokefeler@gmail.com
"""

def propagar(listaoriginal):
    if not 0 in listaoriginal:  #si no hay ningun fosforo para encender
        return listaoriginal
    
    lista = listaoriginal.copy()  #trabajamos con una copia a fin de no modificar lista original
    largo = len(lista)
    #recorremos lista hacia la derecha
    for ind,actual in enumerate(lista): # Recorro la lista hacia la derecha
        anterior = None
        siguiente = None
        if (ind-1) >= 0:
            anterior = lista[ind-1]
        if (ind+1) < largo:
            siguiente = lista[ind+1]
        
        lista[ind] = encender(anterior, actual, siguiente)

    #recorremos lista hacia la Izquierda
    ind = largo-1
    while ind>=0:
        anterior = None
        siguiente = None
        actual = lista[ind]
        if (ind+1) < largo:
            siguiente = lista[ind+1]
        if (ind-1) >= 0:
            anterior = lista[ind-1]
        lista[ind] = encender(anterior, actual, siguiente)
        ind -= 1
    return lista

#funcion que evalua posicion actual, anterior y posterior
def encender(anterior,actual, siguiente):
    try:
        if actual != 0:
            return actual
        if (anterior != None and anterior == 1) or (siguiente != None and siguiente == 1):
            return 1
    except:
        pass
    return actual 
#%%
from pprint import pprint
if __name__ == "__main__":
    # execute only if run as a script
    lista = [ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]
    print("Lista original[1]: ", end='')
    pprint(lista)
    
    lista2 = propagar(lista)
    print("Lista propagada[1]: ", end='')
    pprint(lista2)
    #[ 0, 0, 0,-1, 1, 1, 1, 1,-1, 1, 1, 1, 1]
    
    
    lista = [ 0, 0, 0, 1, 0, 0]
    print("Lista original[2]: ", end='')
    pprint(lista)
    
    lista2 = propagar(lista)
    print("Lista propagada[2]: ", end='')
    pprint(lista2)
    #[ 1, 1, 1, 1, 1, 1]
    