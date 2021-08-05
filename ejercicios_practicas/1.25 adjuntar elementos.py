lista_frutas = ['Frambuesa', 'Manzana', 'Granada', 'Mandarina', 'Banana', 'Pera','Limon']
for s in lista_frutas:
    print('s =', s)

print('Granada' in lista_frutas)
print('Lima' in lista_frutas)
print('Limon' in lista_frutas)
lista_frutas.append('Mango')
print(lista_frutas)
lista_frutas.insert(1,'Lima')
print(lista_frutas)
lista_frutas.remove('Mandarina')
print(lista_frutas)
print(lista_frutas.index('Banana'))
print(lista_frutas.count('Banana'))
print(lista_frutas)
#Ejercicio 1.26: Sorting
lista_frutas.sort()
print(lista_frutas)
lista_frutas.sort(reverse=True)
print(lista_frutas)
