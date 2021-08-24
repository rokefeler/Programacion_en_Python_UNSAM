#costo_camion.py
"""
Developer: rokefeler@gmail.com
Objetivo: Escribí un programa llamado costo_camion.py que 
abra el archivo, lea las líneas, y calcule el precio pagado 
por los cajones cargados en el camión.
"""
import csv
import sys

def costo_camion(nombre_archivo='Data/camion.csv'):
    costototal=0.0 #inicializamos un acumulador
    try:
        with open(nombre_archivo,'rt') as f:
            #headers=next(f).split(',')
            rows=csv.reader(f)
            headers = next(rows)
            print(headers)
            for row in rows:
                #row=line.split(',')
                try:
                    #print(row)
                    costo=int(row[1])*float(row[2])
                    print(f'{row[1]} {row[0]} a {row[2]} cuesta: {round(costo,2):0.2f}')
                except ValueError:
                    costo=0.0
                costototal+=costo
    except FileNotFoundError:
        print(f'{nombre_archivo} No existe, intente ingresar nombre de archivo correcto')
    except Exception as e:
        print(e)
    return costototal
    #print('Costo costototal es:',round(costototal,2))

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = 'Data/camion.csv'

print('nombre achivo',nombre_archivo)
costo = costo_camion(nombre_archivo)
print(f'Costo Total del Camión es: {round(costo,2):0.2f}')





