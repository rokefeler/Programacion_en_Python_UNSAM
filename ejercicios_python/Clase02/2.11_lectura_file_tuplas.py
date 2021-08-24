#lectura csv con tuplas
def costocamion(nombre_archivo):
    costototal=0.0 #inicializamos un acumulador
    with open(nombre_archivo,'rt') as f:
        headers=next(f).split(',')
        print(headers)
        for line in f:
            try:
                row=line.split(',')
                t=(row[0],int(row[1]),float(row[2])) #creación de Tupla, a dif. de Listas y Diccion. son inmutables
                nombre,cajones,precio=t  #disgregacion de contenido de una tupla a variables
                #print(row)
                print(f'{cajones} cajas de {nombre} a {precio:0.2f}')
                #costo=t[1]*t[2]
                costo=cajones*precio
                costototal+=costo
            except ValueError:
                print('Linea sin datos o datos inválidos')
    #print('Costo costototal es:',round(costototal,2))
    return costototal

#costo = costocamion('Data/camion.csv')
#print('Costo Total Camión es:',round(costo,2))

costo = costocamion('Data/missing.csv')
print('Costo Total Camión es:',round(costo,2))
