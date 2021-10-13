# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 20:17:24 2021

@author: rokefeler@gmail.com
"""
#Ejercicio 5.7: arange() y linspace()
import numpy as np
#Generá un vector que tenga los números impares entre el 1 y el 19 inclusive usando arange()
a = np.arange(1,20,2)
print(f'a:{a}')

#Repetí el ejercicio usando linspace().
b = np.linspace(1, 19, num=10)
print(f'b: {b}')

#¿Qué diferencia hay en el resultado?
#Array b es de tipo float

x = np.ones(2, dtype=np.int64)
print(f'x ones: {x}')

