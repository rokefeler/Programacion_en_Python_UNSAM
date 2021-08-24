#esfera.py
"""
Developer: rokefeler@gmail.com
Enunciado: Que pida al usuario que ingrese por teclado el radio r
de una esfera y calcule e imprima el volumen de la misma.
Sugerencia: recordar que el volúmen de una esfera es 4/3 πr^3.
"""
#Ejercicio Volumen de una Esfera
import math
print("1.13 Calculo de Volumen de una Esfera")
respuesta=True
while respuesta:
    r=float(input("Ingrese valor del radio de la esfera:"))
    print(f':. Volumen de Esfera es: {(4/3)*math.pi*(r**3):14.4f}')
    resp=input("\n\n¿Desea Continuar con otra Operación: (Si,NO, Yes, Not):?")
    resp=resp.lower()
    resp=resp[0]
    if not(resp=='s' or resp=='y'):
        respuesta=False
