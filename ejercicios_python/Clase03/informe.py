"""
juntá todo el trabajo que hiciste recién en tu programa informe.py 
(usando las funciones leer_camion() y leer_precios()) y completá el programa 
para que con los precios del camión (Ejercicio 2.16) y los de venta en el negocio
 (Ejercicio 2.17) calcule lo que costó el camión, 
 lo que se recaudó con la venta, y la diferencia
 ¿Hubo ganancia o pérdida? El programa debe imprimir por pantalla un balance con estos datos.
"""
import csv
from pprint import pprint
def leer_camion(nombre_archivo):
    productos=[]
    try:
        with open(nombre_archivo) as f: 
            try:
                rows = csv.reader(f)
                headers=next(rows)
                for row in rows:
                    try:
                        record=dict(zip(headers,row))
                        record['nombre']  = record['nombre'].lower().strip()
                        record['cajones'] = int(record['cajones'])
                        record['precio']  = float(record['precio'])
                        productos.append(record)
                    except Exception as e:
                        pass
            except ValueError:
                pass
    except FileNotFoundError:
        print(f'ERROR: {nombre_archivo} No existe, intente ingresar nombre de archivo correcto')
    except Exception as e:
        print(e)
    return productos
 

def leer_precios(nombre_archivo):
    precios={}
    try:
        with open(nombre_archivo) as f: 
            rows = csv.reader(f)
            header=['nombre','precio']
            for row in rows:
                try:
                    record=dict(zip(header,row))
                    record['nombre']  = record['nombre'].lower().strip()
                    record['precio']  = float(record['precio'])
                    precios[record['nombre']] = record['precio']
                except Exception as e:
                    pass 
    except FileNotFoundError:
        print(f'ERROR: {nombre_archivo} No existe, intente ingresar nombre de archivo correcto')
    except Exception as e:
        print(e)
    return precios
 

productos=leer_camion('../Data/camion.csv') #Datos del camion, precios pagados al productor
listaprecios=leer_precios('../Data/precios.csv') #Lista de Precios de venta

totalCostoCamion=0.0
totalVentaCamion=0.0
for item in productos:
    producto,cajones,precio=item.values()
    totalCostoCamion+=cajones*precio
    if(producto in listaprecios.keys()): #Si nombre de Producto esta en la lista de precios 
         totalVentaCamion+=cajones*listaprecios[producto]
    else:
         totalVentaCamion+=cajones*precio*1.15 #asumimos que lo vende CON UN 15% DE GANANCIA

print(f'Total Costo Camión: {round(totalCostoCamion,2):0.2f}')
print(f'Total Recaudación Venta Camión: {round(totalVentaCamion,2):0.2f}')
if(totalCostoCamion==totalVentaCamion):
    print(f'EL IMPORTE RECAUDADO DE LA VENTA ES IGUAL AL COSTO DEL CAMION, EXISTE PERDIDA DE FLETE U TRASLADOS')
elif(totalVentaCamion>totalCostoCamion):
    print(f'Existe una Diferencia(Ganancia) de: {round(totalVentaCamion-totalCostoCamion,2):0.2f}')
else:
    print(f'Existe una Diferencia(Perdida) de: {round(totalCostoCamion-totalVentaCamion,2):0.2f}')
    