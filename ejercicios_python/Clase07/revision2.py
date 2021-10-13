# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 21:08:03 2021

@author: rokefeler@gmail.com
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 19:00:18 2021

@author: estreg
"""

import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)    
    return pasos.cumsum()
#%%
N = 100000

fig = plt.Figure()

A = [] #lista con los mínimos de cada randomwalk
B = [] #lista con los máximo de cada randomwalk
C = [] # lista con la lista de pasos
for i in range(0,13):
    pasos = randomwalk(N)
    plt.subplot(3,1,1)
    plt.plot(pasos)
    plt.ylim(-800,800)
    plt.xticks([])
    plt.title('12 Caminatas al azar', fontdict = {'fontsize' : 9})
    
    A.append(min(pasos))
    B.append(max(pasos))
    C.append(pasos)

for i,l in enumerate(C):
    if A[i] == min(A) : # grafica cuando encuentra el mínimo
        plt.subplot(3,2,3)
        plt.plot(l) 
        plt.ylim(-800,800)
        plt.xticks([0,50000,N])
        plt.ylabel('Distancia al origen')
        plt.xlabel('Tiempo')
        plt.title('La caminata que más se aleja', fontdict = {'fontsize' : 8.5})
        
        
    if B[i] == max(B): # grafica cuando encuentra el maximo
        plt.subplot(3,2,4)
        plt.plot(l)
        plt.xticks([]), plt.yticks([])
        plt.ylim(-800,800)
        plt.xticks([0,50000,N])
        plt.title('La caminata que menos se aleja', fontdict = {'fontsize' : 8.5})

distancias = [max(abs(caminata)) for caminata in C]
indexMinCaminata = np.argmin(distancias) #Return indice del minimo valor
indexMaxCaminata = np.argmax(distancias) #Return indice del máximo valor

#Graficar la Caminata que mas se aleja
plt.subplot(3, 2, 5)    # define la figura de arriba
plt.plot(C[indexMinCaminata])
plt.ylim(-800,800)
plt.xticks([0,50000,N])
plt.title("La caminata que mas se aleja REAL", size=8)


#Graficar la Caminata que menos se aleja
plt.subplot(3, 2, 6) # define la figura de arriba
plt.plot(C[indexMaxCaminata])
plt.ylim(-800,800)
plt.xticks([0,50000,N])
plt.title("La caminata que menos se aleja REAL", size=8)


plt.show()
