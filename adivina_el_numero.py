# Juego de encontrar un número entre el 1 y el 100

import random

def run():
    numero_aleatorio = random.randint(1,100)
    numero_elegido = int(input("Elige un número entre el 1 al 100: "))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print("Busca un número más grande")
        else:
            print("Busca un número más chico")
        numero_elegido = int(input("Elige otro número: "))
    print("Ganaste!!")



if __name__ == "__main__":
    run()