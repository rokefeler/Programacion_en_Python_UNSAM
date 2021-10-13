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
# Funcion principal
def main(parametros):
    if len(parametros) <= 1:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'archivo_camion1 archivo_camion2 ...')
    files = []
    n=1
    while n<len(parametros):  #Agregar archivos pasados
        files.append(parametros[n])
        n+=1
    
    for name in files:  #Realizar Impresión del Costo del Archivo
        cfile_archivo_camion = os.path.join(name)
        costo=costo_camion(name)
        print(f'Costo Total de archivo {name} es: {round(costo,2):0.2f}')
        print(f"{str('-'):-^53s}")

#%%
if __name__ == "__main__":
    import sys
    main(sys.argv)
    