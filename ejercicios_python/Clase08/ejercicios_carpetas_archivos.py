# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 22:10:16 2021

@author: rokefeler@gmail.com
"""

#8.3 Manejo de archivos y carpetas
#%% Obtener el directorio actual
import os
os.getcwd()
#'R:\\home\\jroque\\Python_UNSAM\\ejercicios_python\\Clase08'

#%%
#Cambiar el directorio de trabajo
os.chdir('../Data')              # entro en ../Data
print(os.getcwd())
#R:\home\jroque\Python_UNSAM\ejercicios_python\Data
os.chdir('..')                  # subo un nivel
os.chdir('..')                  # subo otro nivel
print(os.getcwd())
#R:\home\jroque\Python_UNSAM
os.chdir('/home')
print(os.getcwd())
#R:\home
#%%
#Listar directorios y archivos
print(os.getcwd())
listado=os.listdir('../Data')
print(listado)

#%%
#Crear un nuevo directorio
os.mkdir('test')          # creo el directorio test
os.mkdir(os.path.join('test', 'carpeta'))  # creo el subdirectorio carpeta dentro de test
os.listdir('test')
#['carpeta']
#%% Renombrar un directorio o un archivo

os.chdir('test') 
os.listdir()
#['carpeta']

os.rename('carpeta','carpeta_nueva') # cambio el nombre de carpeta
os.listdir()
# ['carpeta_nueva']

os.chdir('..') # subo un nivel
os.listdir('test')   # miro qué hay en test
os.rename(os.path.join('test', 'carpeta_nueva'), os.path.join('test','carpeta_vieja'))
os.listdir('test')
#['carpeta_vieja']

os.rename(os.path.join('test','carpeta_vieja'), 'carpeta_vieja') # cambio el path
os.listdir('test')   
#{}   #La carpeta 'carpeta' ahora se encuentra en 'Ejercicios', y no dentro de 'Ejercicios/test'.

#%% 
os.chdir('otra_carpeta')    # entro otra carpeta que tiene
                                # una subcarpeta y un archivo de texto
os.listdir()
#['subcarpeta', 'archivo.txt']

os.remove('archivo.txt')    # elimino el archivo
os.listdir()
#['subcarpeta']

os.rmdir('subcarpeta')      # elimino la subcarpeta
os.listdir()
#[]
#Ojo: rmdir() solamente puede borrar directorios 
#si están vacíos. 
#Para eliminar un directorio no vacío, 
#podés usar rmtree() del módulo shutil

os.mkdir(os.path.join('test','carpeta'))                # creo nuevamente una carpeta
os.mkdir(os.path.join('test','carpeta', 'subcarpeta'))  # creo una subcarpeta en carpeta
os.chdir('test')                                        # entro en test
os.rmdir('carpeta')
# Traceback (most recent call last):
#   File "<ipython-input-277-c4255042d84c>", line 1, in <module>
#     os.rmdir('carpeta')
# OSError: [Errno 39] Directory not empty: 'carpeta'

import shutil
shutil.rmtree('carpeta') #elimina carpeta aunque no este vacia
os.listdir()
#[]


#%% Recorriendo directorios con os.walk()
import os
for root, dirs, files in os.walk("."):
   for name in files:
      print(os.path.join(root, name))
   for name in dirs:
      print(os.path.join(root, name))
# .\01_ejercicios_datetime.py
# .\vida.py
# .\readme.txt
# .\8_2 to 8_4_ejercicios.py
# .\carpeta_vieja
# .\otra_carpeta
# .\test
# .\otra_carpeta\readme.txt
# .\otra_carpeta\carpeta_2021

#%%
import os
import datetime
import time

camino = '../Clase06/rebotes.py'

stats_archivo = os.stat(camino)
print(time.ctime(stats_archivo.st_atime))

fecha_acceso = datetime.datetime(year = 2017, month = 9, day = 21, hour = 19, minute =51, second = 0)
fecha_modifi = datetime.datetime(year = 2012, month = 9, day = 24, hour = 12, minute =9, second = 24)

ts_acceso = fecha_acceso.timestamp()
ts_modifi = fecha_modifi.timestamp()
os.utime(camino, (ts_acceso, ts_modifi))

stats_archivo = os.stat(camino)
print(time.ctime(stats_archivo.st_atime))