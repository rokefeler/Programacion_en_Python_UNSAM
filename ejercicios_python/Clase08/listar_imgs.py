# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 23:06:51 2021

@author: rokefeler@gmail.com
"""
import os
import sys
#%%
def archivos_png(directorio):
    ''' arme una lista de todos los archivos .png que se encuentren 
    en algún subdirectorio directorio dado
    '''
    directorio = os.path.normpath(directorio) #normalizar directorio, para multiples os
    listado=[]
    for root, dirs, files in os.walk(directorio):
        for name in files:
            if name.lower().endswith('.png'):  #si es del tipo .png agregarlo
                listado.append(name)
        for name in dirs:
            rutaFile = os.path.join(root, name)
            if os.path.isfile(rutaFile):
                listado.append(name)
    return list(set(listado))  #retornar elementos que no sean duplicados
#%%
if __name__ == "__main__":
    if len(sys.argv)>=2:
        ruta = sys.argv[1] #procesar ruta enviada
    else:
        ruta = os.getcwd()  #procesar ruta actual
        
    res=archivos_png(ruta)
    print(f'Analisis de directorio: {ruta}')
    print(res)