# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 17:14:43 2021

@author: Sistemas
"""
#Ejercicio 7.6: Sumas implementando un ciclo
def sumar_enteros(desde, hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    Inv: sum = (hasta*(hasta+1)/2) - (desde*(desde+1)/2) + (desde if desde>0 and hasta>0 else hasta if desde<0 and hasta<0 else 0)
    '''
    
    if hasta<desde:  #invariante de ciclo
        return 0
    
    return sum([i for i in range(desde,hasta+1)])

#Ejercicio 7.6: Sumas, implementando tiempo constante
def sumar_enteros2(desde, hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
    
    if hasta<desde:
        return 0
    
    n    = abs(desde)
    sum1 = (n*(n+1))//2  #Calculo de primer Rango
    
    n    = abs(hasta)
    sum2 = n*(n+1)//2    #Calculo de segundo rango
    
    if desde>0 and hasta>0:
        sum2 += desde
    elif desde<0 and hasta<0:
        sum2 += hasta
    return sum2-sum1
    #return sum2-sum1 + (desde if desde>0 and hasta>0 else hasta if desde<0 and hasta<0 else 0)
    #implementación utilizando un ciclo

#Test en Rango de enteros
desde=15
hasta=150
assert(sumar_enteros(desde,hasta) == sumar_enteros2(desde,hasta) )

#Test desde un Negativo a un Positivo
desde=-151
hasta=150
assert(sumar_enteros(desde,hasta) == sumar_enteros2(desde,hasta) )


#Test en Rango de Negativos
desde=-100
hasta=-50
assert(sumar_enteros(desde,hasta) == sumar_enteros2(desde,hasta) )


#Test en Rango de n primeros numeros positivos
desde=0
hasta=50
assert(sumar_enteros(desde,hasta) == sumar_enteros2(desde,hasta) )

#Test en Rango de n primeros numeros negativos
desde=-50
hasta=0
assert(sumar_enteros(desde,hasta) == sumar_enteros2(desde,hasta) )