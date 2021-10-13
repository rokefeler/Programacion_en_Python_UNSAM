# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 22:41:24 2021

@author: rokefeler@gmail.com
"""

import os
import pandas as pd
#import seaborn as sns
#%%
directorio = '..\Data'
archivoParques = 'arbolado-en-espacios-verdes.csv'
archivoVeredas = 'arbolado-publico-lineal-2017-2018.csv'

fnameParques = os.path.join(directorio,archivoParques)
fnameVeredas = os.path.join(directorio,archivoVeredas)

especies_seleccionadas = ['Tipuana tipu', 'Tipuana Tipu']
#%%
#1 Abrí ambos datasets a los que llamaremos df_parques y df_veredas.
df_parques = pd.read_csv(fnameParques)
df_veredas = pd.read_csv(fnameVeredas)

#%%
#2 Para cada dataset armate otro seleccionando solamente las filas \
#    correspondientes a las tipas
columnas_sel_Parques = ['diametro','altura_tot']
columnas_sel_Veredas = ['diametro_altura_pecho','altura_arbol']

df_seleccion_parques = df_parques[ df_parques['nombre_cie'].isin(especies_seleccionadas) ]
df_seleccion_veredas = df_veredas[ df_veredas['nombre_cientifico'].isin(especies_seleccionadas) ]

df_tipas_parques = df_seleccion_parques[columnas_sel_Parques].copy()
df_tipas_veredas = df_seleccion_veredas[columnas_sel_Veredas].copy()

del df_seleccion_parques  #eliminar de memoria
del df_seleccion_veredas #eliminar de memoria
#- Renombrá las columnas que muestran la altura y el diámetro \
#    a la altura del pecho para que se llamen igual en ambos dataframes \
#    , para ello explorá el comando rename.
df_tipas_parques = df_tipas_parques.rename(columns={"altura_tot": "altura"})
df_tipas_veredas = df_tipas_veredas.rename(columns={"diametro_altura_pecho": "diametro", "altura_arbol": "altura"})

#%%
#   una columna llamada 'ambiente' que en un caso valga siempre 'parque' \
#   y en el otro caso 'vereda'.
df_tipas_parques['ambiente']='parque'
df_tipas_veredas['ambiente']='vereda'


#%%
#4. Juntá ambos datasets con el comando df_tipas = pd.concat([df_tipas_veredas, \
#  df_tipas_parques]). De esta forma tenemos en un mismo dataframe \
#  la información de las tipas distinguidas por ambiente.
df_tipas = pd.concat( [df_tipas_veredas, df_tipas_parques])

#%%
#5 Creá un boxplot para los diámetros a la altura del pecho de la tipas \
#  distinguiendo los ambientes (boxplot('diametro_altura_pecho',by = 'ambiente')).
df_tipas.boxplot('diametro', by = 'ambiente')

#%%
#6 Repetí para alturas.
df_tipas.boxplot('altura', by = 'ambiente')

#sns.boxplot(data = df_tipas, y = 'diametro', x = 'ambiente')
#sns.boxplot(data = df_tipas, y = 'altura', x = 'ambiente')

#%%
#7. ¿Qué tendrías que cambiar para repetir el análisis para otras especies? \
#   ¿Convendría definir una función?
# Bastaria cambiar datos de lista:
#  especies_seleccionadas = ['Tipuana tipu', 'Tipuana Tipu']