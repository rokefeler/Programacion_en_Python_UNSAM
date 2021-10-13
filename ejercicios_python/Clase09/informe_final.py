#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# informe_final.py

#%% ejercicio 7.7
import fileparse
import lote
import formato_tabla
#%%
def leer_camion(nombre_archivo):
    '''Computa el precio total del camion (cajones * precio) de un archivo'''
    with open(nombre_archivo) as f:
        camion_dicts = fileparse.parse_csv(f,\
                                     select = ['nombre', 'cajones', 'precio'], \
                                         types = [str, int, float], has_headers = True)
    camion = [lote.Lote(d['nombre'], d['cajones'], d['precio']) for d in camion_dicts]
    return camion
#%%
def leer_precios(nombre_archivo):
    with open(nombre_archivo) as f:
        precios = fileparse.parse_csv(f, types = [str, float], has_headers = False)
    return precios
#%%
def hacer_informe(camion, precios):
    lista = []
    for lote in camion:
        cambio = precios[lote.nombre] - lote.precio
        t = (lote.nombre, lote.cajones, lote.precio, cambio)
        lista.append(t)
    return lista
#%%
def imprimir_informe(informe,formateador):
    '''
    Imprime una tabla prolija desde una lista de tuplas
    con (nombre, cajones, precio, diferencia) 
    '''
    formateador.encabezado(['Nombre', 'Cantidad', 'Precio', 'Cambio'])    
    # print('    Nombre    Cajones     Precio     Cambio')
    # print('---------- ---------- ---------- ----------')
    for nombre, cajones, precio, cambio in informe:
        # precio = f'${precio}'
        rowdata = [nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}']
        formateador.fila(rowdata)
        # print(f'**{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}')
#%%
def informe_camion(nombre_archivo_camion, nombre_archivo_precios,fmt = 'txt'):
    '''
    Crea un informe a partir de un archivo de camión
    y otro de precios de venta.
    '''    
    # Leer archivos con datos
    camion = leer_camion(nombre_archivo_camion)
    lista_precios = leer_precios(nombre_archivo_precios)
    precios = dict(lista_precios)
    
    # Crear los datos para el informe
    informe = hacer_informe(camion, precios)
    
    # Imprimir el informe
    # Elige formato
    formateador = formato_tabla.crear_formateador(fmt)
    imprimir_informe(informe,formateador)
#%%
def f_principal(argumentos):
    if len(argumentos)<3:
        raise Exception('Faltan argumentos: Ejemplo informe_final.py <file_ruta_datos> <file_ruta_precios> <tipoSalida>'\
                        +'\n<tipoSalida> puede ser txt,csv o html (por defecto será txt)'\
                        +'\nEjemplo: informe_final.py ../Data/camion.csv ../Data/precios.csv txt')
    if len(argumentos)==3:
        argumentos.append('txt')
    informe_camion(argumentos[1], argumentos[2], argumentos[3])
#%%
if __name__ == '__main__':
    import sys
    f_principal(sys.argv)
    
    






