#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 00:26:44 2021

@author: lsesto
"""


import numpy as np
import matplotlib.pyplot as plt


#-------------------------------------------------
#defino la funcion random que genera los caminos aleatorios.
def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)    
    return pasos.cumsum()

#-------------------------------------------------

#defino una funcion para que arme los n caminos aleatorios
def caminos(num):
    '''me arma "num" caminos aleatorios'''
    lista_caminos=[]
    for i in range(num):
        lista_caminos.append(randomwalk(N))
    return lista_caminos

#--------------------------------------------------

#primero defino los 12 caminos que voy a plotear

N = 100000 #cantidad de puntos o "tiempo" de la caminata
lista_caminos = caminos(12)
#-----------------------------------------

#busco el maximo y el minimo
maximos_locales=[]
#minimos_locales=[]
for i in lista_caminos:
    maximos_locales.append(max(abs(i))) #busco el maximo de cada camino
    #minimos_locales.append(min(abs(i))) #busco el maximo de cada camino
#print(f'Maximo Local: {max(maximos_locales)}')
#print(f'Minimo Local: {min(minimosmos_locales)}')
#el indice del camino que mas se aleja es:
indice_max=maximos_locales.index(max(maximos_locales))
#el indice del camino que menos se aleja es:
indice_min=maximos_locales.index(min(maximos_locales))

#separo los caminos maximos y minimos:
camino_max=lista_caminos[indice_max]
camino_min=lista_caminos[indice_min]

#-----------------------------------------
#hago el plot

fig=plt.figure(figsize=(15, 8), dpi=180) #formato de la figura

#primer plot
plt.subplot(2, 1, 1) #figura principal
plt.xlabel("Tiempo")
plt.ylabel("Distancia al origen")
plt.title("Caminatas al azar")
plt.ylim(-700, 700)
for i in lista_caminos: #ploteo los n caminos distintos
    plt.plot(i, linewidth=1.0)


#el que mas se aleja:
plt.subplot(2,2,3)
plt.title("La caminatas que mas se aleja")
plt.xlabel("Tiempo")
plt.ylabel("Distancia al origen")
plt.ylim(-700, 700)
plt.plot(camino_max, linewidth=1.5)


#el que menos se aleja:
plt.subplot(2,2,4)
plt.title("La caminatas que menos se aleja")
plt.xlabel("Tiempo")
plt.ylabel("Distancia al origen")
plt.ylim(-700, 700)
plt.plot(camino_min, linewidth=1.5)


# plt.legend()
plt.show()