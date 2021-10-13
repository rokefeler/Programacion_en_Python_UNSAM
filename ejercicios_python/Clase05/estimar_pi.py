# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 19:11:38 2021

@author: rokefeler@gmail.com
"""
import random
def generar_punto():
    x = random.uniform(-1, 1) #numero aleatorio entre -1 y 1
    y = random.uniform(-1, 1)
    #x = random.random() #generamos valores aleatorios entre 0 y 1
    #y = random.random()
    return (x,y)

def generar_puntos(N):
    puntos = [generar_punto() for x in range(N)]
    return puntos
#%%
def analizar_punto(punto):
    '''Si la longitud de la linea mediante pitagoras es < 1,
    entonces la gota de agua cayo dentro del circulo,
    por el contrario la gota cayo fuera de el
    '''
    x,y = punto
    resultado = False
    if (x**2+y**2)**0.5<=1.0:
        resultado = True
    return resultado

#%%
#Rpta 5.5 - Estimacion del calculo de pi 
if __name__ == "__main__":
    N_puntos = 100000
    puntos = generar_puntos(N_puntos)
    #print(puntos)
    cant_punto_dentro_circulo = sum([analizar_punto(punto) for punto in puntos])
    cant_puntos_fuera_circulo = N_puntos
    relacion_circ_cuadrado = cant_punto_dentro_circulo/cant_puntos_fuera_circulo
    print(f'Cantidad de puntos dentro del Circulo: {cant_punto_dentro_circulo}')
    print(f'Cantidad de puntos fuera del Circulo: {cant_puntos_fuera_circulo}')
    print(f'Relación Circulo / Cuadrado: {relacion_circ_cuadrado}')
    print(f'Valor Aprox. 4 * Relación : {4*relacion_circ_cuadrado}')
    
    print(f'Valor de pi, utilizando método MonteCarlo (con {N_puntos} puntos) = {4*relacion_circ_cuadrado}')