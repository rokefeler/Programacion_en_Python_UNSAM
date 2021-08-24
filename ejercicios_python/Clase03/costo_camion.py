#costo_camion.py
"""
Developer: rokefeler@gmail.com
Ejercicio 3.8 ejemplo practico de enumerate
"""
import csv
def costo_camion(nombre_archivo):
    costototal=0.0 #inicializamos un acumulador
    try:
        with open(nombre_archivo,'rt') as f:
            rows=csv.reader(f)
            headers = next(rows)
            for n_fila,fila in enumerate(rows,start=1):
                try:
                    #print(row)
                    record=dict(zip(headers,fila))
                    ncajones = int(record['cajones'])
                    precio = float(record['precio'])
                    costototal+=ncajones*precio
                except Exception as e:
                    print(f'\tError: Fila{n_fila} no puede interpretar {str(fila)}')
    except FileNotFoundError:
        print(f'ERROR: {nombre_archivo} No existe, intente ingresar nombre de archivo correcto')
    except Exception as e:
        print(e)
    return costototal
    #print('Costo costototal es:',round(costototal,2))
#costo = costo_camion('../Data/camion.csv')
#print(f'Costo Total es: {round(costo,2):0.2f}')


#%%
#Ejercicio 3.9. uzo de funcion zip y dict
#Comentario: Se leera archivo fecha_camion.csv
# ... definición de funcion no termina con :
# ... linea while le faltaba los ":"
# ... linea if tenia una asignación en lugar de una comparación, debe ser "=="
# ... Ult. linea decia return Falso, debio de decir return False.

costo = costo_camion('../Data/camion.csv')
print(f'Costo Total de camion.csv es: {round(costo,2):0.2f}')

costo = costo_camion('../Data/fecha_camion.csv')
print(f'Costo Total de fecha_camion.csv es: {round(costo,2):0.2f}')