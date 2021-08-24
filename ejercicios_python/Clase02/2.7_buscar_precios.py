"""
A partir de lo que hiciste en el Ejercicio 2.3, escribí una función 
buscar_precio(fruta) que busque en archivo ../Data/precios.csv 
el precio de determinada fruta (o verdura) y lo imprima en pantalla. 
Si la fruta no figura en el listado de precios, 
debe imprimir un mensaje que lo indique.
"""
def buscar_precio(nombre_fruta):
    with open('Data/precios.csv','rt') as f:
        headers=next(f).split(',')
        for line in f:
            row=line.split(',')
            if str(row[0].lower().strip())==nombre_fruta.lower().strip():
                print(f'El precio de {row[0]} es ',float(row[1]))
                return True
    print(f'{nombre_fruta} no existe, aun no tenemos su lista de precios')
    return False

try:
    while 1:
        print('BUSCADOR DE PRECIOS')
        nombre_fruta=input('Ingrese nombre de la fruta a buscar o ENTER para terminar:')
        if(nombre_fruta==''):
            break
        buscar_precio(nombre_fruta)
except Exception as e:
    print(e)
    print('ERROR inesperado... good bye!')

#buscar_precio('Frambuesa')
#buscar_precio('Kale')
