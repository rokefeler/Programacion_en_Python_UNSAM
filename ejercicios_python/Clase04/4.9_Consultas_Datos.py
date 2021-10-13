# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 22:36:31 2021

@author: rokefeler@gmail.com
"""
import informe

#generá una lista con la info de todas las frutas que tienen más de 100 cajones en el camión.
masde100 = [x for x in camion if x['cajones']>100]
#[{'nombre': 'caqui', 'cajones': 150, 'precio': 103.44},
#{'nombre': 'mandarina', 'cajones': 200, 'precio': 51.23}]


#O una con la info de las frutas que costaron más de $10000.
myn = [s for s in camion if s['nombre'].capitalize() in {'Mandarina','Naranja'}]
# [{'nombre': 'naranja', 'cajones': 50, 'precio': 91.1},
#  {'nombre': 'mandarina', 'cajones': 200, 'precio': 51.23},
#  {'nombre': 'mandarina', 'cajones': 50, 'precio': 65.1},
#  {'nombre': 'naranja', 'cajones': 100, 'precio': 70.44}]

#O una con la info de las frutas que costaron más de $10000.
costo10k = [x for x in camion if x['cajones']*x['precio']>10000]
# [{'nombre': 'caqui', 'cajones': 150, 'precio': 103.44},
#  {'nombre': 'mandarina', 'cajones': 200, 'precio': 51.23}]

#%%Ejercicio 4.10: Extracción de datos
'''
Usando un comprensión de listas, construí una lista de tuplas (nombre, cajones) 
que indiquen la cantidad de cajones de cada fruta tomando los datos de camion
'''
nombre_cajones =[(s['nombre'], s['cajones']) for s in camion]
# [('lima', 100),
#  ('naranja', 50),
#  ('caqui', 150),
#  ('mandarina', 200),
#  ('durazno', 95),
#  ('mandarina', 50),
#  ('naranja', 100)]

#%%
# Si cambiás los corchetes ([,]) por llaves ({, }), obtenés algo 
''' que se conoce como comprensión de conjuntos. 
Vas a obtener valores únicos.'''

# Por ejemplo, si quisieras un listado de las frutas en el 
# camión pordías usar:
nombres = {s['nombre'] for s in camion}
for s in camion:
    stock[s['nombre']] += s['cajones']