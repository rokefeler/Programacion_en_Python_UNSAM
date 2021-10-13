# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 12:56:36 2021
Ejercicio 4.5: Invertir una lista
@author: rokefeler@gmail.com
"""

def invertir_lista(lista):
    invertida = []
    for e in lista: # Recorro la lista
        invertida.insert(0, e)       #metodo utilizando insert
    return invertida
#%%
print( invertir_lista([1,2,7,2,3,4]) )
print( invertir_lista( [1, 2, 3, 4, 5] ) )
print( invertir_lista( ['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel'] ) )
