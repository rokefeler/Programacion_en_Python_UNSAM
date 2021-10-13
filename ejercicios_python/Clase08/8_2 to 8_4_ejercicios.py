# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 23:26:21 2021

@author: rokefeler@gmail.com
"""
#%% Ejercicio 8.2: Cuánto falta
#Un conocido canal Argentino tiene por costumbre anunciar la cantidad de días 
#que faltan para la próxima primavera.
from datetime import datetime,date,timedelta

def dias_to_primavera():
    '''devuelve la cantidad de dias que faltan para llegar a la Primavera 
    que se festeja el 22 de Setiembre en Argentina
    '''
    now = datetime.now()  #Fecha actual
    
    cFechaPrimavera = datetime(now.year,9,22)  #Fecha Primavera actual
    
    #Si ya pasamos la Primavera de este año, reajustar
    if (now.month==9 and now.day>22) \
        or now.month>9: 
        cFechaPrimavera = datetime(now.year+1,9,22)  
        
    dif = cFechaPrimavera - now #cuanto falta
    return dif.days   #devuelve total de dias faltantes
#%%
#Ejercicio 8.3: Fecha de reincorporación
'''
Si tenés una licencia por xaternidad que empieza el 26 de septiembre de 2020 
y dura 200 días, ¿qué día te reincorporás al trabajo?
'''
def fecha_reincorporacion(cFecha_start, dias):
    #convertir cadena a fecha
    dFecha = datetime.strptime(cFecha_start, '%d/%m/%Y')
    
    timedeltaFinal = timedelta(days=dias)
    dFechaFinal = dFecha + timedeltaFinal
    
    return dFechaFinal.date()
#%% "Ejercicio 8.4: Días hábiles"
def dias_habiles(inicio, fin, feriados=[]):
    '''calcule los días hábiles entre dos fechas dadas
    inicio y fin son fechas en formato texto dd/mm/yyyy
    feriados es una Lista de fechas de feriados
    
    Consideramos día hábil a un día que no es feriado ni sábado ni domingo.
    
    devuelve una lista con las fechas de días hábiles del período, 
    incluyendo la fecha inicial y la fecha final indicadas
    
    '''
    try:
        dFechaInicio = datetime.strptime(inicio, '%d/%m/%Y')
    except ValueError:
        raise Exception(f"{inicio} es una Fecha invalida... corriga al formato dd/mm/yyyy")
    #print(f'Fecha Inicio: {dFechaInicio}')
    
    try:
        dFechaFin = datetime.strptime(fin, '%d/%m/%Y')
    except ValueError:
        raise Exception(f"{fin} es una Fecha invalida... corriga al formato dd/mm/yyyy")
    #print(f'Fecha Fin: {dFechaFin}')
    
    dias =  dFechaFin - dFechaInicio
    #print(f'dias : {dias.days}')
    ListaFechas = []
    for x in range(0,dias.days+1):
        fecha = dFechaInicio + timedelta(days=x) 
        
        cfecha = fecha.strftime('%d/%m/%Y')  #fecha en formato cadena dd/mm/yyyy
        if fecha.weekday()<4 \
            and cfecha not in feriados:      #fecha no esta en lista de feriados
            ListaFechas.append(cfecha)       #agregar fecha
    return ListaFechas
    
#%%
if __name__ == "__main__":
    print("========================")
    dias = dias_to_primavera()
    print(f"Faltan {dias} dias para la Primavera")
    
    print("========================")    
    dias_licencia = 200
    cFechaInicioLicencia = '26/09/2020'
    fecha = fecha_reincorporacion(cFechaInicioLicencia, dias_licencia)
    print(f"Fecha Reincorporación por Maternidad es: {fecha.strftime('%d/%m/%Y')}")
    
    print("========================")
    feriados = []
    diash1 = dias_habiles('20/09/2020', '10/10/2020', feriados)
    print(f"Dias Habiles entre 20/09/2020 y 10/10/2020 sin feriados")
    print(diash1)
    
    print("========================")
    feriados = ['12/10/2020', '23/11/2020', '7/12/2020', '8/12/2020', '25/12/2020']
    print(f"Dias Habiles entre 20/09/2020 y 10/10/2020 con feriados {feriados} -----")
    diash2 = dias_habiles('20/09/2020', '10/10/2020', feriados)
    print(diash2)
