# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 00:11:08 2021

@author: rokefeler@gmail.com
"""

import random
def tirar(n_dados=5):
    n_caras_dado = 6
    caras = [x for x in range(1,n_caras_dado)]  #dara [1,2,3,4,5,6]
    tirada = random.choices(caras,k=n_dados) #Resultado de n_dados lanzados
    #debug print(f'Resultado de tirar {n_dados} dados: {tirada}')
    return tirada

def es_generala(tirada):
    if len(tirada) != 5:  #Si longitud final no es 5 devolver Falso
        return False
    dado = sum(tirada)//len(tirada) #division entera
    return dado == tirada[0]

def extraer_dado(tirada, cara=None):
    '''devuelve una tupla indicando Dado, Cant.Veces'''
    tupla_devolver = None
    contar = list( { (i,tirada.count(i)) for i in tirada }) #Generar tuplas con Dado y Cantidad de veces que se repite
    if cara == None:
        contar.sort(key = lambda x: x[1], reverse=True)
        tupla_devolver = contar[0]    #devolver primer elemento
    else:
        tupla_devolver = (cara,tirada.count(cara))
    #debug print(f'Tupla resultado de extraer_dado({tirada},{cara}): {tupla_devolver}')
    return tupla_devolver
#%%    
def jugar(total_dados_a_jugar=5,ntiros=3, verbose=False):
    #total_dados_a_jugar = 5
    n_dados_a_jugar = total_dados_a_jugar #inicialmente 5 dados
    resultado =[]       #aqui se almacenan los dados escogidos
    nlances = 0
    dado_escogido = None
    #ntiros = 3          #Cant.l de tiros Disponibles
    while ntiros>0 and n_dados_a_jugar>0 and len(resultado)<5:
        nlances +=1
        tirada = tirar(n_dados_a_jugar)
        ntiros -= 1
        
        
       
        #tupla_dado_mas_alto
        dado, ocurrencias = extraer_dado(tirada,dado_escogido)
        if dado_escogido == None:
            dado_escogido = dado
        #debug print(f'Tupla mas alta: ({dado},{ocurrencias})')
        if ocurrencias > 0:
            resultado = resultado + ocurrencias*[dado]
        n_dados_a_jugar = total_dados_a_jugar - len(resultado)
        if verbose:
            print(f'#Dados a Jugar:{n_dados_a_jugar}')        
            print(f'Tirada:{tirada} en {nlances} lances')
            print(f'resultado acumulado actual: {resultado}')
            
        #if len(resultado)==5 and es_generala(resultado):
        #    break;
        
    #return {'tiros':ntiros, 'resultado':resultado, 'es_generala': es_generala(resultado)}
    return resultado
#%% 
#Test para calcular la Probabilidad con N Juegos
def test(N):
    #se agrega variabe temporal verbose para hacer 
    #test de cada tirada, (demora mas tiempo por Imprimir)
    G = sum([es_generala(jugar(verbose=False)) for i in range(N)])
    prob = (G/N)
    print(f'Jugue {N} veces, de las cuales {G} saqué generala servida.')
    print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')
    
if __name__ == "__main__":
    N = 100000
    test(N)
    



