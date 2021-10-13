# -*- coding: utf-8 -*-
"""
#fileparse.py
Created on Mon Sep 13 22:30:38 2021

@author: rokefeler@gmail.com
"""

import csv
import gzip
#%%
def read_data(iterable, select, types, has_headers, silence_errors):
    registros = []
    rows = csv.reader(iterable)     #Leer Archivo
    if has_headers:          # Si hay Encabezados
        headers = next(rows) # Lee los encabezados
        if select: #conventir los nombres de las columnas listadas en select a índices (posiciones) de columnas
            indices = [headers.index(ncolumna) for ncolumna in select]
            if not types:
                types = [str for ncolumna in select]
        else:      #si no hay Columnas, por defecto seran todas 
            select=headers
            indices = [i for i in range(len(headers))]  #Indices por defecto 
            if not types:
                types = [str for ncolumna in headers]
    for nfila,row in enumerate(rows,start=1):   #evaluar cada registro
        try:
            if not row:    # Saltea filas sin datos
                continue
            if has_headers:
                registro = { ncolumna: t(row[index]) for ncolumna, index, t in zip(select, indices,types)} 
            else:         #Si no tiene Headers, devolver una Tupla
                if types:
                    registro = (row[0], types[1](row[1]))
                else:
                    registro = (row[0], row[1])
            registros.append(registro)
        except ValueError as e:
            if not silence_errors:
                print(f'\tError: Fila{nfila} no puede convertir {str(row)}')
                print(f'\tMotivo:{e}')
    return registros
#%%
def parse_csv(iterable,select=None,types=[],has_headers=True,silence_errors=False):
    '''
    Parsea un archivo CSV en una lista de registros
    '''
    if select and not has_headers:
        raise RuntimeError('Para seleccionar, necesito encabezados.')
    #Otras posibles Validaciones
    # if  not isinstance(nombre_archivo,str):
    #     raise RuntimeError('Se Esperaba un tipo String para el parámetro nombre_archivo.')
    # if select!=None and not isinstance(select,list):
    #     raise RuntimeError('Se Esperaba un tipo List para el parámetro select')
    # if not isinstance(types,list):
    #     raise RuntimeError('Se Esperaba un tipo List para el parámetro types')
    registros = []           #lo que se devolvera
    registros=read_data(iterable,select,types,has_headers,silence_errors)
    return registros
#%%
if __name__ == "__main__":
    #Ejercicio 7.4: De archivos a "objetos cual archivos"
    nombre_archivo = '../Data/camion.csv.gz'
    camion=[]
    if nombre_archivo.lower().endswith('.csv.gz'):
        with gzip.open(nombre_archivo,'rt', encoding='utf8') as f:
            camion=parse_csv(f,types=[str,int,float])
    elif nombre_archivo.lower().endswith('.csv'):
        with open(nombre_archivo,'rt', encoding='utf8') as f:
            camion=parse_csv(f,types=[str,int,float])
    print(camion)
    