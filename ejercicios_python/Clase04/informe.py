# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 12:51:39 2021

@author: rokefeler@gmail.com
"""


import csv
from pprint import pprint
import locale

def leer_camion(nombre_archivo):
    productos=[]
    try:
        with open(nombre_archivo) as f: 
            try:
                rows = csv.reader(f)
                headers=next(rows)
                for row in rows:
                    try:
                        record=dict(zip(headers,row))
                        record['nombre']  = record['nombre'].lower().strip()
                        record['cajones'] = int(record['cajones'])
                        record['precio']  = float(record['precio'])
                        productos.append(record)
                    except Exception as e:
                        pass
            except ValueError:
                pass
    except FileNotFoundError:
        print(f'ERROR: {nombre_archivo} No existe, intente ingresar nombre de archivo correcto')
    except Exception as e:
        print(e)
    return productos
 

def leer_precios(nombre_archivo):
    precios={}
    try:
        with open(nombre_archivo) as f: 
            rows = csv.reader(f)
            header=['nombre','precio']
            for row in rows:
                try:
                    record=dict(zip(header,row))
                    record['nombre']  = record['nombre'].lower().strip()
                    record['precio']  = float(record['precio'])
                    precios[record['nombre']] = record['precio']
                except Exception as e:
                    pass 
    except FileNotFoundError:
        print(f'ERROR: {nombre_archivo} No existe, intente ingresar nombre de archivo correcto')
    except Exception as e:
        print(e)
    return precios
 

def hacer_informe(camion,precios):
    datos_informe=[] 
    for item in camion:
        try:
            reg_tupla = ( item['nombre'].capitalize(), item['cajones'], listaprecios[item['nombre']], listaprecios[item['nombre']]-item['precio'] )
            datos_informe.append(reg_tupla)
        except Exception as e:
            pass
    return datos_informe

if __name__ == "__main__":
    productos=leer_camion('../Data/camion.csv') #Datos del camion, precios pagados al productor
    listaprecios=leer_precios('../Data/precios.csv') #Lista de Precios de venta
    informe = hacer_informe(productos, listaprecios)
    
    headers=('Nombre','Cajones','Precio','Cambio')
    print('{0[0]:>10s} {0[1]:>10s} {0[2]:>10s} {0[3]:>10s}'.format(headers) )
    print('{:<10s} {:10s} {:10s} {:10s}'.format(10*'-',10*'-',10*'-',10*'-'))
    
    for nombre, cajones, precio, cambio in informe:
        precio = '$'+str(precio)
        print(f'{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}')
    
