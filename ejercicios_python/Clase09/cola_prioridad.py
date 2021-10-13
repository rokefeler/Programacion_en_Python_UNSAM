class ColaPrioridad:

    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []
        self.items_con_prioridad = []

    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def encolar_prioritario(self, x):
        '''Encola el elemento x.'''
        self.items_con_prioridad.append(x)

    def proximo(self):
        '''Devuelve el próximo elemento sin desencolar
        Requiere que la cola no sea vacía'''
        if len(self.items_con_prioridad):
            res = self.items_con_prioridad[0]
        else:
            res = self.items[0]
        return res

    def desencolar(self):
        '''Elimina el primer elemento de la cola
        y devuelve su valor.
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')

        if len(self.items_con_prioridad):
            res = self.items_con_prioridad.pop(0)
        else:
            res = self.items.pop(0)
        return res

    def largo_cola(self):
        '''Devuelve el largo de la cola.'''
        return len(self.items) + len(self.items_con_prioridad)

    def esta_vacia(self):
        '''Devuelve
        True si la cola esta vacia,
        False si no.'''
        return self.largo_cola() == 0

    def imprimir(self):
        res = "Normal: <"
        res += ", ".join(self.items)
        res += ">\n"
        res += "Prioridad: <"
        res += ", ".join(self.items_con_prioridad)
        res += ">"
        if not self.esta_vacia():
            res += "\n"
            res += f"Prox: {self.proximo()}"
        res += "\n"
        print(res)

