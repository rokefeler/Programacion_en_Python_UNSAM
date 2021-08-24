#funciones.py
def sumcount(n):
    '''
    Devuelve la suma de los primeros n enteros
    '''
    total = 0 #acumulador
    while n > 0:
        total += n
        n -= 1
    return total
n=int(input('Suma de los primeros n enteros, ingrese valor de n:'))   
print(f'Suma de los {n} primeros enteros: {sumcount(n)}')