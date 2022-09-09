# Reto-inicial

El link al repositorio es el siguiente: [ GitHub](https://github.com/jzazooro/Reto-inicial.git)

D

### CODIGO CABALLO

def formulauno(ind):
    solucion = 6*ind+8*ind-4+4*ind-4
    return solucion
    
### CODIGO REINA
    
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
    
    
### CODIGO MAIN

from clases.caballo import formulauno
from clases.reina import formulados
def main():

    print("Ejercicio del caballo")
    n=int(input("¿cuantos movimientos desea que haga el caballo?: "))
    h=formulauno(n)
    h=str(h)
    print("hay", h,"posibilidades de movimiento")

    print("Ejercicio de la reina")
    t=int(input("¿cuantas casillas quiere que tenga el tablero en cada lado?: "))
    resultado=formulados(t)
    print(resultado, "reinas")

if __name__=='main':
    main()
