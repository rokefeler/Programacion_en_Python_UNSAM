# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 23:04:03 2021

@author: rokefeler@gmail.com
"""

# Escribí una función llamada vida_en_segundos(fecha_nac) a la que le pasás 
# tu fecha de nacimiento y te devuelve la cantidad de segundos que viviste 
# (asumiendo que naciste a las 00:00hs de tu fecha de nacimiento). 
# La función debe tomar como entrada una cadena en formato 'dd/mm/AAAA' 
# (día, mes, año con 2, 2 y 4 dígitos, separados con barras normales) 
# y devolver un float.
from datetime import datetime


def vida_en_segundos(fecha_nac):
    '''recibe una cadena en formato 'dd/mm/AAAA' 
    y devuelve la cantidad de segundos desde esa fecha a la actual 
    '''
    now = datetime.now()  #Fecha actual
    
    #convertir cadena a fecha
    fechaNacimiento = datetime.strptime(fecha_nac, '%d/%m/%Y')
    
    dif = now - fechaNacimiento #calculo de diferencia de fechas
    return dif.total_seconds() #devuelve total segundos

#%%
if __name__ == "__main__":
    seconds = vida_en_segundos('25/10/1985')
    print(f'Vida en Segundos: {seconds:.6f}')
    
    print(f'dias vividos: {seconds/(3600*24):.4f}')
    print(f'años vividos: {seconds/(3600*24*365):.4f}')
