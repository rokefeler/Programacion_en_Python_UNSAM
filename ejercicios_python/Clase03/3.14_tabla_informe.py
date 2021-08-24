# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 12:51:39 2021

@author: rokefeler@gmail.com
"""


import csv
from pprint import pprint
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
    #headers=('Nombre','Cajones','Precio','Cambio')
    datos_informe=[] 
    #debe contener tuplas 
    #Nombre     Cajones     Precio     Cambio
    for item in camion:
        try:
            reg_tupla = ( item['nombre'].capitalize(), item['cajones'], listaprecios[item['nombre']], listaprecios[item['nombre']]-item['precio'] )
            datos_informe.append(reg_tupla)
        except Exception as e:
            pass
    return datos_informe
    #return dict(zip(headers,datos_informe))

productos=leer_camion('../Data/camion.csv') #Datos del camion, precios pagados al productor
listaprecios=leer_precios('../Data/precios.csv') #Lista de Precios de venta
informe = hacer_informe(productos, listaprecios)

for r in informe:
    print('%10s %10d %10.2f %10.2f' % r)

print()
print('impresion utilizando f-strings.')
for nombre, cajones, precio, cambio in informe:
    print(f'{nombre:>10s} {cajones:>10d} {precio:>10.2f} {cambio:>10.2f}')    

