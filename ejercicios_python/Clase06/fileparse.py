# -*- coding: utf-8 -*-
"""
#fileparse.py
Created on Mon Sep 13 22:30:38 2021

@author: rokefeler@gmail.com
"""

import csv
def parse_csv(nombre_archivo,select=None,types=[],has_headers=True):
    '''
    Parsea un archivo CSV en una lista de registros
    '''
    with open(nombre_archivo,'rt', encoding='utf8') as f:
        rows = csv.reader(f)     #Leer Archivo
        registros = []           #lo que se devolvera
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
        for row in rows:   #evaluar cada registro
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
    return registros
#%%
if __name__ == "__main__":
    #OK Lectura por Defecto, todo en string sin tipos
    camion = parse_csv('../Data/camion.csv')
    print(camion)
    #[{'nombre': 'Lima', 'precio': '32.2'}, {'nombre': 'Naranja', 'precio': '91.1'}, {'nombre': 'Caqui', 'precio': '103.44'}, {'nombre': 'Mandarina', 'precio': '51.23'}, {'nombre': 'Durazno', 'precio': '40.37'}, {'nombre': 'Mandarina', 'precio': '65.1'}, {'nombre': 'Naranja', 'precio': '70.44'}]
    #%%
    #OK se envia tipos de columnas
    camion = parse_csv('../Data/camion.csv',types=[str,int,float])
    print(camion)
    # #[{'nombre': 'Lima', 'cajones': 100, 'precio': 32.2}, {'nombre': 'Naranja', 'cajones': 50, 'precio': 91.1}, {'nombre': 'Caqui', 'cajones': 150, 'precio': 103.44}, {'nombre': 'Mandarina', 'cajones': 200, 'precio': 51.23}, {'nombre': 'Durazno', 'cajones': 95, 'precio': 40.37}, {'nombre': 'Mandarina', 'cajones': 50, 'precio': 65.1}, {'nombre': 'Naranja', 'cajones': 100, 'precio': 70.44}]
    #%%
    #OK Se pide solo ciertas columnas sin tipos, todo en string
    camion = parse_csv('../Data/camion.csv',select=['nombre','precio'])
    print(camion)
    #[{'nombre': 'Lima', 'precio': '32.2'}, {'nombre': 'Naranja', 'precio': '91.1'}, {'nombre': 'Caqui', 'precio': '103.44'}, {'nombre': 'Mandarina', 'precio': '51.23'}, {'nombre': 'Durazno', 'precio': '40.37'}, {'nombre': 'Mandarina', 'precio': '65.1'}, {'nombre': 'Naranja', 'precio': '70.44'}]
    #%%
    #OK Se pide solo ciertas columnas con sus tipos
    camion = parse_csv('../Data/camion.csv',select=['nombre','precio'],types=[str,float])
    print(camion)
    # #[{'nombre': 'Lima', 'precio': 32.2}, {'nombre': 'Naranja', 'precio': 91.1}, {'nombre': 'Caqui', 'precio': 103.44}, {'nombre': 'Mandarina', 'precio': 51.23}, {'nombre': 'Durazno', 'precio': 40.37}, {'nombre': 'Mandarina', 'precio': 65.1}, {'nombre': 'Naranja', 'precio': 70.44}]
    #%%
    #OK Se pide solo ciertas columnas con sus tipos
    camion = parse_csv('../Data/camion.csv',select=['nombre','cajones'],types=[str,int])
    print(camion)
    #[{'nombre': 'Lima', 'cajones': 100}, {'nombre': 'Naranja', 'cajones': 50}, {'nombre': 'Caqui', 'cajones': 150}, {'nombre': 'Mandarina', 'cajones': 200}, {'nombre': 'Durazno', 'cajones': 95}, {'nombre': 'Mandarina', 'cajones': 50}, {'nombre': 'Naranja', 'cajones': 100}]
    #%%
    #----------------------------Cambio de archivo Precios.csv
    #Al ASumir que hay Encabezados, devuelve datos erroneos, Error de Sintaxis
    camion = parse_csv('../Data/precios.csv')
    print(camion)
    # [{'Lima': 'Uva', '40.22': '24.85'}, {'Lima': 'Ciruela', '40.22': '44.85'}, {'Lima': 'Cereza', '40.22': '11.27'}, {'Lima': 'Frutilla', '40.22': '53.72'}, {'Lima': 'Caqui', '40.22': '105.46'}, {'Lima': 'Tomate', '40.22': '66.67'}, {'Lima': 'Berenjena', '40.22': '28.47'}, {'Lima': 'Lechuga', '40.22': '24.22'}, {'Lima': 'Durazno', '40.22': '73.48'}, {'Lima': 'Remolacha', '40.22': '20.75'}, {'Lima': 'Habas', '40.22': '23.16'}, {'Lima': 'Frambuesa', '40.22': '34.35'}, {'Lima': 'Naranja', '40.22': '106.28'}, {'Lima': 'Bruselas', '40.22': '15.72'}, {'Lima': 'Batata', '40.22': '55.16'}, {'Lima': 'Rúcula', '40.22': '36.9'}, {'Lima': 'Radicheta', '40.22': '26.11'}, {'Lima': 'Repollo', '40.22': '49.16'}, {'Lima': 'Cebolla', '40.22': '58.99'}, {'Lima': 'Cebollín', '40.22': '57.1'}, {'Lima': 'Puerro', '40.22': '27.58'}, {'Lima': 'Mandarina', '40.22': '80.89'}, {'Lima': 'Ajo', '40.22': '15.19'}, {'Lima': 'Rabanito', '40.22': '51.94'}, {'Lima': 'Zapallo', '40.22': '24.79'}, {'Lima': 'Espinaca', '40.22': '52.61'}, {'Lima': 'Acelga', '40.22': '29.26'}, {'Lima': 'Zanahoria', '40.22': '49.74'}, {'Lima': 'Papa', '40.22': '69.35'}]
    #%%
    camion = parse_csv('../Data/precios.csv',has_headers=False)
    print(camion) #OK
    #[('Lima', '40.22'), ('Uva', '24.85'), ('Ciruela', '44.85'), ('Cereza', '11.27'), ('Frutilla', '53.72'), ('Caqui', '105.46'), ('Tomate', '66.67'), ('Berenjena', '28.47'), ('Lechuga', '24.22'), ('Durazno', '73.48'), ('Remolacha', '20.75'), ('Habas', '23.16'), ('Frambuesa', '34.35'), ('Naranja', '106.28'), ('Bruselas', '15.72'), ('Batata', '55.16'), ('Rúcula', '36.9'), ('Radicheta', '26.11'), ('Repollo', '49.16'), ('Cebolla', '58.99'), ('Cebollín', '57.1'), ('Puerro', '27.58'), ('Mandarina', '80.89'), ('Ajo', '15.19'), ('Rabanito', '51.94'), ('Zapallo', '24.79'), ('Espinaca', '52.61'), ('Acelga', '29.26'), ('Zanahoria', '49.74'), ('Papa', '69.35')]
    #%%
    camion = parse_csv('../Data/precios.csv',types=[str,float],has_headers=False)
    print(camion)
    # #[('Lima', 40.22), ('Uva', 24.85), ('Ciruela', 44.85), ('Cereza', 11.27), ('Frutilla', 53.72), ('Caqui', 105.46), ('Tomate', 66.67), ('Berenjena', 28.47), ('Lechuga', 24.22), ('Durazno', 73.48), ('Remolacha', 20.75), ('Habas', 23.16), ('Frambuesa', 34.35), ('Naranja', 106.28), ('Bruselas', 15.72), ('Batata', 55.16), ('Rúcula', 36.9), ('Radicheta', 26.11), ('Repollo', 49.16), ('Cebolla', 58.99), ('Cebollín', 57.1), ('Puerro', 27.58), ('Mandarina', 80.89), ('Ajo', 15.19), ('Rabanito', 51.94), ('Zapallo', 24.79), ('Espinaca', 52.61), ('Acelga', 29.26), ('Zanahoria', 49.74), ('Papa', 69.35)]
    #%%
    
    