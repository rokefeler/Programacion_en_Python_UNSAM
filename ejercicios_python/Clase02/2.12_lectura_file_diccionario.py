#lectura csv con tuplas
def costocamion(nombre_archivo):
    costototal=0.0 #inicializamos un acumulador
    with open(nombre_archivo,'rt') as f:
        headers=next(f).split(',')
        print(headers)
        for line in f:
            try:
                row=line.split(',')
                d = {
                    'nombre': row[0],
                    'cajones': int(row[1]),
                    'precio': float(row[2]),
                }
                #print(row)
                print(f"{d['cajones']} cajas de {d['nombre']} a {d['precio']:0.2f}")
                #costo=t[1]*t[2]
                costo=d['cajones']*d['precio']
                costototal+=costo
            except ValueError:
                pass
    #print('Costo costototal es:',round(costototal,2))
    return costototal

#costo = costocamion('Data/camion.csv')
#print('Costo Total Camión es:',round(costo,2))

costo = costocamion('Data/missing.csv')
print('Costo Total Camión es:',round(costo,2))
