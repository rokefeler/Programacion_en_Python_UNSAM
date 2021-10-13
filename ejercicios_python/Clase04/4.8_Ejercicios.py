# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 22:22:28 2021

@author: rokefeler@gmail.com
"""

#Ejercicio 4.7: Comprensión de listas
nums = [1,2,3,4]
cuadrados = [x*x for x in nums]
#[1, 4, 9, 16]

dobles = [2*x for x in nums if x>2]
#[6, 8]

#%%
# Ejercicio 4.8: Reducción de secuencias
import informe

camion = leer_camion('../Data/camion.csv')
precios = leer_precios('../Data/precios.csv')
costo = sum([s['cajones'] * s['precio'] for s in camion])
valor = sum([s['cajones'] * precios[s['nombre']] for s in camion])
print(f'Costo:{costo}')
print(f'Valor:{valor}')

[s['cajones'] * s['precio'] for s in camion]
#[3220.0000000000005, 4555.0, 15516.0, 10246.0, 3835.1499999999996, 3254.9999999999995, 7044.0]
sum(_)
#47671.15

#%%
#precios = leer_precios('../Data/precios.csv')