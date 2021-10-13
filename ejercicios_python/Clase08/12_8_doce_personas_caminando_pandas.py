# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 21:28:54 2021

@author: rokefeler@gmail.com
"""
import pandas as df

#Ejemplo: 12 personas caminando 8 horas
horas = 8
idx = pd.date_range('20200923 14:00', periods = horas*60, freq = 'min')
nombres = ['Pedro', 'Santiago', 'Juan', 'Andrés','Bartolomé','Tiago','Isca','Tadeo','Mateo','Felipe','Simón','Tomás']

df_walks = pd.DataFrame(np.random.randint(-1,2,[horas*60,12]).cumsum(axis=0), index = idx, columns = nombres)
df_walks.plot()

#Ahora suavizamos los datos, usando min_periods para no perder los datos de los extremos.

w = 45
df_walk_suav = df_walks.rolling(w, min_periods = 1).mean() # datos suavizados
nsuav = ['S_' + n for n in nombres]
df_walk_suav.columns = nsuav # cambio el nombre de las columnas
                             # para los datos suavizados
df_walk_suav.plot()

#Guardando datos
df_walk_suav.to_csv('caminata_apostolica.csv').