'''
Usá una iteración sobre el string cadena para 
agregar la sílaba 'pa', 'pe', 'pi', 'po', o 'pu' 
según corresponda luego de cada vocal.
'''
cadena = 'Geringoso'
capadepenapa = ''
for c in cadena:
    capadepenapa=capadepenapa + c
    if c in ('a','e','i','o','u'):
        capadepenapa=capadepenapa + 'p' + c

print('capadepenapa:',capadepenapa)