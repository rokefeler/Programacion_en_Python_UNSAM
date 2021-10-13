# -*- coding: utf-8 -*-
"""
#Ejercicio 8.6: Ordenar el árbol de archivos (optativo)
Created on Fri Oct  8 00:47:28 2021

@author: rokefeler@gmail.com
"""

import os
import datetime
import shutil
import sys
#%%
def ObtenerListaArchivos_png(directorio):
    ''' arme una lista de todos los archivos .png que se encuentren 
    en algún subdirectorio directorio dado
    '''
    directorio = os.path.normpath(directorio) #normalizar directorio, para multiples os
    listado=[]
    for root, dirs, files in os.walk(directorio):
        for name in files:
            if name.lower().endswith('.png'):  #si es del tipo .png agregarlo
                listado.append(os.path.join(root, name))
        for name in dirs:
            rutaFile = os.path.join(root, name)
            if os.path.isfile(rutaFile):
                listado.append(rutaFile)
    return list(set(listado))  #retornar elementos que no sean duplicados
#%%
def ObtenerListaSubDirectorios(directorio):
    ''' Arma una Lista de Subdirectorios co sus rutas completas
    '''
    directorio = os.path.normpath(directorio) #normalizar directorio, para multiples os
    listado=[]
    for root, dirs, files in os.walk(directorio):
        for name in dirs:
            rutaFile = os.path.join(root, name)
            if os.path.isdir(rutaFile):
                listado.append(rutaFile)
    return list(set(listado))  #retornar elementos que no sean duplicados
#%%
def procesar_nombre(fname):
    '''
    Permite procesar archivos que tengan en formato nombre_AAAAMMDD.png

    Parameters
    ----------
    fname : string
        últ. 8 carac de su nombre estan en el formato 
        AAAAMMDD (año en 4 dígitos, mes en 2 y día en 2).

    Returns
    -------
    result : tupla(string,datetime) o None
        devuelve (nombre, fecha)
    '''
    result=None
    try:
        fecha   = fname[-12:][:8]
        dfecha  = datetime.datetime.strptime(fecha,'%Y%m%d')
        archivo = fname[:(len(fname)-13)]+fname[-4:]
        result  = (archivo,dfecha)
        #print(f'tupla:({archivo}, {dfecha})')
    except ValueError:
        raise ValueError('Archivo no cumple formato name_AAAAMMDD.png') 
    return result
#%%
if __name__ == "__main__":
    if len(sys.argv)>=2:
          rutaAProcesar = sys.argv[1]      #ruta origen a procesar
          rutaDataProcesada = sys.argv[2]  #ruta destino
    else:
        raise Exception ("Debe pasar [Ruta a Procesar] [Ruta Destino],"+\
                          " Ej. ordenar_imgs.py '..Data\ordenar' '..\Data\imgs_procesadas' ")
    
    # rutaAProcesar = '../Data/ordenar/'
    # rutaDataProcesada = '../Data/imgs_procesadas/'
    
    #normalizar rutas
    rutaAProcesar = os.path.normpath(os.path.join(rutaAProcesar))
    rutaDataProcesada = os.path.normpath(os.path.join(rutaDataProcesada))
    
    print(f'ruta origen: {rutaAProcesar}')
    print(f'ruta destino: {rutaDataProcesada}')
    
    #obtener lista de archivos 
    listaArchivos = ObtenerListaArchivos_png(rutaAProcesar) 
    print(listaArchivos)
    
    #obtener lista de SubDirectorios
    listaDirectorios = ObtenerListaSubDirectorios(rutaAProcesar) 


    if os.path.exists(rutaDataProcesada):
        shutil.rmtree(rutaDataProcesada) #elimina carpeta aunque no este vacia
    
    os.mkdir(rutaDataProcesada)          #Recrear Carpeta
    
    for rutaFile in listaArchivos:
        rutaSplit = rutaFile.split(os.sep)   #dividir ruta normalizada   
        fileName = rutaSplit[-1:][0]       #obtener solo el nombre del archivo

        #os.sep es separador del sistema operativo
        rutaBase = os.sep.join(rutaSplit[:-1])   #mantener ruta Base para procesar despues
        newrutabase = (rutaBase + '.')[:-1]    #tip hacer una copia de contenido

        try:
            nuevoFile,fecha = procesar_nombre(fileName)
            
            newrutabase = newrutabase.replace(rutaAProcesar,rutaDataProcesada)
            rutaNuevoFile = os.path.join(newrutabase,nuevoFile)
            
            if not os.path.exists(newrutabase):     #Si no existe la ruta
                os.makedirs(newrutabase)            #Crear Subdirectorios forma recursiva
            
            os.rename(rutaFile, rutaNuevoFile )     # Mover archivo
            # shutil.copy(rutaFile, rutaNuevoFile ) # Copiar archivo
            ts_acceso = fecha.timestamp()
            ts_modifi = fecha.timestamp()
            os.utime(rutaNuevoFile, (ts_acceso, ts_modifi)) #Cambiar Fecha
        except Exception as e:
            print(f'{e}')

    #Evaluar directorios para Eliminar
    for rutaDir in listaDirectorios:
        try:
            os.removedirs(rutaDir)
        except Exception as e:
            pass  #continuar, puede ser que directorio no este vacio
