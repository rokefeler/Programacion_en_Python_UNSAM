# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 22:10:55 2021

@author: rokefeler@gmail.com
"""
#%%
class Punto():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def dist_origen(self):
        return np.sqrt(self.x**2 + self.y**2)

    def mover(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def rotar90(self):
        '''Permite rotar un punto geometrico 90 Grados '''
        return Punto(-1*self.y, self.x)
    
    def __str__(self):
        return f'({self.x},{self.y})'

    def __repr__(self):
        return f'Punto({self.x},{self.y})'
    
    def __add__(self, otro):
        return Punto(self.x + otro.x, self.y + otro.y)

class Rectangulo(Punto):
    def __init__(self, puntoIzq, puntoDer):
        self.puntoIzq = puntoIzq
        self.puntoDer = puntoDer
    
    def __str__(self):
        return f'(Izq:{self.puntoIzq}, Der:{self.puntoDer})'

    def __repr__(self):
        return f'Rectagulo( {self} )'
    
    def base(self):
        '''Calcula la base del Rectangulo '''
        return abs(self.puntoIzq.x - self.puntoDer.x)
    
    def altura(self):
        '''Calcula la altura del Rectangulo '''
        return abs(self.puntoIzq.y - self.puntoDer.y)
    
    def area(self):
        '''Calcula el area del rectangulo '''
        return self.base()*self.altura()
    
    def desplazar(puntoDesplazamiento):
        '''desplace el rectángulo en ambas coordenadas'''
        p1 = self.puntoDer + puntoDesplazamiento
        p2 = self.puntoIzq + puntoDesplazamiento
        self.puntoDer = p1
        self.puntoIzq = p2
    
    def rotar(self):
        '''rote el rectángulo sobre su esquina inferior derecha 90 grados a la derecha'''
        p1 = self.puntoDer.rotar90()
        p2 = self.puntoIzq.rotar90()
        self.puntoDer = p1
        self.puntoIzq = p2
        