# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 19:50:40 2021

@author: rokefeler@gmail.com
"""

from matplotlib import pyplot as plt
import numpy as np

X = np.linspace(-2*np.pi, 2*np.pi, 256*2)  #array de numpy con 256 valores que van desde -π a +π (incluído)
C = np.cos(X)                   #C tiene los valores del coseno (256 valores)
S = np.sin(X)                   #S tiene los valores del seno (256 valores).
plt.plot(X, C)                  #Crea el Grafico de Coseno
plt.plot(X, S)                  #Crea el Grafico de Seno    

plt.show()                      #Muestro el Grafico
