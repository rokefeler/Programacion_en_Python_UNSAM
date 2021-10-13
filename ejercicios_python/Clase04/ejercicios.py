# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 08:37:35 2021

@author: rokefeler@gmail.com
"""
#%%
#Ejercicio 4.1: Debugger
def invertir_lista(lista):
    '''Recibe una lista L y la develve invertida.'''
    copia = lista.copy()
    invertida = []
    # i = len(lista)
    # while i > 0:    # tomo el último elemento 
    #     i = i-1
    #     invertida.append (lista.pop(i))  #
    while(len(copia)>0):
        invertida.append(copia.pop())
    return invertida

# l = [1, 2, 3, 4, 5]    
# m = invertir_lista(l)
# print(f'Entrada {l}, Salida: {m}')

#%%
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion = []
    #registro = {} #Error si se declara fuera de bucle for, espacio de memoria es unico y se modifica todos los valores
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro = {} #fix, aqui se debe colocar la inicializacion para cada iteracion
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)

#%%
def busqueda_con_index(lista, e):
    '''Busca un elemento e en la lista.

    Si e está en lista devuelve el índice,
    de lo contrario devuelve -1.
    '''
    pos = -1
    if e in lista:
        pos = lista.index(e)
    #else:
    #    pos = -1
    return pos
print( busqueda_con_index([1, 4, 54, 3, 0, -1], 1) )
#0
print(busqueda_con_index([1, 4, 54, 3, 0, -1], -1) )
#5
print(busqueda_con_index([1, 4, 54, 3, 0, -1], 3) )
#3
print(busqueda_con_index([1, 4, 54, 3, 0, -1], 44) )
#-1
print(busqueda_con_index([], 0) )
#-1
#%%
#Búsqueda lineal
def busqueda_lineal(lista, e):
    '''Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1.
    '''
    pos = -1  # comenzamos suponiendo que e no está
    i = 0     
    for z in lista:  # recorremos los elementos de la lista
        if z == e:   # si encontramos a e
            pos = i  # guardamos su posición
            break    # y salimos del ciclo
        i += 1
    # Esto es mas Elegante
    # for i, z in enumerate(lista): # recorremos la lista
    #     if z == e:   # si encontramos a e
    #         pos = i  # guardamos su posición
    #         break    # y salimos del ciclo
    return pos
print( busqueda_lineal([1, 4, 54, 3, 0, -1], 44) )
#-1
print( busqueda_lineal([1, 4, 54, 3, 0, -1], 3) )
#3
print( busqueda_lineal([1, 4, 54, 3, 0, -1], 0) )
#4
print( busqueda_lineal([], 42) )
#-1

#%%
#
