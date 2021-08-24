#costo_camion.py
"""
Developer: rokefeler@gmail.com
Objetivo: Escribí un programa llamado costo_camion.py que 
abra el archivo, lea las líneas, y calcule el precio pagado 
por los cajones cargados en el camión.
"""
import csv
def costo_camion(nombre_archivo='Data/camion.csv'):
    costototal=0.0 #inicializamos un acumulador
    try:
        with open(nombre_archivo,'rt') as f:
            rows=csv.reader(f)
            headers = next(rows)
            print(headers)
            for row in rows:
                print(row)
                if(len(row)>1):
                    costo=int(row[1])*float(row[2])
                    costototal+=costo
    except FileNotFoundError:
        print(f'{nombre_archivo} No existe, intente ingresar nombre de archivo correcto')
    except Exception as e:
        print(e)
    return costototal
    #print('Costo costototal es:',round(costototal,2))
costo = costo_camion('Data/camion.csv')
print(f'Costo Total es: {round(costo,2):0.2f}')


