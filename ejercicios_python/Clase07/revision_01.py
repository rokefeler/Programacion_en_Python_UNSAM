# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 10:36:48 2021

@author: Sistemas
"""

#import csv
#from fileparse import parse_csv
from informe_funciones import leer_camion

def costo_camion(nombre_archivo):
    costo_total = 0
    info_camion = leer_camion(nombre_archivo)
    for linea, _ in enumerate(info_camion):                 
        total = int(info_camion[linea]['cajones']) * float(info_camion[linea]['precio'])
        costo_total += total   
    return costo_total

if __name__ == '__main__':
    Camion = costo_camion('../Data/camion.csv')
    print(f'\nEl costo del camión de frutas es de: ${Camion}')
    print('\n\n')
    print(f'▄'*25)
    print(f'█\tFrutas\t\t█   █▀▀▄╗(¤')
    print('█'*25,'--█▄▄▀╝(¤')
    print(f'{("(@)"):>3s}{("(@)"):>7s}{("(@)"):>12s}{("(@)"):>9s}')
    print('▒'*40)
    print('\n')


# %%