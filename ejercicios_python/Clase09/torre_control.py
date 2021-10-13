# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 23:39:48 2021

@author: rokefeler@gmail.com
"""
class Cola:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []

    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def desencolar(self):
        '''Elimina el primer elemento de la cola 
        y devuelve su valor. 
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            return None
        return self.items.pop(0)

    def esta_vacia(self):
        '''Devuelve 
        True si la cola esta vacia, 
        False si no.'''
        return len(self.items) == 0
    
    def __str__(self):
        '''Imprime el Estado de una Cola'''
        if len(self.items):
            res = ""
            res += ", ".join(self.items)
        else:
            res = ""
        return res
#%%
#Ejercicio 9.12: Torre de Control
class TorreDeControl:
    def __init__(self):
        self.arribos = Cola()   #cola Prioritaria
        self.partidas = Cola()
    def nuevo_arribo(self,nombre):
        self.arribos.encolar(nombre)
        
    def nueva_partida(self,nombre):
        self.partidas.encolar(nombre)
    def ver_estado(self):
        print(f'Vuelos esperando para aterrizar: {self.arribos}')
        print(f'Vuelos esperando para despegar:: {self.partidas}')
    def asignar_pista(self):
        isArribo = False
        if not self.arribos.esta_vacia():
            vuelo=self.arribos.desencolar()
            isArribo = True
        else:
            vuelo=self.partidas.desencolar()
        
        if vuelo==None:
            print('No hay vuelos en espera.')
        else:
            if isArribo:
                print(f'El vuelo {vuelo} aterrizó con éxito.')
            else:
                print(f'El vuelo {vuelo} despegó con éxito.')

#%%    
if __name__ == '__main__':
    torre = TorreDeControl()
    torre.nuevo_arribo('AR156')
    torre.nueva_partida('KLM1267')
    torre.nuevo_arribo('AR32')
    torre.ver_estado()
    # Vuelos esperando para aterrizar: AR156, AR32
    # Vuelos esperando para despegar: KLM1267
    torre.asignar_pista()
    # El vuelo AR156 aterrizó con éxito.
    torre.asignar_pista()
    # El vuelo AR32 aterrizó con éxito.
    torre.asignar_pista()
    # El vuelo KLM1267 despegó con éxito.
    torre.asignar_pista()
    # No hay vuelos en espera.