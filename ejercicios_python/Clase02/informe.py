"""
juntá todo el trabajo que hiciste recién en tu programa informe.py 
(usando las funciones leer_camion() y leer_precios()) y completá el programa 
para que con los precios del camión (Ejercicio 2.16) y los de venta en el negocio
 (Ejercicio 2.17) calcule lo que costó el camión, 
 lo que se recaudó con la venta, y la diferencia
 ¿Hubo ganancia o pérdida? El programa debe imprimir por pantalla un balance con estos datos.
"""
import csv
def leer_camion(nombre_archivo):
    productos=[]
    with open(nombre_archivo) as f: 
        try:
            rows = csv.reader(f)
            headers=next(rows)
            for row in rows:
                try:
                    if(len(row)>2):
                        #value={'cantidad': int(row[1]), 'precio':float(row[2])}
                        productos.append( 
                            (
                                row[0].lower().strip(),  #Clave todo en mayusculas
                                int(row[1]), 
                                float(row[2])
                            ) 
                        )
                except Exception as e:
                    print(e)
        except ValueError:
            pass
    return productos
 

def leer_precios(nombre_archivo):
    precios={}
    with open(nombre_archivo) as f: 
        try:
            rows = csv.reader(f)
            #headers=next(rows)
            for row in rows:
                if(len(row)>1):
                    precios[row[0].lower().strip()]=float(row[1])
                #print(row[0])
        except ValueError:
            pass
    return precios
 

productos=leer_camion('Data/camion.csv') #Datos del camion, precios pagados al productor
#print(productos)
listaprecios=leer_precios('Data/precios.csv') #Lista de Precios de venta
#print(listaprecios)
totalCostoCamion=0.0
totalVentaCamion=0.0
for item in productos:
    producto,cantidad,precio = item
    #item=productos[i]
    #totalCostoCamion+=item['cantidad']*item['precio']
    totalCostoCamion+=cantidad*precio
    print(item)
    if(producto in listaprecios.keys()): #Si nombre de Producto esta en la lista de precios 
        totalVentaCamion+=cantidad*listaprecios[producto]
    else:
        totalVentaCamion+=cantidad*precio*1.15 #asumimos que lo vende CON UN 15% DE GANANCIA
    #debug print(i,productos[i])

print(f'Total Costo Camión: {round(totalCostoCamion,2):0.2f}')
print(f'Total Recaudación Venta Camión: {round(totalVentaCamion,2):0.2f}')
if(totalCostoCamion==totalVentaCamion):
    print(f'EL IMPORTE RECAUDADO DE LA VENTA ES IGUAL AL COSTO DEL CAMION, EXISTE PERDIDA DE FLETE U TRASLADOS')
elif(totalVentaCamion>totalCostoCamion):
    print(f'Existe una Diferencia(Ganancia) de: {round(totalVentaCamion-totalCostoCamion,2):0.2f}')
else:
    print(f'Existe una Diferencia(Perdida) de: {round(totalCostoCamion-totalVentaCamion,2):0.2f}')
