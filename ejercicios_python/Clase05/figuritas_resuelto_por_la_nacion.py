# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 22:02:10 2021

@author: rokefeler@gmail.com
Source: https://www.lanacion.com.ar/sociedad/rusia-2018-cuantos-sobres-de-figuritas-hacen-falta-para-llenar-el-album-del-mundial-nid2125275/
"""
import random
import numpy as np
import matplotlib.pyplot as plt
#%%
def llenar_albumFiguritas_solo():
    #las constantes de la simulacion
    FIGURITAS_POR_PAQUETE = 5
    FIGURITAS_POR_ALBUM = 669
    CANTIDAD_DE_CORRIDAS = 1000
    #pensemos un grupo de 20 amigos que se juntan para llenar cada uno su album
    CANTIDAD_DE_ALBUMES = 20
    print(f"Cuántos sobres se necesitan para llenar el 1 album de {FIGURITAS_POR_ALBUM} figuritas")
    
    
    #inicializo el vector simulacion
    #alli voy a ir registrando cuantos sobres necesito en cada corrida
    simulacion = np.empty(CANTIDAD_DE_CORRIDAS)
    
    #voy a realizar tantas corridas como dice la constante CANTIDAD_DE_CORRIDAS
    for i in range(CANTIDAD_DE_CORRIDAS):
    
    	#modelo el album vacio como un vector lleno de ceros
    	album = np.zeros(FIGURITAS_POR_ALBUM, dtype=int)
    
    	#en esta variable contabilizare cuantos sobres se necesitan 
    	cantidad_de_sobres = 0
    
    	#voy abriendo sobres nuevos hasta llenar el album
    	#si el vector contiene algun 0 en alguna posicion significa 
    	#que aun no esta completo esa condicion la podemos expresar de muchas 
    	#formas la que elegi es min(album) == 0, 
    	#tambien podria ser len(album[album == 0]) > 0 
    	while min(album) == 0:
    
    		#un nuevo sobre formado por figuritas tomadas de manera aleatoria
    		sobre = random.sample(range(FIGURITAS_POR_ALBUM), FIGURITAS_POR_PAQUETE)
    
    		#voy llenando el album
    		#sumo 1 en cada posicion correspondiente a cada una de las figuritas 
            #Nota: para quienes conocen otros lenguajes de programacion, esta 
            #operacion puede llegar a causar confusion. La libreria NumPy permite
            #realizar operaciones sobre multiples indices a la vez. 
            #Aprovechenla, es muy util.
    		album[sobre] += 1
    
    		#incremento la cantidad de sobres en 1
    		cantidad_de_sobres += 1
    
            #para llenar este album he necesitado tantos sobres como 
            #lo dice cantidad_de_sobres
    	simulacion[i] = cantidad_de_sobres
    
    #cuantos sobres necesitamos en promedio para llenar el album
    sobres_promedio = simulacion.mean()
    print(f"Llenar el album costará...{sobres_promedio * 15:.2f} pesos")
    print(f"Y qué hago con las {sobres_promedio * FIGURITAS_POR_PAQUETE - FIGURITAS_POR_ALBUM:.2f} repetidas!")
    
    #visualizamos la simulacion con un histograma de las corridas
    plt.hist(simulacion, bins=50)
    plt.axvline(sobres_promedio, color='r')
    plt.legend(["%.2f sobres" % sobres_promedio])
    plt.title("Cantidad de sobres en promedio para llenar 1 album")
    plt.show()

#%%
def llenar_albumFiguritas_grupode(CANTIDAD_DE_ALBUMES=20):
    #pensemos un grupo de 20 amigos que se juntan para llenar cada uno su album

    FIGURITAS_POR_PAQUETE = 5
    FIGURITAS_POR_ALBUM = 669
    CANTIDAD_DE_CORRIDAS = 1000
    
     
    #inicializo el vector simulacion_grupo con 2 dimensiones 
    simulacion_grupo = np.zeros([CANTIDAD_DE_ALBUMES+1,CANTIDAD_DE_CORRIDAS], dtype=int)
    #voy a realizar muchas corridas, tantas como dice la constante CANTIDAD_DE_CORRIDAS
    for i in range(CANTIDAD_DE_CORRIDAS):
      #modelo el album vacio como un vector lleno de ceros
      album = np.zeros(FIGURITAS_POR_ALBUM, dtype=int)
    
      #en esta variable contabilizare cuantos sobres se necesitan para llenar 1..n albumes
      cantidad_de_sobres = 0
    
      #aqui voy a contabilizar cuando albumes estan llenos
      albumes_llenos = 0
    
      #a diferencia de la simulacion anterior, la condicion de corte sera cuando se 
      #llenen los n albumes. Eso lo podemos expresar asi:
    	#albumes_llenos < CANTIDAD_DE_ALBUMES
      while albumes_llenos < CANTIDAD_DE_ALBUMES:
    
        #un nuevo sobre formado por figuritas tomadas de manera aleatoria
        sobre = random.sample(range(FIGURITAS_POR_ALBUM), FIGURITAS_POR_PAQUETE)
    
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
    
    amigos = [2, 5, 10, 20]
    
    fig, axes = plt.subplots(nrows=2, ncols=2, sharey=True, sharex=True)
    
    for ax, q in zip(axes.flat, amigos):
      simulacion = simulacion_grupo[q]/q
      sobres_promedio = simulacion.mean()
      ax.set_title('$albumes=%d $' % (q))
      ax.hist(simulacion, bins=50)
      ax.axvline(sobres_promedio, color='r')
      ax.legend(["%.2f sobres" % sobres_promedio])
    
    fig.suptitle("Cantidad de sobres en promedio para llenar $n$ albumes")
    plt.show()
    
    #Otra forma de visualizar la cantidad promedio de sobres para llenar n-albumes

    plt.boxplot([simulacion_grupo[i]/i for i in xrange(1,CANTIDAD_DE_ALBUMES+1)])
    plt.title("Cantidad de sobres para llenar $n$ albumes")
    plt.show()
    
    print ("Llenar %d albumes costara... %2.f pesos por integrante. Que bueno es tener amigos!" % (CANTIDAD_DE_ALBUMES, (simulacion_grupo[CANTIDAD_DE_ALBUMES]/CANTIDAD_DE_ALBUMES).mean() * 15))
    
#%%
if __name__ == "__main__":
    llenar_albumFiguritas_grupode(20)   