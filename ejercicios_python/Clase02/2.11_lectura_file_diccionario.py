#lectura csv con Diccionarios
def costocamion(nombre_archivo):
    costototal=0.0 #inicializamos un acumulador
    with open(nombre_archivo,'rt') as f:
        headers=next(f).split(',')
        print(headers)
        precios = {}
        for line in f:
            try:
                row=line.split(',')
                precios[row[0]] = float(row[2])
                t={'nombre':row[0], 'cajones':int(row[1]), 'precio':float(row[2])} #creación de Diccionario     nombre,cajones,precio=t  #disgregacion de contenido de una tupla a variables
                #print(row)
                print(f'{ t["cajones"] } cajas de { t["nombre"] } a { t["precio"]:0.2f} ')
                #costo=t[1]*t[2]
                costo = t['cajones']*t['precio']
                costototal+=costo
            except ValueError:
                pass #print('Linea sin datos o datos inválidos')
    #print('Costo costototal es:',round(costototal,2))
    return costototal

#costo = costocamion('Data/camion.csv')
#print('Costo Total Camión es:',round(costo,2))

costo = costocamion('Data/missing.csv')
print('Costo Total Camión es:',round(costo,2))
