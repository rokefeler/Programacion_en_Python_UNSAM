# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 22:45:00 2021

@author: rokefeler@gmail.com
#Ejercicios con figus sueltas
"""
import numpy as np
import random
import matplotlib.pyplot as plt
#%%
#Ejercicio 5.10: Crear
def crear_album(figus_total):
    return np.zeros([figus_total], dtype=int)
#%%
#Ejercicio 5.11: Incompleto
def album_incompleto(A):
    return min(A)==0
#%%
#Ejercicio 5.12: Comprar
''' devuelva un número entero aleatorio que representa la figurita que nos tocó'''
def comprar_figu(figus_total):
    return random.randint(1,figus_total)

#%%
#Ejercicio 5.13: Cantidad de compras
def cuantas_figus(figus_total):
    '''devuelva la cantidad de figuritas que se debieron comprar para completarlo '''
    
    #Iniciamos con un álbum vacío y sin haber comprado ninguna figurita.
    album = crear_album(figus_total)
    
    #Inicializamos contador de figuritas
    nfigus_compradas = 0
    #Compramos figuritas (de a una) hasta llenar el álbum; 
    #es decir, se repite la acción (el paso) de comprar y pegar figuritas mientras 
    #(while) el álbum está incompleto.
    while album_incompleto(album):
        figu = comprar_figu(figus_total)
        album[figu-1]+=1
        nfigus_compradas +=1
    return nfigus_compradas

#%%
#Ejercicio 5.15: simula y devuelva el número estimado de figuritas que hay que comprar, 
#en promedio, para completar el álbum
def experimento_figus(n_repeticiones, figus_total):
    resultados = np.array([cuantas_figus(figus_total) for i in range(n_repeticiones)])
    return np.mean(resultados)
    
#%%
#Ejercicio 5.17: genere un paquete (lista) de figuritas al azar
def comprar_paquete(figus_total, figus_paquete,repetidos=True):
    if repetidos:
        return random.choices(range(figus_total), k=figus_paquete)
    else: #Elementos únicos no repetidos
        return random.sample(range(figus_total), figus_paquete)
    
#Ejercicio 5.18: simule su llenado y devuelva cuántos paquetes se debieron comprar para completarlo
# se agrega parametro opcional para reutilizar y cumplir consigna de 5.23 con repetidos
def cuantos_paquetes(figus_total, figus_paquete,hayRepetidosEnPaquete=True):
    #Iniciamos con un álbum vacío y sin haber comprado ninguna figurita.
    album = crear_album(figus_total)
    npaquetes_comprados = 0 #Inicializamos contador de paquetes de figuras
    while min(album)==0:
        paquete = comprar_paquete(figus_total, figus_paquete,hayRepetidosEnPaquete)
        album[paquete]+=1  #sumo 1 en cada posicion correspondiente a cada una de las figuritas 
        npaquetes_comprados +=1
    return npaquetes_comprados

def experimento_figus_paquete(n_repeticiones=100,figus_total=670, figus_paquete=5, hayRepetidosEnPaquete=True):
    resultados = np.array([cuantos_paquetes(figus_total,figus_paquete,hayRepetidosEnPaquete) for i in range(n_repeticiones)])
    #visualizamos la simulacion con un histograma de las corridas
    #promedio = np.mean(resultados)
    return resultados
#%%
def graficar_simulacion_paquetes(resultados,nbins=70):
    promedio = np.mean(resultados)
    plt.hist(resultados, bins=nbins)
    plt.axvline(promedio, color='r')
    plt.legend(["%.2f paquetes" % promedio])
    plt.title("Cant. paquetes en promedio para llenar 1 album")
    plt.show()
def graficar_curva_llenado(figus_total,figus_paquete):
    plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
    plt.xlabel("Cantidad de paquetes comprados.")
    plt.ylabel("Cantidad de figuritas pegadas.")
    plt.title("La curva de llenado se desacelera al final")
    plt.show()
#%%

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

def experiento_figus_grupo(n_albunes,n_repeticiones,n_figus_album,n_figus_en_paquete):
    # Cod. referencia de: https://www.lanacion.com.ar/sociedad/rusia-2018-cuantos-sobres-de-figuritas-hacen-falta-para-llenar-el-album-del-mundial-nid2125275/   
    #inicializo el vector simulacion_grupo con 2 dimensiones 
    simulacion_grupo = np.zeros([n_albunes+1,n_repeticiones], dtype=int)
    #voy a realizar muchas corridas, tantas como dice parametro n_repeticiones
    for i in range(n_repeticiones):
      #modelo el album vacio como un vector lleno de ceros
      album = np.zeros(n_figus_album, dtype=int)
    
      #en esta variable contabilizare cuantos sobres se necesitan para llenar 1..n albumes
      cantidad_de_sobres = 0
    
      #aqui voy a contabilizar cuando albumes estan llenos
      albumes_llenos = 0
    
      #a diferencia de la simulacion anterior, la condicion de corte sera cuando se 
      #llenen los n albumes. Eso lo podemos expresar asi:
    	#albumes_llenos < n_albunes
      while albumes_llenos < n_albunes:
    
        #un nuevo sobre formado por figuritas tomadas de manera aleatoria
        sobre = random.sample(range(n_figus_album), n_figus_en_paquete) #sample no devuelve repetidos
    
        #voy llenando los albumes
        album[sobre] += 1
    
        #incremento la cantidad de sobres en 1
        cantidad_de_sobres += 1
    
        #si el min(album) se incremento, significa que se ha llenado un nuevo album. 
        if albumes_llenos < min(album):
          #hemos llenado un album nuevo
          albumes_llenos = min(album)
    
          #registramos la cantidad de sobres
          simulacion_grupo[albumes_llenos, i] = cantidad_de_sobres
    
    
    #cuantos sobres necesitamos en promedio para llenar n-albumes
    #usamos una matriz de histogramas
    print ("Llenar %d albumes costara... %2.f pesos por integrante. Que bueno es tener amigos!" % (n_albunes, (simulacion_grupo[n_albunes]/n_albunes).mean() * 15))
    
    # amigos = [2, 5, 10, 20]
    
    # fig, axes = plt.subplots(nrows=2, ncols=2, sharey=True, sharex=True)
    
    # for ax, q in zip(axes.flat, amigos):
    #   simulacion = simulacion_grupo[q]/q
    #   sobres_promedio = simulacion.mean()
    #   ax.set_title('$albumes=%d $' % (q))
    #   ax.hist(simulacion, bins=50)
    #   ax.axvline(sobres_promedio, color='r')
    #   ax.legend(["%.2f sobres" % sobres_promedio])
    
    # fig.suptitle("Cantidad de sobres en promedio para llenar $n$ albumes")
    # plt.show()
    
    #Otra forma de visualizar la cantidad promedio de sobres para llenar n-albumes
    # plt.boxplot([simulacion_grupo[i]/i for i in xrange(1,n_albunes+1)])
    # plt.title("Cantidad de sobres para llenar $n$ albumes")
    # plt.show()
    
    
#%%
#Ejercicio 5.14: estimá cuántas figuritas hay que comprar, en promedio, para completar el álbum de seis figuritas
if __name__ == "__main__":
    n_repeticiones = 1000
    n_figus_album = 6
    resultados = np.array([cuantas_figus(n_figus_album) for i in range(n_repeticiones)])
    print(f'Para llenar el Album de {n_figus_album} figuritas con {n_repeticiones} repeticiones')
    print(f'Se necesita COMPRAR un Promedio de {np.mean(resultados):.0f} figuras')
    # Para llenar el Album de 6 figuritas con 1000 repeticiones
    # Se necesita COMPRAR un Promedio de 14 figuras

#%%    
    #Ejercicio 5.15: ¿Cuánto te da para 100 repeticiones en un álbum de 670 figuritas?
    print('Espere, calculando otra simulación 5.15...')
    n_repeticiones = 100
    n_figus_album = 670
    prom = experimento_figus(n_repeticiones, n_figus_album)
    print(f'Para llenar el Album de {n_figus_album} figuritas con {n_repeticiones} repeticiones')
    print(f'Se necesita COMPRAR un Promedio de {prom:.0f} figuras')
    # Para llenar el Album de 670 figuritas con 100 repeticiones
    # Se necesita COMPRAR un Promedio de 4780 figuras

#%%    
    #---------------------------------------------------
    #Ejercicio 5.19 Calculá n_repeticiones = 100 veces la función cuantos_paquetes, 
    #utilizando figus_total = 670, figus_paquete = 5.
    #En esta opción pueden salir figuritas repetidas en un mismo paquete
    print('Espere, calculando otra simulación 5.19 ...')
    n_repeticiones = 100
    n_figus_album = 670
    n_figus_en_paquete = 5
    resultados = experimento_figus_paquete(n_repeticiones, n_figus_album, n_figus_en_paquete)
    prom = np.mean(resultados)
    print(f'Para llenar el Album de {n_figus_album} figuritas con {n_repeticiones} repeticiones')
    print(f'Se necesita COMPRAR un Promedio de {prom:.0f} Paquetes de Figuras')
    print('Revise Grafico de Curva de Llenado')
    graficar_curva_llenado(n_figus_album,n_figus_en_paquete)
    
    #-----------------------------------------------------------------    
    #Ejercicio 5.20 estimá la probabilidad de completar el álbum con 850 paquetes o menos.
    #p= G / N, G=Cuantas se cumplieron
    probabilidad = (resultados <= 850).sum() / n_repeticiones
    print(f'La probabilidad de Completar el album con 850 paquetes o menos es de {probabilidad:.4f}%')
        
    #Ejercicio 5.21 Plotear el histograma
    print('Revise grafica de histograma solicitada 5.21')
    graficar_simulacion_paquetes(resultados,nbins=65)
    # Para 100 repeticiones
    # Para llenar el Album de 670 figuritas con 100 repeticiones
    # Se necesita COMPRAR un Promedio de 961 Paquetes de Figuras
    
    # Para 1000 repeticiones
    # Para llenar el Album de 670 figuritas con 1000 repeticiones
    # Se necesita COMPRAR un Promedio de 950 Paquetes de Figuras
    
    #-----------------------------------------------------------------    
    #Ejercicio 5.22 estimá cuántos paquetes habría que comprar para tener una chance del 90% de completar el álbum.
    #Si p = G/N,  p=90%, N=10000, entonces G=p*N
    probabilidad = 0.0
    n_paquetes_estimar = 0
    while probabilidad<90.0:
        n_paquetes_estimar+=1
        probabilidad = (resultados <= n_paquetes_estimar).sum() / n_repeticiones
    print(f'5.22 Para tener un Chance del 90%, hay que comprar {n_paquetes_estimar} paquetes')
    print(f"{25*'-'}")
    
#%%
    #----------------------------------------------------------------
    #----------------------------------------------------------------
    #Ejercicio 5.23 suponiendo que hay figuritas repetidas
    n_repeticiones = 1000
    n_figus_album = 670
    n_figus_en_paquete = 5
    HayFigurasRepetidasEnPaquete = False
    resultados = experimento_figus_paquete(n_repeticiones, n_figus_album, n_figus_en_paquete, HayFigurasRepetidasEnPaquete)
    prom = np.mean(resultados)
    print('Volviendo analizar - SIN FIGURAS REPETIDAS EN PAQUETE')
    print(f'Para llenar el Album de {n_figus_album} figuritas con {n_repeticiones} repeticiones')
    print(f'Se necesita COMPRAR un Promedio de {prom:.0f} Paquetes de Figuras')
    print('Revise Grafico de Curva de Llenado Sin Repetidos')
    graficar_curva_llenado(n_figus_album,n_figus_en_paquete)
    
    #p= G / N, G=Cuantas se cumplieron
    probabilidad = (resultados <= 850).sum() / n_repeticiones
    print(f'La probabilidad de Completar el album con 850 paquetes o menos es de {probabilidad:.4f}%')
        
    print('Revise grafica de histograma solicitada 5.21')
    graficar_simulacion_paquetes(resultados,nbins=65)
    
    #-----------------------------------------------------------------    
    #estimá cuántos paquetes habría que comprar para tener una chance del 90% de completar el álbum.
    probabilidad = 0.0
    n_paquetes_estimar = 0
    while probabilidad<90.0:
        n_paquetes_estimar+=1
        probabilidad = (resultados <= n_paquetes_estimar).sum() / n_repeticiones
    print(f'... Para tener un Chance del 90%, hay que comprar {n_paquetes_estimar} paquetes')
#%%
        
