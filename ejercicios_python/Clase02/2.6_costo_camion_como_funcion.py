
def costocamion(nombre_archivo):
    costototal=0.0 #inicializamos un acumulador
    with open(nombre_archivo,'rt') as f:
        headers=next(f).split(',')
        print(headers)
        for line in f:
            try:
                row=line.split(',')
                print(row)
                if(len(row)>1):
                    costo=int(row[1])*float(row[2])
                    costototal+=costo
            except ValueError:
                pass
                #print('Linea sin datos o datos inválidos')
    #print('Costo costototal es:',round(costototal,2))
    return costototal

#costo = costocamion('Data/camion.csv')
#print('Costo Total Camión es:',round(costo,2))

costo = costocamion('Data/missing.csv')
print(f'Costo Total Camión es: {round(costo,2):0.2f}')
