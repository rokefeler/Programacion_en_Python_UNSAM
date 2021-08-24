# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 15:19:30 2021

@author: rokefeler@gmail.com
"""
print('    ',end='')
#Imprimir Cabecera 0 1 2 ... 9
for c in range(10):
    print(f'{c:6d}',end='')
print() #Salto de linea
#Imprimir Guiones
print('{:<10s}'.format((6*11-1)*'-'))

#Imprimir Tabla de Multiplicar
mul=0
for i in range(10):
    print(f'{i:3d}:',end='') #Imprimir numero de Fila con :
    mul=0                         #Siempre inicia en 0
    for j in range(10):
        #print(f'{round(i*j,2):6d}',end='') #usando multiplicacion
        print(f'{mul:6d}',end='') #utilizando solo acumulador con sumas
        mul = mul + i             #acumulador sumarle numero de la tabla 
    print()    #Salto de Linea
