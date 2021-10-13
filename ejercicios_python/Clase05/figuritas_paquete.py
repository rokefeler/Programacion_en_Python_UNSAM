# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 23:51:07 2021

@author: rokefeler@gmail.com
#Ejercicios con Paquetes
"""
import numpy as np
import random
import matplotlib.pyplot as plt
#%%
def crear_album(figus_total):
    return np.zeros([figus_total], dtype=int)
#%%
#Ejercicio 5.11: Incompleto
def album_incompleto(A):
    return min(A)==0
#%%
#Ejercicio 5.17: genere un paquete (lista) de figuritas al azar
def comprar_paquete(figus_total, figus_paquete):
    return random.sample(range(figus_total), figus_paquete)
    
#Ejercicio 5.18: simule su llenado y devuelva cuántos paquetes se debieron comprar para completarlo
def cuantos_paquetes(figus_total, figus_paquete):
    #Iniciamos con un álbum vacío y sin haber comprado ninguna figurita.
    album = crear_album(figus_total)
    npaquetes_comprados = 0 #Inicializamos contador de paquetes de figuras
    while min(album)==0:
        paquete = comprar_paquete(figus_total, figus_paquete)
        album[paquete]+=1  #sumo 1 en cada posicion correspondiente a cada una de las figuritas 
        npaquetes_comprados +=1
    return npaquetes_comprados

def experimento_figus_paquete(n_repeticiones=100,figus_total=670, figus_paquete=5):
    resultados = np.array([cuantos_paquetes(figus_total,figus_paquete) for i in range(n_repeticiones)])
    return np.mean(resultados)  
#%% #graficar
def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop()] = 1
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)        
    return historia_figus_pegadas
#%%    
#Ejercicio 5.19 Calculá n_repeticiones = 100 veces la función cuantos_paquetes, 
#utilizando figus_total = 670, figus_paquete = 5.
if __name__ == "__main__":
    n_repeticiones = 100
    n_figus_album = 670
    n_figus_en_paquete = 5
    prom = experimento_figus_paquete(n_repeticiones, n_figus_album, n_figus_en_paquete)
    print(f'Para llenar el Album de {n_figus_album} figuritas con {n_repeticiones} repeticiones')
    print(f'Se necesita COMPRAR un Promedio de {prom:.0f} Paquetes de Figuras')
    # Para 100 repeticiones
    # Para llenar el Album de 670 figuritas con 100 repeticiones
    # Se necesita COMPRAR un Promedio de 961 Paquetes de Figuras
    
    # Para 1000 repeticiones
    # Para llenar el Album de 670 figuritas con 1000 repeticiones
    # Se necesita COMPRAR un Promedio de 950 Paquetes de Figuras
    
    
    #---------------------------------------------------------
    figus_total = 670
    figus_paquete = 5

    plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
    plt.xlabel("Cantidad de paquetes comprados.")
    plt.ylabel("Cantidad de figuritas pegadas.")
    plt.title("La curva de llenado se desacelera al final")
    plt.show()