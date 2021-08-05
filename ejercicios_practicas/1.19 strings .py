'''
>>> frutas.find('Mandarina') #16
>>> frutas[13:17] #'ja,M'
>>> frutas.replace('Kiwi','Melón') #'Manzana,Naranja,Mandarina,Banana,Melón,Pera'
>>> nombre='   Naranja   \n  '
>>> nombre=nombre.strip()
>>> nombre                         #'Naranja'
'''
frutas = 'Melón,Manzana,Naranja,Mandarina,Banana,Kiwi,Pera'
frutas.lower()
lowersyms = frutas.lower()
frutas.find('Mandarina')
frutas[13:17]
frutas = frutas.replace('Kiwi','Melón')
frutas
nombre = '   Naranja   \n'
nombre = nombre.strip()    # Remove surrounding whitespace
nombre

