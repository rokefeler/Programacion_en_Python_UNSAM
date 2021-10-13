# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 10:10:09 2021

@author: rokefeler@gmail.com
"""

import csv
#%%
#Ejercicio  4.15: Lectura de todos los árboles
def leer_arboles(nombre_archivo):
    '''devuelva una lista de diccionarios con la información de todos 
    los árboles en el archivo.
    '''
    arboles=[]
    types = [float,float,int,int,int,int,int,str,str,str,str,str,str,str,str,float,float]
    
    try:
        with open(nombre_archivo,'rt',encoding='utf8') as f: 
            try:
                rows = csv.reader(f)
                headers=next(rows)
                for row in rows:
                    
                    try:
                        if row:
                            converted = [func(val) for func, val in zip(types, row)]
                            record = dict(zip(headers, converted))
                            arboles.append(record)
                    except Exception as e:
                        pass
            except ValueError as v:
                pass
    except FileNotFoundError:
        print(f'ERROR: {nombre_archivo} No existe, intente ingresar nombre de archivo correcto')
    except Exception as e:
        print(e)
    return arboles
#%%
def medidas_de_especies(especies,arboleda):
    resultado = {}
    for especie in especies:
        arboles_filtrado = [ arbol for arbol in arboleda if arbol['nombre_com']==especie ]
        arboles_alto_y_diametro = [ (arbol['altura_tot'],arbol['diametro'] ) for arbol in arboles_filtrado]
        test = {}
        test['nombre_com'] = especie
        test['datos'] = arboles_alto_y_diametro
        resultado.pop(test)
    return resultado
#%%
def medidas_de_especies2(especies,arboleda):
    resultado = []
    for especie in especies:
        arboles_filtrado = [ arbol for arbol in arboleda if arbol['nombre_com']==especie ]
        arboles_alto_y_diametro = [ (arbol['altura_tot'],arbol['diametro'] ) for arbol in arboles_filtrado]
        test = {}
        test['nombre_com'] = especie
        test['datos'] = arboles_alto_y_diametro
        resultado.append(test)
    return resultado
#diccionario = { clave: valor for clave in claves }
#%%
if __name__ == "__main__":
    cfile = '../Data/arbolado-en-espacios-verdes.csv'
    arboleda = leer_arboles(cfile)
    
#%%    
    #Ejercicio 4.16: Lista de altos de Jacarandá
    arbol_to_test = 'Jacarandá'
    arboles_filtrado = [arbol for arbol in arboleda if arbol['nombre_com']==arbol_to_test]
    arboles_altura=[arbol['altura_tot'] for arbol in arboles_filtrado]

#%%    
    #Ejercicio 4.17: Lista de altos y diámetros de Jacarandá
    arboles_alto_y_diametro = [(arbol['altura_tot'],arbol['diametro'] ) for arbol in arboles_filtrado]
    
    #Ejercicio 4.18: Diccionario con medidas
    especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
    testdiccionario =  medidas_de_especies(especies,arboleda)
    #%%
    #test para imprimir solo primer registro
    print (testdiccionario[0]['nombre_com']) #imprimir nombre clave
    print (testdiccionario[0]['datos'])      #imprimir valors (alto,diametro)
    
