# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 22:14:32 2021

@author: rokefeler@gmail.com

"""
#%%
#Ejercicio 7.11: Subplots fuera de una grilla
import matplotlib.pyplot as plt

def test_711():
    fig = plt.figure()
    plt.subplot(2, 1, 1) # define la figura de arriba
    plt.plot([0,1,2],[0,1,0]) # dibuja la curva
    plt.xticks([]), plt.yticks([]) # saca las marcas
    
    plt.subplot(2, 3, 4) # define la primera de abajo, que sería la tercera si fuera una grilla regular de 2x3
    plt.plot([0,1],[0,1])
    plt.xticks([]), plt.yticks([])
    
    #insercion pedida
    plt.subplot(2, 3, 5)    #define Segunda de abajo (en medio)
    plt.plot([0,1],[0,0])   #Dibuja en Eje X
    plt.xticks([]), plt.yticks([])
    
    
    plt.subplot(2, 3, 6) # define la segunda de abajo, que sería la ultima Figura, si fuera una grilla regular de 2x3
    plt.plot([0,1],[1,0])
    plt.xticks([]), plt.yticks([])
    
    plt.show()

#%%
#Ejercicio 7.12: Caminatas al azar
import numpy as np
import matplotlib.pyplot as plt

def randomwalk(nPasosDelargo):
    'Genera una caminata al azar de N pasos de largo'
    pasos=np.random.randint (-1,2,nPasosDelargo)    #devuelve un arrays desde -1 hasta 2, en un tamaño de largo
    return pasos.cumsum()  #retorna la suma acumulada de los elementos
#%%

N = 100000
NTrayectorias = 12
anchoLinea = 0.65
caminatas = [randomwalk(N) for i in range(NTrayectorias)]
indexMinCaminata = 0
indexMaxCaminata = 0
color = ['blue','orange','green','red','purple','brown','pink','gray','olive','cyan','gold','darksalmon']
factorx = 1.05   #Factor para eje x
factory = 1.11   #Factor para eje y
fig = plt.figure()
plt.subplot(2, 1, 1) # define la figura de arriba

for i, caminata in enumerate(caminatas):
    plt.plot(caminata,color=color[i], linewidth=anchoLinea, linestyle="-")
    plt.xlim(0, N*factorx)                     #rango del ejex 
    plt.ylim(-500*factory, 500*factory)        #rango del ejey
    plt.xticks([]), plt.yticks([-500,0,500])   # saca las marcas    
    plt.title("12 Caminatas al Azar", size=10) ## Titulo del Grafico

    
    #determinando el que menos se aleja
    if min(abs(caminata)) < min(abs(caminatas[indexMinCaminata])):
        indexMinCaminata = i  #Almacenar solo su indice

       
    #determinando la que mas se aleja
    if max(abs(caminata)) > max(abs(caminatas[indexMaxCaminata])):
        indexMaxCaminata = i  #Almacenar solo su indice


#Graficar la Caminata que mas se aleja
plt.subplot(2, 2, 3)    # define la figura de arriba
plt.plot(caminatas[indexMaxCaminata],color=color[indexMaxCaminata], \
         linewidth=anchoLinea, linestyle="-")
plt.xlim(0, N*factorx)
plt.ylim(-500*factory, 500*factory)
plt.xticks([]), plt.yticks([-500,0,500]) # saca las marcas    
plt.title("La caminata que mas se aleja", size=8)


#Graficar la Caminata que menos se aleja
plt.subplot(2, 2, 4) # define la figura de arriba
plt.plot(caminatas[indexMinCaminata],color=color[indexMinCaminata],\
         linewidth=anchoLinea, linestyle="-")
plt.xlim(0, N*factorx)
plt.ylim(-500*factory, 500*factory)
plt.xticks([]), plt.yticks([-500,0,500]) # saca las marcas    
plt.title("La caminata que menos se aleja", size=8)

plt.show()