#geringoso.py
'''
Developer: rokefeler@gmail.com
Enunciado: Usá una iteración sobre el string cadena para
agregar la sílaba 'pa', 'pe', 'pi', 'po', o 'pu'
según corresponda luego de cada vocal.
'''
#cadena = 'Geringoso'
cadena="Geringoso cálculo Ángulo capa método pingüino quirquincho que cuenca ciencia"
capadepenapa = ''
for c in cadena:
    capadepenapa=capadepenapa + c
    if c in ('a','e','i','o','u','Á','É','Í','Ó','Ú'):
        capadepenapa=capadepenapa + 'p' + c

print('capadepenapa:',capadepenapa)