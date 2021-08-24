numero_valido=False
while not numero_valido:
    try:
        a = input('Ingrese un numero entero:')
        n = int(a)
        numero_valido = True
        raise RuntimeError('¡Qué moco!')
    except ValueError:
        print('valor no válido, Intente de nuevo!')
print(f'Numero ingresado es {n}')    