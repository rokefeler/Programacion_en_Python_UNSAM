# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 22:25:37 2021

@author: rokefeler@gmail.com
"""
#Ejercicio 7.10: Funciones y documentación

def valor_absoluto(n):
    '''Devuelve el Valor Absoluto de un numero.

    Pre: n es un numero Natural Entero o Float 
    Pos: Siempre devuelve el mismo numero que es >0
    Inv: return abs(n)    
    '''
    if n >= 0:
        return n
    else:
        return -n
#%%
def suma_pares(l):
    '''Suma todos los numeros pares de la lista l.

    Pre: l es una Lista de Enteros 
    Pos: res = SUMA( l[i] ), para todo l[i] que sea PAR
    '''
    res = 0             #Acumulador de Suma
    for e in l:
        if e % 2 ==0:
            res += e
        #else:   #Lineas insignificantes no alteran en nada, se pueden Eliminar
        #    res += 0

    return res 
#%%
def veces(a, b):
    '''Devuelve la suma de "b" veces del numero a.

    Pre: b, numero entero >=0
    Pos: res = a*b
    '''    
    res = 0  #Acumulador
    nb = b   #Variable de Control, se inicializa en la maxima Cant. de veces
    while nb != 0:
        #print(nb * a + res)
        res += a  #Incrementar Contador
        nb -= 1   #Disminuir Contador
    return res
#%%
def collatz(n, verbose=False):
    '''Devuelve La Cantidad de pasos para resolver la Conjetura
    de Collatz o Conjetura de ulam y llegar a 1

    Pre: n>0
    Pos: res = # de Iteraciones de Calcular: n=n//2 Si n es PAR, 
                                             n=3n+1 si n es IMPAR
    Inv: 
    '''        
    res = 1  # Numero de Pasos, inicializacion en 0

    while n!=1:
        
        if n % 2 == 0:  #si es Residuo es CERO, si es un numero PAR
            n = n//2   
            #print(f'n es PAR: n=n//2 : {n} ')
        else:
            n = 3 * n + 1
            #print(f'n NO ES PAR: n=3n+1 : {n} ')
        if verbose:
            print(f'{n}', end=',')
        res += 1
    if verbose:
        print(f'\nCant. de pasos: {res}')
    return res