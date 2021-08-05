cadena = "Ejemplo con for"
vocal_o=0
for c in cadena:
    if c=='o' or c=='O':
        vocal_o=vocal_o+1
    print('caracter:', c)

print('Se encontró', vocal_o, ' vocales o')    