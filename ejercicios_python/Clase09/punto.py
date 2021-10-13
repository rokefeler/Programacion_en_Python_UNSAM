# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 22:12:48 2021

@author: rokefeler@gmail.com
"""

#%%
################
##  herencia  ##
################
class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def dist_origen(self):
        return np.sqrt(self.x**2 + self.y**2)

    def mover(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return f'({self.x},{self.y})'

    def __repr__(self):
        return f'Punto({self.x},{self.y})'
    
    def __add__(self, otro):
        return Punto(self.x + otro.x, self.y + otro.y)
