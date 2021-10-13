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

    def proximo(self):
        '''Devuelve el próximo elemento sin desencolar
        Requiere que la cola no sea vacía'''
        return self.items[0]

    def desencolar(self):
        '''Elimina el primer elemento de la cola
        y devuelve su valor.
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def largo_cola(self):
        '''Devuelve el largo de la cola.'''
        return len(self.items)

    def esta_vacia(self):
        '''Devuelve
        True si la cola esta vacia,
        False si no.'''
        return self.largo_cola() == 0

    def imprimir(self):
        res = "<"
        res += ", ".join(self.items)
        res += ">"
        if not self.esta_vacia():
            res += "\n"
            res += f"Prox: {self.proximo()}"
        res += "\n"
        print(res)

