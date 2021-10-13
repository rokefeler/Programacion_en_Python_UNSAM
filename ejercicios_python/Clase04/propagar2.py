def propagar(lista):
    l = lista.copy() 

    p = len(l)-1
    for i in range(p):
        c+=1
        if l[i]>0 and l[i+1] == 0:
            l[i+1] = 1
        if l[p-i] > 0 and l[p-(i+1)] == 0:
            l[p-(i+1)] = 1
    return l

#%% Prueba

# l1 = [ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]

# l11 = propagar(l1)
# Entrada: [0, 0, 0, -1, 1, 0, 0, 0, -1, 0, 1, 0, 0]
# Salida : [0, 0, 0, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1]
# En 25 operaciones

# l2 = [ 0, 0, 0, 1, 0, 0]

# l22 = propagar(l2)
# Entrada: [0, 0, 0, 1, 0, 0]
# Salida : [1, 1, 1, 1, 1, 1]
# En 11 operaciones

# s1 = propagar(l1)
# Entrada: [0, 0, 0, -1, 1, 0, 0, 0, -1, 0, 1, 0, 0]
# Salida : [0, 0, 0, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1]
# En 17 operaciones

# s2 = propagar(l2)
# Entrada: [0, 0, 0, 1, 0, 0]
# Salida : [1, 1, 1, 1, 1, 1]
# En 8 operaciones