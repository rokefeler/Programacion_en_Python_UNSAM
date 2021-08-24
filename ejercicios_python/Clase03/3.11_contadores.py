from collections import Counter
from pprint import pprint
import csv
def leer_camion(nombre_archivo):
    productos=[]
    with open(nombre_archivo) as f: 
        try:
            rows = csv.reader(f)
            headers=next(rows)
            for row in rows:
                value={}
                try:
                    if(len(row)>2):
                        value={'nombre': row[0].lower().strip(),
                               'cajones': int(row[1]),
                               'precio':float(row[2])
                               }
                    productos.append(value)
                except Exception as e:
                    pass #print(e)
        except ValueError:
            pass
    return productos

camion = leer_camion('../Data/camion.csv')
tenencias = Counter()
for s in camion:
    tenencias[s['nombre']] += s['cajones']
print('Contador 1')
pprint(tenencias)
#Counter({'Caqui': 150, 'Durazno': 95, 'Lima': 100, 'Mandarina': 250, 'Naranja': 150})
print('# Las 3 frutas con más cajones')
pprint(tenencias.most_common(3))

camion2 = leer_camion('../Data/camion2.csv')
tenencias2 = Counter()
for s in camion2:
    tenencias2[s['nombre']] += s['cajones']
print('Contador 2')
pprint(tenencias2)
#Counter({'Durazno': 125, 'Frambuesa': 250, 'Lima': 50, 'Mandarina': 25})

print('Combinación de Contador 1 y 2')
combinada = tenencias + tenencias2
pprint(combinada)