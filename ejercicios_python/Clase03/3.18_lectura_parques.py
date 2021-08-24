# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 20:09:10 2021

@author: FamiliaRoqueSosa
"""
import csv
from pprint import pprint
from collections import Counter
#%%
#Ejercicio 3.18: Lectura de los árboles de un parque
def leer_parque(nombre_archivo, parque):
    '''devuelva una lista de diccionarios con la información 
    del parque especificado. 
    La función debe devolver, en una lista un diccionario con todos los datos 
    por cada árbol del parque elegido 
    (recordá que cada fila del csv es un árbol).
    '''
    arboles=[]
    if(parque==''):
        parque='*'
    else:
        parque=parque.upper()
        
    #print(nombre_archivo)
    try:
        with open(nombre_archivo,'rt',encoding='utf8') as f: 
            try:
                rows = csv.reader(f)
                #print(rows)
                headers=next(rows)
                #print(headers)
                for row in rows:
                    try:
                        record=dict(zip(headers,row))
                        #print(record)
                        record['long']  = float(record['long'])
                        record['lat']  = float(record['lat'])
                        
                        
                        record['id_arbol'] = int(record['id_arbol'])
                        record['altura_tot'] = int(record['altura_tot'])
                        record['diametro'] = int(record['diametro'])
                        record['inclinacio'] = int(record['inclinacio'])
                        record['id_especie'] = int(record['id_especie'])

                        record['coord_x']  = float(record['coord_x'])
                        record['coord_y']  = float(record['coord_y'])   
                        #if(parque=='' or parque=='*'):
                        #    arboles.append(record)
                        #elseif(record['espacio_ve'].lower() == parque.lower()):
                        if(record['espacio_ve'].upper() == parque or parque=='*'):
                            arboles.append(record)
                    except Exception as e:
                        #pass
                        print(e)
            except ValueError as v:
                #pass
                print(v)
    except FileNotFoundError:
        print(f'ERROR: {nombre_archivo} No existe, intente ingresar nombre de archivo correcto')
    except Exception as e:
        print(e)
    return arboles

#%%
#Ejercicio 3.19: Determinar las especies en un parque

def especies(lista_arboles):
    '''  devuelva el conjunto de especies 
    (la columna 'nombre_com' del archivo) que figuran en la lista
    '''
    especies = set()
    for arbol in lista_arboles:
        especies.add(arbol['nombre_com'].upper())
    return list(especies)

#%%
#Ejercicio 3.20: Contar ejemplares por especie    
def contar_ejemplares(lista_arboles):
    lista_especies = especies(lista_arboles) #seran keys
    #print(lista_especies)
    lista_cant_especies = Counter()
    
    for s in lista_especies:
        lista_cant_especies[s]=0 #Inicializamos
        
        for arbol in lista_arboles:
            #print(f"arbol:{arbol['nombre_com']}, especie:{s}")
            if(arbol['nombre_com'].upper()==s):
                lista_cant_especies[s]+=1
                #item[arbol['nombre_com']] += 1
        
    return lista_cant_especies

cfile = '../Data/arbolado-en-espacios-verdes.csv'

lista_parques = ['General Paz','ANDES, LOS','centenario']

for nombre_parque in lista_parques:
    print(f'PARQUE {nombre_parque.upper():60s}')
    print('{:<80s}'.format(60*'=') )
    
    lista_arboles = leer_parque(cfile, nombre_parque)
    print(f'Hay {len(lista_arboles)} arboles en {nombre_parque}')
    lista_especies = especies(lista_arboles)
    print(f'Hay {len(lista_especies)} especies en el parque:en {nombre_parque}')
    
    listado_contar_arboles = contar_ejemplares(lista_arboles)
    print(f'Las 5 Especies mas frecuentes del Parque: {nombre_parque} son:')
    for item in listado_contar_arboles.most_common(5):
        print(f'{item[0].capitalize()}: {item[1]}')
    print('{:<80s}'.format(60*'-') )