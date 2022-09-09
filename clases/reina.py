class formulados():
    def __init__(self, t):
        self.t = t
    def tablero(self):
        tablero = []
        for i in range(self.t):
            fila=[]
            for m in range(self.t):
                fila.append(" ")
            tablero.append(fila)
        return tablero
    def desplazamiento(self):
        for i in range(self.t):
            for j in range(self.t):
                self.tablero()[i][j] == 'X'
    def efecto(self):
        self.desplazamiento()
        resultado = []
        for i in range(self.t):
            for j in range(self.t):
                if self.tablero()[i][j] == 'X':
                    resultado.append(self.tablero().index('X'))
                else:
                    pass
        return resultado
