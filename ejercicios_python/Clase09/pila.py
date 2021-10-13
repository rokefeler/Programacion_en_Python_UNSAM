# -*- coding: utf-8 -*-
"""
Created on Wed Oct 13 00:02:50 2021

@author: rokefeler@gmail.com
"""

def f():
    x = 50
    a = 20
    print("En f, x vale", x)

def g():
    x = 10
    b = 45
    print("En g, antes de llamar a f, x vale", x)
    f()
    print("En g, después de llamar a f, x vale", x)
class Pila:
    def __init__(self, estado={}):
        self.estado = {}
        self.estado.update(estado)
    def falta:
        pass