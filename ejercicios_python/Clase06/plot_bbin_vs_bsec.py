# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 23:51:47 2021

@author: rokefeler@gmail.com
"""

import random
import matplotlib.pyplot as plt
import numpy as np
#from busqueda_binaria import bbin
#%%
def busqueda_secuencial_(lista, x):
    '''Si x está en la lista devuelve el índice de su primera aparición, 
    de lo contrario devuelve -1. Además devuelve la cantidad de comparaciones
    que hace la función.
    '''
    comps = 0 # inicializo en cero la cantidad de comparaciones
    pos = -1
    for i,z in enumerate(lista):
        comps += 1 # sumo la comparación que estoy por hacer
        if z == x:
            pos = i
            break
    return pos, comps
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
        print('[DEBUG] izq |der |medio | Valor')
    pos = -1 # Inicializo respuesta, el valor no fue encontrado
    ubi = -1 #posible ubicación Si no se encuentra
    izq = 0  #posicion Inicial Izquierda, siempre es 0
    der = len(lista) - 1 #posicion FInal Derecha, Long -1
    while izq <= der:
        comps += 1 # incrementar cant de comparaciones
        medio = (izq + der) // 2  #Division Entera
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d} | {lista[medio]} | {ubi}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
            ubi=der
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
            ubi=izq
    if pos<0:       #si no se encontro
        pos=ubi*-1  #devolver posible posicion de insercion en negativo
    return pos,comps
#%%
def generar_lista(n, m):
    '''
    Devuelve una lista ordenada de n elementos diferentes entre 0 y m-1
    '''
    l = random.sample(range(m), k = n)
    l.sort()
    return l
#%%
def generar_elemento(m):
    '''
    devuelve un elemento aleatorio entre 0 y m-1
    '''    
    return random.randint(0, m-1)
#%%
#Ejercicio 6.19: Contar comparaciones en la búsqueda binaria
def experimento_secuencial_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_secuencial_(lista,x)[1]

    comps_prom = comps_tot / k
    return comps_prom
#%%%
#Ejercicio 6.20: Búsqueda binaria vs. búsqueda secuencial
def experimento_binario_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_binaria(lista,x)[1]
    comps_prom = comps_tot / k
    return comps_prom    
#%%    
def test_grafico_experimento_secuencial_promedio():
    '''
    Grafica Resultado de un experimento de promedios utilizando algoritmo de busqueda secuencial.
    '''
    m = 10000
    k = 1000
    
    largos = np.arange(256) + 1 # estos son los largos de listas que voy a usar
    comps_promedio = np.zeros(256) # aca guardo el promedio de comparaciones sobre una lista de largo i, para i entre 1 y 256.

    for i, n in enumerate(largos):
        lista = generar_lista(n, m) # genero lista de largo n
        comps_promedio[i] = experimento_secuencial_promedio(lista, m, k)

    # ahora grafico largos de listas contra operaciones promedio de búsqueda.
    plt.plot(largos,comps_promedio,label = 'Búsqueda Secuencial') #label: permite ponerle un nombre a la curva que se muestra luego con la función plt.legend()
    plt.xlabel("Largo de la lista")             
    plt.ylabel("Cantidad de comparaciones")
    plt.title("Complejidad de la Búsqueda")
    plt.legend()
    plt.show()
#%%
def test_grafico_experimento_binario_promedio():
    '''
    Grafica Resultado de un experimento de promedios utilizando algoritmo de busqueda binaria.
    '''
    m = 10000
    k = 1000
    
    largos = np.arange(256) + 1 # estos son los largos de listas que voy a usar
    comps_promedio = np.zeros(256) # aca guardo el promedio de comparaciones sobre una lista de largo i, para i entre 1 y 256.

    for i, n in enumerate(largos):
        lista = generar_lista(n, m) # genero lista de largo n
        comps_promedio[i] = experimento_binario_promedio(lista, m, k)

    # ahora grafico largos de listas contra operaciones promedio de búsqueda.
    plt.plot(largos,comps_promedio,label = 'Búsqueda Binaria') #label: permite ponerle un nombre a la curva que se muestra luego con la función plt.legend()
    plt.xlabel("Largo de la lista")             
    plt.ylabel("Cantidad de comparaciones")
    plt.title("Complejidad de la Búsqueda")
    plt.legend()
    plt.show()    
#%%
#Ejercicio 6.20: Búsqueda binaria vs. búsqueda secuencial
def graficar_bbin_vs_bseq(m=10000, k=1000):
    '''
    Grafica Resultado de un experimento de promedios utilizando algoritmo de busqueda Secuencial y binaria.
    '''
    largos = np.arange(256) + 1 # estos son los largos de listas que voy a usar
    comps_promedio_secuencial = np.zeros(256) # aca guardo el promedio de comparaciones sobre una lista de largo i, para i entre 1 y 256.
    comps_promedio_binario = np.zeros(256) # aca guardo el promedio de comparaciones sobre una lista de largo i, para i entre 1 y 256.
    for i, n in enumerate(largos):
        lista = generar_lista(n, m) # genero lista de largo n
        comps_promedio_secuencial[i] = experimento_secuencial_promedio(lista, m, k)
        comps_promedio_binario[i] = experimento_binario_promedio(lista, m, k)

    # ahora grafico largos de listas contra operaciones promedio de búsqueda.
    #Multiples graficos en una sola figure
    # fig = plt.figure(figsize=(80,25))
    # fig.tight_layout()
    # ax = plt.subplot(1, 2, 1)  #1Grafico de 1 fila con 2 Columnas]
    # ax.plot(largos,comps_promedio_binario,color='green') #label: permite ponerle un nombre a la curva que se muestra luego con la función plt.legend()
    # ax.set_xlabel("Largo de la lista")
    # ax.set_ylabel("Cantidad de comparaciones")
    # ax.set_title('Búsqueda Binaria')
    
    # ax = plt.subplot(1, 2, 2)  #1Grafico de 1 fila con 2 Columnas]
    # ax.plot(largos,comps_promedio_secuencial,color='red') #label: permite ponerle un nombre a la curva que se muestra luego con la función plt.legend()
    # ax.set_xlabel("Largo de la lista")
    # ax.set_ylabel("Cantidad de comparaciones")
    # ax.set_title('Búsqueda Secuencial')
    
    plt.plot(largos,comps_promedio_binario,label = 'Búsqueda Binaria', color='green') #label: permite ponerle un nombre a la curva que se muestra luego con la función plt.legend()
    plt.plot(largos,comps_promedio_secuencial,label = 'Búsqueda Secuencial',color='red') #label: permite ponerle un nombre a la curva que se muestra luego con la función plt.legend()
    plt.xlabel("Largo de la lista")             
    plt.ylabel("Cantidad de comparaciones")
    plt.title("Complejidad de la Búsqueda")
    plt.xlim(0,250) 
    plt.ylim(0,50) 
    plt.legend()
    plt.show() 
    
#%%
if __name__ == "__main__":
    #test_grafico_experimento_secuencial_promedio()
    #test_grafico_experimento_binario_promedio()
    graficar_bbin_vs_bseq(m=10000, k=1000)