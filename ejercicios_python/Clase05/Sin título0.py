# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 22:46:13 2021

@author: FamiliaRoqueSosa
"""

import random
random.seed(31415)

tirada=[]

for i in range(5):
    tirada.append(random.randint(1,6)) 

caras = ['uno', 'dos', 'tres', 'cuatro', 'cinco', 'seis']
print(random.choice(caras))
print(random.choices(caras,k=5))
print(tirada)