# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 15:10:14 2021

@author: rokefeler@gmail.com



"""
import random
import numpy as np
def medir_temp(n):
    '''
    La distribución normal tiene dos parámetros, 
    denominados media  => mu    0
     y desvío estándar => sigma 0.2
     random.normalvariate(mu,sigma)
    '''
    temp_real_persona = 37.5
    temperaturas = [temp_real_persona+random.normalvariate(0,0.2) for i in range(n)]
    return temperaturas

def mediana(l):
    mitad = len(l) // 2 #division entera
    l.sort()            #ordenar lista
    if not len(l) % 2:  #Si residuo no es la mitad
        return (l[mitad - 1] + l[mitad]) / 2.0
    return l[mitad]
def resumen_temp(n, verbose=False, save=False):
    '''Dev. tupla con el valor máximo, el mínimo, promedio y la mediana 
    (en ese orden)
    '''
    temperaturas =  medir_temp(n)
    if verbose:
        print(f'Temperaturas: {temperaturas}')
    if save:
        b=np.array(temperaturas)
        np.save('temperaturas',b)
    max_t = max(temperaturas)
    min_t = min(temperaturas)
    avg_t = sum(temperaturas) / len(temperaturas)
    mediana_t = mediana(temperaturas)
    if verbose:
        print(f'Resultado: (máximo, mínimo, promedio,mediana): ({max_t}, {min_t}, {avg_t}, {mediana_t})')
    return ( max_t,min_t, avg_t, mediana_t)

#%%
#Rpta 5.6 - Estimacion del calculo de pi 
if __name__ == "__main__":
    N = 999
    #aqui si verbose =True imprime Valores 
    #y si save=True, se graban los datos generados en un archivo llamado temperaturas.npy
    #pueden activar verbose para ver datos parciales y hacer test
    print (resumen_temp(N,verbose=False,save=True))