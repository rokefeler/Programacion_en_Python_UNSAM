#geringoso.py
'''
Developer: rokefeler@gmail.com
Enunciado: Construí una función que, a partir de una lista de palabras, devuelva un diccionario geringoso. 
Las claves del diccionario deben ser las palabras de la lista y los valores deben ser sus traducciones al geringoso.
'''
def dicgeringoso(palabras):
    resultado = []
    for p in palabras:
        t = (p,geringoso(p))
        resultado.append(t)
    return dict(resultado)

def geringoso(cadena):
    capadepenapa = ''
    for c in cadena:
        capadepenapa=capadepenapa + c
        if c in ('a','e','i','o','u','Á','É','Í','Ó','Ú'):
            capadepenapa=capadepenapa + 'p' + c
    return capadepenapa
    #print('capadepenapa:',capadepenapa)
    
listapalabras = ['banana','manzana','mandarina']
print(dicgeringoso(listapalabras))