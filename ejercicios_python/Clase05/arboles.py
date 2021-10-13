# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 09:34:09 2021

@author: rokefeler@gmail.com
"""

import csv
import os
import matplotlib.pyplot as plt
import numpy as np
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
# def medidas_de_especies(especies,arboleda):
#     resultado = {}
#     for especie in especies:
#         arboles_filtrado = [ arbol for arbol in arboleda if arbol['nombre_com']==especie ]
#         arboles_alto_y_diametro = [ (arbol['altura_tot'],arbol['diametro'] ) for arbol in arboles_filtrado]
#         test = {}
#         test['nombre_com'] = especie
#         test['datos'] = arboles_alto_y_diametro
        
#         resultado.pop(test)
        
#     return resultado
#%%
def medidas_de_especies(especies,arboleda):
    #return {especie:[ (arbol['altura_tot'],arbol['diametro'] ) for arbol in arboleda if arbol['nombre_com']==especie ] for especie in especies }
    #para Ejercicio de cap.5 piden diametro, altura
    return {especie:[ (arbol['diametro'],arbol['altura_tot'] ) for arbol in arboleda if arbol['nombre_com']==especie ] for especie in especies }
#%%
#Ejercicio 5.25: Histograma de altos de Jacarandás
def histograma(altos, nbins=50, title='Histograma'):
    promedio = np.mean(altos)
    plt.hist(altos, bins=nbins)
    plt.axvline(promedio, color='r')
    plt.legend(["%.2f Altura" % promedio])
    plt.title(title)
    plt.show()
#%%
#Ejercicio 5.26: Scatterplot (diámetro vs alto) de Jacarandás
def scatter_hd(lista_de_pares, title='Relación diámetro-alto para Jacarandá'):
    # d = [i[0] for i in lista_de_pares]
    # h = [i[1] for i in lista_de_pares]
    pares = np.array(lista_de_pares)
    d = np.array(pares)[:,0] #Corte solo 
    h = np.array(pares)[:,1]
    colors = np.random.rand(len(d))
    #area = (20 * np.random.rand(len(d)))**2  # 0 to 15 point radii
    plt.figure()
    plt.xlabel("diametro (cm)")
    plt.ylabel("alto (m)")
    plt.title(title)
    plt.scatter(d, h, c=colors, alpha=0.5)
    
#%%
if __name__ == "__main__":
    cfile = '../Data/arbolado-en-espacios-verdes.csv'
    arboleda = leer_arboles(cfile)
    
    #Ejercicio 4.16: Lista de altos de Jacarandá
    arbol_to_test = 'Jacarandá'
    arboles_filtrado = [arbol for arbol in arboleda if arbol['nombre_com']==arbol_to_test]
    arboles_altura=[arbol['altura_tot'] for arbol in arboles_filtrado]
    
    #Ejercicio 4.17: Lista de altos y diámetros de Jacarandá
    arboles_alto_y_diametro = np.array( [(arbol['altura_tot'],arbol['diametro'] ) for arbol in arboles_filtrado] )
    
    #Ejercicio 5.25: Histograma de altos de Jacarandás
    histograma(arboles_altura,title='Alturas Jacarandá')
    
    
    #Ejercicio 5.26: Scatterplot (diámetro vs alto) de Jacarandás
    arboles_diametro_altura = [(arbol['diametro'],arbol['altura_tot'] ) for arbol in arboles_filtrado]    
    scatter_hd(arboles_diametro_altura)
    
    #Ejercicio 5.27: Scatterplot para diferentes especies
    especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
    medidas = medidas_de_especies(especies, arboleda)
    for especie in especies:
        scatter_hd(medidas[especie],'Relación diámetro-alto para ' + especie)
    #preguntas
    #¿Se mantienen las relaciones que viste en el ejercicio anterior para las tres especies?
    # No se mantienen . varian
    #¿Hay diferencias entre las especies? , SI pero es poca
    #¿cuál tiene mayor diámetro (tipicamente)?, el Eucalipto, tambien es mas Alto   
        
    #Falta tiempo para las demas pero las completare, Gracias
    
    
    

    #%%-----------Semana 5
    
    
    
    
