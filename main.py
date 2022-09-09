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
