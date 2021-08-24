"""
Escribí una función leer_precios(nombre_archivo) que a partir de un conjunto de precios 
como éste arme un diccionario donde las claves sean los nombres de frutas y verduras,
y los valores sean los precios por cajón
"""
import csv

def leer_precios(nombre_archivo):
    precios={}
    with open(nombre_archivo) as f: 
        try:
            rows = csv.reader(f)
            #headers=next(rows) no hay headers
            for row in rows:
                if(len(row)>1):
                    precios[row[0].lower().strip()]=float(row[1])
                #print(row[0])
        except ValueError:
            pass
    return precios

try:
    precios = leer_precios('Data/precios.csv')

    while 1:
        print('BUSCADOR DE PRECIOS')
        fruta=input('Ingrese nombre de la fruta a buscar o ENTER para terminar:')
        fruta=fruta.lower().strip() #a minusculas y sin espacios al inicio y final
        if(fruta==''):
            break
        if(fruta in precios):
            print(f'precio de {fruta.upper()} es: {round(precios[fruta],2):0.2f}')
        else:
            print('Fruta no Encontrada, por favor intente con otro nombre')
except Exception as e:
    print(e)
    print('ERROR inesperado... good bye!')


