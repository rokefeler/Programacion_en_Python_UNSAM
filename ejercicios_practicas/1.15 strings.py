'''
  Extraer caracteres individuales y subcadenas
  frutas = 'Manzana,Naranja,Mandarina,Banana,Kiwi'
  frutas[0]='M'
  frutas[1]='a'
  frutas[2]='n'
  frutas[-1]='i'
  frutas[-2]='w'
'''
frutas = 'Manzana,Naranja,Mandarina,Banana,Kiwi'
frutas = frutas + 'Pera' #'Manzana,Naranja,Mandarina,Banana,KiwiPera'
#correccion
frutas = frutas[:-4] + ',Pera' #'Manzana,Naranja,Mandarina,Banana,Kiwi,Pera'
print(frutas)
#Agregá 'Melón'` al principio de la cadena:
frutas = 'Melon,'+frutas
print(frutas)