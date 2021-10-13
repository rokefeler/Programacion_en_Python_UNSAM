# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 22:54:26 2021

@author: FamiliaRoqueSosa
"""
import random
#random.seed(31415)
def tirar():
    tirada=[]
    for i in range(5):
        tirada.append(random.randint(1,6))
    return tirada

def es_generala(tirada):
    return sum(tirada)/5 == tirada[0]

def test(N):
    G = sum([es_generala(tirar()) for i in range(N)])
    prob = G/N
    print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
    print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')
    
#%%    
#¿Por qué varían más los resultados obtenidos con N = 100000 
#que con N = 1000000? 

#%%
#¿Cada cuántas tiradas en promedio podrías decir que 
#sale una generala servida? 
jugada = 6**5
print(f'En promedio, cada {jugada} puede salir una Generala.')
#     La probabilidad de obtener una generala es 1/7776
#%%
#source: referencia https://seriesdivergentes.wordpress.com/2012/07/29/cuantas-veces-hay-que-tirar-los-dados/
print('¿Cómo se puede calcular la probabilidad de forma exacta?')
print('cada dado tiene una posibilidad en seis de obtener el mismo resultado que el primero')
print(', entonces la probabilidad de que todos caigan igual es?:')
print(' 1   1   1   1   1       1 ')
print('---*---*---*---*---- = ----')
print(' 6   6   6   6   6     7776')
