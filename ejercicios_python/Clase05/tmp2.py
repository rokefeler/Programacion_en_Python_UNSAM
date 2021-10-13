# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 22:51:59 2021

@author: FamiliaRoqueSosa
"""

# -*- coding: utf-8 -*-
import random
###   El juego "Generala" consiste en tirar cinco dados y establecer el puntaje de la
###   jugada. De las posibles, la escalera se da cuando suceden algunas de las tres progresiones: 1-2-3-4-
###   5, 2-3-4-5-6 y 3-4-5-6-1. Realice un programa que tire los 5 dados al azar y determine si se produjo
###   una escalera. 
 
 
 
Iteraciones = 0
Ganaste = 0
while Ganaste != 1000:
    Lista_dados=[]
    dado_1= random.randrange(1,7)
    Lista_dados.append(dado_1)
   
    dado_2= random.randrange(1,7)
    Lista_dados.append(dado_2)
   
    dado_3= random.randrange(1,7)
    Lista_dados.append(dado_3)
   
    dado_4= random.randrange(1,7)
    Lista_dados.append(dado_4)
   
    dado_5= random.randrange(1,7)
    Lista_dados.append(dado_5)
     
    Lista_dados.sort()
     
     
    if ( Lista_dados == [1, 2, 3, 4, 5] ) or ( Lista_dados == [ 2, 3, 4, 5,6] ) or ( Lista_dados == [1, 3, 4, 5, 6] ):
          Iteraciones +=1
          print(f'Ganaste en: {Iteraciones} Lanzadas')
          print (Lista_dados)
 
          Ganaste += 1000
           
           
    else:
          Iteraciones +=1
          print (f"Sigue intentando solo son: {Iteraciones} Lanzadas")