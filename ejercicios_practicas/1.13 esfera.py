"""
    Que pida al usuario que ingrese por teclado el radio r
    de una esfera y calcule e imprima el volumen de la misma.
    Sugerencia: recordar que el volúmen de una esfera es 4/3 πr^3.
"""
import math
print("1.13 Calculo de Volumen de una Esfera")
r=float(input("Ingrese valor del radio:"))
print(":. Volumen es:", (4/3)*math.pi*(r**3))
