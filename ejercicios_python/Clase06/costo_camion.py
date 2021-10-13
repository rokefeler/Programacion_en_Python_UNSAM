#costo_camion.py
"""
Developer: rokefeler@gmail.com
Ejercicio 3.8 ejemplo practico de enumerate
"""
import os
from informe_funciones import leer_camion
def costo_camion(nombre_archivo):
    camion=leer_camion(nombre_archivo)
    costototal = sum([s['cajones'] * s['precio'] for s in camion])
    return costototal


#%%
if __name__ == "__main__":
    files = ['../Data/camion.csv', '../Data/camion2.csv']
    for name in files:
        print(f'{name:-^43s}')
        cfile_archivo_camion = os.path.join(name)
        costo=costo_camion(name)
        print(f'Costo Total de archivo {name} es: {round(costo,2):0.2f}')
