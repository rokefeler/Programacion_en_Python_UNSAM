#frase = 'todos somos programadores'
#frase = 'Los hermanos sean unidos porque ésa es la ley primera'
def traductor_neutro(frase):
    palabras = frase.split()
    frase_t=[]
    for palabra in palabras:
        if palabra[-1]=='o':
            frase_t.append(palabra[:-1]+'e')
        elif len(palabra)>2 and palabra[-2]=='o': #fix
            frase_t.append(palabra[:-2]+'e'+palabra[-1])
        else:
            frase_t.append(palabra)
    #print(' '.join(frase_t))
    return ' '.join(frase_t)
    
print(traductor_neutro('todos somos programadores'))
print(traductor_neutro('Los hermanos sean unidos porque ésa es la ley primera'))
print(traductor_neutro('¿cómo transmitir a los otros el infinito Aleph?'))
print(traductor_neutro('Todos, tu también'))
    #'todes somes programadores'