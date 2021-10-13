# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 22:13:22 2021

@author: rokefeler@gmail.com
"""

import pandas as pd
import os
import seaborn as sns
#%%
directorio = '..\Data'
archivo = 'arbolado-publico-lineal-2017-2018.csv'
fname = os.path.join(directorio,archivo)
df = pd.read_csv(fname)
cols_sel = ['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol']
df_lineal = df[cols_sel]

#%%
#Imprimí las diez especies más frecuentes con sus respectivas cantidades.
print('las diez especies mas frecuentes son:')
print(df_lineal['nombre_cientifico'].value_counts().head(10))


especies_seleccionadas = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']
df_lineal_seleccion = df_lineal[ df_lineal['nombre_cientifico'].isin(especies_seleccionadas) ]
#%%
#Ejercicio 8.8: Boxplots
df_lineal_seleccion.boxplot('diametro_altura_pecho', by = 'nombre_cientifico')

#Realizá un gráfico similar pero de los altos en lugar de los diámetros de los árboles.
df_lineal_seleccion.boxplot('altura_arbol', by = 'nombre_cientifico')

#%%
#Ejemplo de pairplot
sns.pairplot(data = df_lineal_seleccion[cols_sel], hue = 'nombre_cientifico')