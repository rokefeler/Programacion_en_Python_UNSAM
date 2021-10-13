# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 21:42:49 2021

@author: FamiliaRoqueSosa
"""
import numpy as np
import matplotlib.pyplot as plt

def plotear_temperaturas():
    temperaturas = np.load('temperaturas.npy')
    plt.hist(temperaturas,bins=115)
    plt.show() #el show no hace falta en algunos entornos. A veces lo omitiremos.
    
if __name__ == "__main__":
    plotear_temperaturas()
