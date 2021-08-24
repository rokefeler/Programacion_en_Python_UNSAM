# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 20:19:10 2021

@author: rokefeler@gmail.com
"""

#solucion_de_errores.py
#Ejercicios de errores en el código
#%%
#Ejercicio 3.1. Función tiene_a()
#Comentario: Es un Error de lógica; Bucle while solo itera una sola vez
# Porque si no empieza con 'a' minuscula simplemente devuelve False
# La corrección depende del objetivo de la función.
# ...Evaluará si Frase empieza con a, o que tenga la palabra a
# ...en este caso en base a nombre de funcion corregire si expresión tiene la letra "a"
#    A continuación va el código corregido
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        #else:
        #    return False
        i += 1
    return False #linea Agregada para corregir.

#a fin de evaluar y ver respuestas en consola, usamos funcion print
print(tiene_a('UNSAM 2020'))
print(tiene_a('abracadabra'))
print(tiene_a('La novela 1984 de George Orwell'))

#%%
#Ejercicio 3.2. Función tiene_a(), nuevamente
#Comentario: El error era de sintaxis
# ... definición de funcion no termina con :
# ... linea while le faltaba los ":"
# ... linea if tenia una asignación en lugar de una comparación, debe ser "=="
# ... Ult. linea decia return Falso, debio de decir return False.

#def tiene_a(expresion)
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n: #No tenia :
        #if expresion[i] = 'a' Error se esta asignando en lugar de Comparar ==
        if expresion[i] == 'a':
            return True
        i += 1
    #return Falso  Error detectado
    return False

print(tiene_a('UNSAM 2020'))
print(tiene_a('La novela 1984 de George Orwell'))

#%%
#Ejercicio 3.3. Función tiene_uno()
#Comentario: Se trata de un Error Semantico.
#... función trabaja bien cuando recibe una cadena
#... pero no funciona cuando se pasa un tipo entero
#... Una Solución generica sería Para solucionar esto basta con poner una validación del parametro que se recibe
# ... Si no se recibe una cadena que devuelva 
def tiene_uno(expresion):
    #debug print(repr(expresion))
    try:
        expresion = str(expresion)
    except e as Exception:
        return False
    #debug print(repr(expresion))

    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene

print(tiene_uno('UNSAM 2020'))
print(tiene_uno('La novela 1984 de George Orwell'))
print(tiene_uno(1984))
print(tiene_uno(['cadena1',20,'60']))

#%%
#Ejercicio 3.4. Función suma(a,b)
#Comentario: La siguiente suma no da lo que debería:
#Funcion no retorna el resultado

def suma(a,b):
    c = a + b
    return c #Linea Faltante

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")
#%%
#Ejercicio 3.5. Función leer_camion(nombre_archivo)
#Comentario: variable registro se asigna globalmente
#, es por esto que todos los valores de la lista apuntan
# al contenido del ultimo valor asignado a registro  
# Se soluciona definiendo una variable registro para cada iteración
import csv
import sys
from pprint import pprint

def leer_camion(nombre_archivo):
    print(sys.argv)
    camion=[]
    #registro={} #Variable Diccionario Global, esto ocasiona que por cada 
    with open(nombre_archivo,'rt') as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            #print(fila) para verificar que se este imprimiendo cada valor
            registro={} #Solucion
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)