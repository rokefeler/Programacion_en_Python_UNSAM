# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 14:39:26 2021
Consigna: Estimá la probabilidad de que en un grupo de 30 personas elegidas al azar,
          dos cumplan años el mismo día. 
          Escribí un programita que permita calcular esa probabilidad asumiendo 
          que el año tiene 365 días.
@author: rokefeler@gmail.com
"""

#Source: https://www.pagina12.com.ar/347117-la-simulacion-de-monte-carlo
#Haga lo siguiente: 
#a. numere los días del año del 1 al 365 (suponiendo que no es un año bisiesto).
#   Por ejemplo, el número 1 es el 1 de enero y el 365 el 31 de diciembre. 
#b. Dígale al programa que elija 30 números entre esos 365 en forma aleatoria.
#   Este dato es vital: tienen que ser elegidos al azar. 
#c. Elige un número y lo repone a los 365 que tenía originalmente. 
#   De esta forma, entre los 30 números puede aparecer alguno repetido. 
#d. Cuando haya terminado el proceso y ya tiene estos 30 números fíjese 
#-justamente- si hay al menos algún par repetido, que corresponderían al mismo
# día del año. 
#e. Repita el proceso 10 mil veces (por supuesto, con la ayuda de una computadora). 
#   Fíjese en cuántos de los 10 mil casos de muestra aparecen números repetidos.
#f. Divida ese número por 10 mil. Verá que el número que obtiene 
#   es (aproximadamente) 0.7129… 
# ¿Cómo se interpreta esto? 
#Esto significa que con 30 personas en una habitación, 
#las chances de que haya dos que cumplan años el mismo día 
#¡supera el 71 por ciento!
import random
def escoger(calendario,n_dias_escoger=30):
    #n_dias_calendario = len(calendario)
    dias_aleatorios = random.choices(calendario, k = n_dias_escoger) #Resultado de n_dados lanzados
    #debug print(f'Resultado de tirar {n_dados} dados: {tirada}')
    return dias_aleatorios

def ejecutar_modelo(n_grupo=30, dias_calendario = 365):
    calendario = [x+1 for x in range(dias_calendario)]  #año Calendario del 1 al 365
    grupo_aleatorio = escoger(calendario,n_grupo)
    encontrados = dias_calendario*[0]
    for x in grupo_aleatorio:
        encontrados[x-1] += 1
    return len([x for x in encontrados if x>=2])>0
    #print(encontrados)
    
def test(N, n_grupo=30, verbose=False):
    #n_grupo = 30
    dias_calendario = 365
    G = sum([ejecutar_modelo(n_grupo, dias_calendario) for i in range(N)])
    prob = G/N
    if verbose:
        print(f'Se repitio {N} veces este Modelo, de las cuales salio {G} pares o más.')
        print(f'Podemos estimar la probabilidad mediante {prob:.6f}.')
    return prob

def CalcularMinimaProbabilidad(N):
    '''Minima Probabilidad que 2 personas cumplan años
       la probabilidad debe ser > 50%
    '''
    probabilidad = 0.0
    n_personas = 0
    while probabilidad<0.5:
        n_personas += 1
        probabilidad = test(N, n_personas)
    return (n_personas,probabilidad)
    
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
    
    
    