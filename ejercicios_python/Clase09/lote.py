# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 19:16:01 2021

@author: rokefeler@gmail.com
"""

class Lote:
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio
    
    def __repr__(self):
        return f"Lote('{self.nombre}',{self.cajones}, {self.precio:.2f} )"
    
    def costo(self):
        return self.cajones * self.precio
    
    def vender(self, cantidad):
        if self.cajones<cantidad:
            raise Exception("No Existe Cantidad minima para realizar esta operación")
        self.cajones -= cantidad
        
class MiLote(Lote):
    def __init__(self, nombre, cajones, precio, factor):
        # Fijate como es el llamado a `super().__init__()`
        super().__init__(nombre, cajones, precio)
        self.factor = factor
        
    def rematar(self):
        self.vender(self.cajones)

    def costo(self):
        costo_orig = super().costo() #llamar a metodo de clase base
        return self.factor * costo_orig