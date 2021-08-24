#2.1 Lectura de un archivo
f=open('Data/camion.csv','rt')
headers=next(f).split(',')
print(headers)
for line in f:
    row=line.split(',')
    print(row)
f.close() #esto porque no estamos trabajando con with


