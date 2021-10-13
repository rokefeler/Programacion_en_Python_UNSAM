# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 19:11:38 2021

@author: rokefeler@gmail.com
"""
import random
def generar_punto():
    x = random.random()
    y = random.random()
    return x,y

def generar_puntos(N):
    puntos = [generar_punto() for x in range(N)]
    return puntos

def analizar_punto(punto):
    '''Si la longitud de la linea mediante pitagoras es < 1,
    entonces la gota de agua cayo dentro del circulo,
    por el contrario la gota cayo fuera de el
    '''
    x,y = punto
    resultado = False
    if (x**2+y**2)<1:
        resultado = True
    return resultado

def calculo_py_metodo_montecarlo:
    N = 10000
    puntos = generar_puntos(N)
    cant_punto_dentro_circulo = sum([analizar_punto(punto) for punto in puntos])
    cant_puntos_fuera_circulo = N - cant_punto_dentro_circulo
    relacion_circ_cuadrado = cant_punto_dentro_circulo / cant_puntos_fuera_circulo
    return 4*relacion_circ_cuadrado

if __name__ == "__main__":
    N = 10000
    #Rpta 5.3 estimá la probabilidad de que en un grupo de 30 personas elegidas al azar,
    #dos cumplan años el mismo día. 
    test(N, 30, verbose=True)
    
    #Rpta 5.3 II
    #¿podés calcular cuántas personas tiene que haber en un grupo para que sea más probable
    # que dos cumplan años el mismo día que que todas cumplan en días diferentes
    n_personas, probabilidad = CalcularMinimaProbabilidad(10000)
    print(f'Probabilidad minima: {probabilidad} con N_PERSONAS: {n_personas}')
    
    
        