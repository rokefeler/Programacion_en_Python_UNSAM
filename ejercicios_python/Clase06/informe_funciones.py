# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 20:54:46 2021

@author: rokefeler@gmail.com
"""

import csv
import os
from fileparse import parse_csv

def leer_camion(nombre_archivo):
    camion=parse_csv(nombre_archivo, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
    return camion
 
#%%
def leer_precios(nombre_archivo):
    lista_precios=parse_csv(nombre_archivo, types = [str, float], has_headers = False)
    return dict(lista_precios)
#%%
def hacer_informe(camion, precios):
    lista = []
    for lote in camion:
        precio_venta = precios[lote['nombre']]
        cambio = precio_venta - lote['precio']
        t = (lote['nombre'], lote['cajones'], precio_venta, cambio)
        lista.append(t)
    return lista
#%%
def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    camion=leer_camion(nombre_archivo_camion)
    precios=leer_precios(nombre_archivo_precios)
    informe = hacer_informe(camion, precios)
    
    totalCostoCamion = sum([s['cajones'] * s['precio'] for s in camion])
    totalVentaCamion = sum([s['cajones'] * precios[s['nombre']] for s in camion])
    
    headers=('Nombre','Cajones','Precio','Cambio')
    print('%10s %10s %10s %10s'  % headers)
    print(('-' * 10 + ' ') * len(headers))

    
    # for row in informe:
    #     print('%10s %10d %10.2f %10.2f' % row)
    for nombre, cajones, precio, cambio in informe:
        precio = f'${precio}'
        print(f'{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}')
       

    print(f'Total Costo Camión: {round(totalCostoCamion,2):0.2f}')
    print(f'Total Recaudación Venta Camión: {round(totalVentaCamion,2):0.2f}')
    if(totalCostoCamion==totalVentaCamion):
        print('EL IMPORTE RECAUDADO DE LA VENTA ES IGUAL AL COSTO DEL CAMION, EXISTE PERDIDA DE FLETE U TRASLADOS')
    elif(totalVentaCamion>totalCostoCamion):
        print(f'Existe una Diferencia(Ganancia) de: {round(totalVentaCamion-totalCostoCamion,2):0.2f}')
    else:
        print(f'Existe una Diferencia(Perdida) de: {round(totalCostoCamion-totalVentaCamion,2):0.2f}')
#%%
if __name__ == "__main__":
    files = ['../Data/camion.csv', '../Data/camion2.csv']
    cfile_archivo_precios = os.path.join('../Data/precios.csv')
    for name in files:
        print(f'{name:-^43s}')
        cfile_archivo_camion = os.path.join(name)
        informe_camion(name, cfile_archivo_precios)
        print()
    