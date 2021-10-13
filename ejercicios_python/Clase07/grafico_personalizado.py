# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 21:58:55 2021

@author: rokefeler@gmail.com
"""

import numpy as np
import matplotlib.pyplot as plt

colorCoseno = "blue"
colorSin = "red"
anchoLinea = 2.5
factor = 1.1
# Crea una figura nueva, de 8x6 pulgadas, con 80 puntos por pulgada

plt.figure(figsize=(10, 6), dpi=80)


# Crea un nuevo subplot, en una grilla de 1x1
plt.subplot(1, 1, 1)

X = np.linspace(-np.pi, np.pi, 256)
C, S = np.cos(X), np.sin(X)

# Plotea el coseno con una línea azul contínua de ancho 1 (en pixeles)
plt.plot(X, C, color=colorCoseno, linewidth=anchoLinea, linestyle="-")

# Plotea el seno con una línea verde contínua de ancho 1 (en pixeles)
plt.plot(X, S, color=colorSin, linewidth=anchoLinea, linestyle="-")

# Rango del eje x Automatico
plt.xlim(X.min()*factor, X.max()*factor)

# Ponemos marcas (ticks) en el eje x
#plt.xticks(np.linspace(-4, 4, 9))
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], \
           [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$']) #Texto de marca en el Eje

# Rango del eje y Automatico
plt.ylim(C.min()*factor, C.max()*factor)

# Ponemos marcas (ticks) en el eje y
#plt.yticks(np.linspace(-1, 1, 5))
plt.yticks([-1, 0, +1],\
           [r'$-1$', r'$0$', r'$+1$'])  #Texto de marca en el eje y

    
#Movemos el contorno
ax = plt.gca()  # gca es 'get current axis' ó 'tomar eje actual'
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
    
#Ponemos un Titlo
plt.plot(X, C, color="blue", linewidth=2.5, linestyle="-", label="coseno")
plt.plot(X, S, color="red",  linewidth=2.5, linestyle="-", label="seno")

plt.legend(loc='upper left')  #En que posicion del tablero ponemos la leyenda

#------------------------------------------------------
#Marcacion de puntos y Anotaciones Latex en las graficas
t = 2 * np.pi / 3
plt.plot([t, t], [0, np.cos(t)], color='blue', linewidth=2.5, linestyle="--")
plt.scatter([t, ], [np.cos(t), ], 50, color='blue')

plt.annotate(r'$cos(\frac{2\pi}{3})=-\frac{1}{2}$',
             xy=(t, np.cos(t)), xycoords='data',
             xytext=(-90, -50), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

plt.plot([t, t],[0, np.sin(t)], color='red', linewidth=2.5, linestyle="--")
plt.scatter([t, ],[np.sin(t), ], 50, color='red')

plt.annotate(r'$sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',
             xy=(t, np.sin(t)), xycoords='data',
             xytext=(+10, +30), textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))

#------------------------------------------------------
#hacer más grandes las marcas y los textos y ajustar sus propiedades de modo
#que tengan sean semi-transparentes.
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(16)
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.65))

#------------------------------------------------------

# Podemos grabar el gráfico (con 72 dpi)
# plt.savefig("ejercicio_2.png)", dpi=72)

# Mostramos el resultado en pantalla
plt.show()