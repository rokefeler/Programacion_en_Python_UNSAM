# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 23:04:08 2021

@author: rokefeler@gmail.com
"""

#canguros_buenos.py

class Canguro:
    """Un Canguro es un marsupial."""
    
    def __init__(self, nombre, contenido=[]):
        """Inicializar los contenidos del marsupio.

        nombre: string
        contenido: contenido inicial del marsupio, lista.
        """
        self.nombre = nombre
        #self.contenido_marsupio = contenido  ERROR
        self.contenido_marsupio = [] #inicializo siempre en vacio objeto
        if len(contenido):
            self.contenido_marsupio += contenido  #agregar contenido si existe

    def __str__(self):
        """devuelve una representación como cadena de este Canguro.
        """
        if len(self.contenido_marsupio)==0:
            t = [ self.nombre  + ' (no tiene nada en su marsupio)']
        else:
            t = [ self.nombre + ' tiene en su marsupio:' ]
            for obj in self.contenido_marsupio:
                # s = '    ' + object.__str__(obj)   ERROR object
                s = '  - ' + str(obj)  #llamo a método generico str en lugar de object.__str__
                t.append(s)
        return '\n'.join(t)

    def meter_en_marsupio(self, item):
        """Agrega un nuevo item al marsupio.
        item: objecto a ser agregado
        """
        self.contenido_marsupio.append(item)

#%%
madre_canguro = Canguro('Madre')
cangurito = Canguro('gurito')
madre_canguro.meter_en_marsupio('billetera')
madre_canguro.meter_en_marsupio('llaves del auto')
madre_canguro.meter_en_marsupio(cangurito)

print(madre_canguro)

# Al ejecutar este código todo parece funcionar correctamente.
# Para ver el problema, imprimí el contenido de cangurito.