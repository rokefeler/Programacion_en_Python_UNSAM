# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 23:49:04 2021

@author: rokefeler@gmail.com
"""

import pandas as pd
#%%
df = pd.read_csv('../Data/OBS_SHN_SF-BA.csv',)
df.head()
df.index
#%%
#volvemos a cargar pero ahora el indice es columna Time y que parsee fechas
df = pd.read_csv('../Data/OBS_SHN_SF-BA.csv', index_col=['Time'], parse_dates=True)

df.head()
df.index
#%%
# imprimir un rango de horas
df['1-18-2014 9:00':'1-18-2014 18:00']

#slice, solo de esta fecha y grafica correspondiente
df['12-25-2014':]
df['12-25-2014':].plot()

#%%
#El siguiente comando genera un gráfico entre el 15 de octubre de 2014 y \
# el 15 de diciembre del mismo año.
df['10-15-2014':'12-15-2014'].plot()

#%% Ejercicio 8.10:
'''La transformada de Fourier no resultará muy útil para ver estas ondas de 
 tormenta. Como carecen de regularidad, no aparecerán claramente en el espectro 
 de frecuencias.
'''    
dh = df['12-25-2014':].copy()

delta_t = 0 # tiempo que tarda la marea entre ambos puertos
delta_h = 0 # diferencia de los ceros de escala entre ambos puertos

'''Podemos desplazar (shift en inglés) una Serie de Pandas usando el 
método ds.shift(pasos)'''
pd.DataFrame([dh['H_SF'].shift(delta_t) - delta_h, dh['H_BA']]).T.plot()

