# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 08:45:27 2021

@author: rokefeler@gmail.com
"""

#%%
#Ejercicio 7.12: Caminatas al azar
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors




def randomwalk(nPasosDelargo):
    'Genera una caminata al azar de N pasos de largo'
    pasos=np.random.randint (-1,2,nPasosDelargo)    #devuelve un arrays desde -1 hasta 2, en un tamaño de largo
    return pasos.cumsum()  #retorna la suma acumulada de los elementos
#%%
#Ejercicio 7.9: Subplots fuera de una grilla
def ejercicio_709():
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
#Ejercicio 7.10: Caminatas al azar
def doceCaminatas(NTrayectorias=12, N=100000, minRangeY=None, maxRangeY=None):
    anchoLinea = 0.65
    caminatas = [randomwalk(N) for _ in range(NTrayectorias)]
    distancias = [max(abs(caminata)) for caminata in caminatas]
    colores = [nam for nam,namhex in \
                random.choices(list(mcolors.CSS4_COLORS.items()), \
                               k=NTrayectorias )] 
    #colores = np.random.rand(N)
    
    indexMinCaminata = np.argmin(distancias) #Return indice del minimo valor
    indexMaxCaminata = np.argmax(distancias) #Return indice del máximo valor
    
    #si no hay datos de Rango de Eje y, calcular automaticamente
    if minRangeY==None:
        minRangeY = min([min(caminata) for caminata in caminatas])
    if maxRangeY==None:
        maxRangeY = max([max(caminata) for caminata in caminatas])
    
    factorX = 1.05   #Factor para eje x
    factorY = 1.11   #Factor para eje y
    #fig = plt.figure()
    fig = plt.figure(figsize=(15, 8), dpi=80) #formato de la figura
    #top=0.928,bottom=0.041,left=0.098,right=0.977,hspace=0.186,wspace=0.252
    
    plt.subplot(2, 1, 1) # define la figura de arriba
    for i, caminata in enumerate(caminatas):
        alpha = 0.4
        lineStyle = '-'
        if (i==indexMinCaminata or i==indexMaxCaminata):
            alpha = 1.0
            lineStyle = '--'
        plt.plot(caminata, color=colores[i], linewidth=anchoLinea,\
                 linestyle=lineStyle, alpha=alpha)
        plt.xlim(0, N*factorX)                     #rango del ejex 
        plt.ylim(minRangeY*factorY, maxRangeY*factorY)        #rango del ejey
        plt.xticks([]), plt.yticks([minRangeY,0,maxRangeY])   # saca las marcas    
        plt.title("12 Caminatas al Azar", size=10) ## Titulo del Grafico
    
    
    #Graficar la Caminata que mas se aleja
    plt.subplot(2, 2, 3)    # define la figura de arriba
    plt.plot(caminatas[indexMaxCaminata],color=colores[indexMaxCaminata], \
             linewidth=anchoLinea, linestyle="-")
    plt.xlim(0, N*factorX)
    plt.ylim(minRangeY*factorY, maxRangeY*factorY)
    plt.xticks([]), plt.yticks([minRangeY, 0, maxRangeY]) # saca las marcas    
    plt.title("La caminata que mas se aleja", size=8)
    
    
    #Graficar la Caminata que menos se aleja
    plt.subplot(2, 2, 4) # define la figura de arriba
    plt.plot(caminatas[indexMinCaminata],color=colores[indexMinCaminata],\
             linewidth=anchoLinea, linestyle="-")
    plt.xlim(0, N*factorX)
    plt.ylim(minRangeY*factorY, maxRangeY*factorY)
    plt.xticks([]), plt.yticks([minRangeY, 0, maxRangeY]) # saca las marcas    
    plt.title("La caminata que menos se aleja", size=8)
    
    plt.show()
#%%
#Ejercicio 7.11: Gráficos de barras
def ejercicio711():
    n = 12 
    X = np.arange(n)
    Y1 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
    Y2 = (1 - X / float(n)) * np.random.uniform(0.5, 1.0, n)
    fig = plt.figure()
    plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
    plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')
    for x, y in zip(X, Y1):
        plt.text(x + 0.8, y + 0.05, '%.2f' % y, ha='right', va='bottom')
    
    for x, y in zip(X, Y2):
        plt.text(x + 0.8, -1*y - 0.18, '%.2f' % y, ha='right', va='bottom')
    
    plt.ylim(-1.25, +1.25)
    plt.show()
#%%
#Ejercicio 7.12: Coordenadas polares
def ejercicio712():
    fig = plt.figure()
    plt.axes([0, 0, 1, 1], polar=True)

    N = 20
    theta = np.arange(0., 2 * np.pi, 2 * np.pi / N)
    radii = 10 * np.random.rand(N)
    width = np.pi / 4 * np.random.rand(N)
    bars = plt.bar(theta, radii, width=width, bottom=0.0)

    for r, bar in zip(radii, bars):
        bar.set_facecolor(plt.cm.jet(r / 10.))
        bar.set_alpha(0.5)
    plt.show()
#%%
#Ejercicio 7.13: Setear el color de un scatter plot
def ejercicio713():
    fig = plt.figure()
    n = 1024
    colors = np.random.rand(n)
    X = np.random.normal(0,1,n)
    Y = np.random.normal(0,1,n)
    plt.scatter(X,Y,c=colors, alpha=0.5)
    plt.show()      
#%%
if __name__ == "__main__":
    
    N=100000
    #Descomentar para ejecutar grafico de 12 caminatas
    doceCaminatas(24, N)
    
    #ejercicio711()
    
    #ejercicio712()
    
    #ejercicio713()