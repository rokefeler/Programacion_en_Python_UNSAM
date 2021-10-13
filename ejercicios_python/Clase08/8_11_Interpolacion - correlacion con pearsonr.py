# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 10:42:34 2021

@author: rokefeler@gmail.com
"""
import numpy as np
import pandas as pd
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
#%%

#Ejercicio 8.11: Interpolación
'''Este ejemplo muestra una manera de interpolar la serie de manera de 
poder usar desplazamientos menores a una hora.'''

# Cada cuarto de hora
df=pd.read_csv('../Data/OBS_SHN_SF-BA.csv',index_col=['Time'],parse_dates=True)
dh =df['10-01-2014':].copy() #ultimo trimestre
freq_horaria = 30 # 4 para 15min, 60 para 1min
cant_horas = 24
N = cant_horas * freq_horaria

#resampleo cada tantos minutos
dh = dh.resample(f'{int(60/freq_horaria)}T').mean()

#rellenos los NaNs suavemente
dh =dh.interpolate(method='quadratic')

# genero vector de desplazamientos (enteros)
ishifts = np.arange(-N,N+1)
# y su desplamiento horario asociado
shifts=ishifts/freq_horaria

# finalmente calculo las correlaciones correspondientes
corrs = np.zeros(shifts.shape)
for i, sh in enumerate(ishifts):
    corrs[i] = pearsonr(dh['H_SF'].shift(sh)[N:-N], dh['H_BA'][N:-N])[0]
# y grafico
plt.plot(shifts, corrs)

coordMaximaCorrelacion=np.argmax(corrs)
print(coordMaximaCorrelacion)