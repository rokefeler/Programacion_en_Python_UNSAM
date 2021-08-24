#Leer archivo linea por linea
print("Leer archivo linea por linea")
with open('B002-00027086.txt', 'rt') as file:
    for line in file:
        print(line)

#Leer archivo todo en bloque
print("Leyendo archivo completamente"
     )
with open('B002-00027086.txt', 'rt') as file:
    data=file.read()
    print(data)

