#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: rgrimson
"""

#%% Archivos

f = open('../Data/arboles.csv', 'rt',encoding='utf8'  )
data = f.read()
print(data)

#%%
f.close()

#%%

nombre_archivo = '../Data/arboles.csv'
with open(nombre_archivo, 'rt',encoding='utf8') as archivo:
    for i, linea in enumerate(archivo):
        print(i, linea,end='')
f.close()
#%%

#f = open('../Data/arboles.csv', 'rt')
# o si hace falta aclararlo en tu SO
f = open('../Data/arboles.csv', 'rt', encoding='utf8') 
encabezados = next(f).split(',')
encabezados

#%%

for line in f:
    fila = line.split(',')
    print(fila)

#%%

encabezados
fila
f.close()
#%% zip

l=[]
f = open('../Data/arboles.csv', 'rt', encoding='utf8')
encabezados = next(f).split(',')
for line in f:
    fila = line.split(',')
    #print(fila)
    registro = dict(zip(encabezados, fila))
    l.append(registro)
print(l)
f.close()

#%%

f = open('../Data/arboles.csv', 'rt', encoding='utf8') 
encabezados = next(f).split(',')
for line in f:
    fila = line.split(',')
    for e,d in zip(encabezados,fila):
        el = e.strip("\n")
        dl = d.strip("\n")
        print(f'{el:>12s}: {dl}')
    print()
f.close()


#%%

f = open('../Data/arboles.csv', 'rt', encoding='utf8') 
#f = open('../Data/camion.csv', 'rt', encoding='utf8')
encabezados = next(f).strip("\n").split(',')
arboles = []
for line in f:
    fila = line.strip("\n").split(',')
    arbol = {}
    print(zip(encabezados,fila))
    for e,d in zip(encabezados,fila):
        arbol[e]=d
    arboles.append(arbol)
print(arboles)    
f.close()    