# rebotes.py
# Archivo de ejemplo
# Ejercicio
"""
Developer: rokefeler@gmail.com
Enunciado: Una pelota de goma es arrojada desde una altura de 100 metros y cada vez que toca el piso
salta 3/5 de la altura desde la que cayó.
Escribí un programa rebotes.py que imprima una tabla mostrando las alturas que alcanza
en cada uno de sus primeros diez rebotes.
"""
altura = 100
nrebotes=0
while nrebotes<10:
    altura=altura*(3/5)
    nrebotes+=1
    #print('Rebote #',nrebotes,' Altura Alcanzada:',round(altura,4))
    print(f'Rebote # {nrebotes}, Altura alcanzada: {round(altura,4):0.4f}')
