#Ejemplo Precoi Naranja
with open('../Data/precios.csv','rt') as f:
    headers=next(f).split(',')
    for line in f:
        row=line.split(',')
        if str(row[0])=='Naranja':
            print('El precio de la Naranja es ',float(row[1]))

