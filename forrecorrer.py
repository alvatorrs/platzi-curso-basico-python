# Recorrer strings con For

from _typeshed import IdentityFunction
from typing import MappingView


def run():
    frase = input("Escribe un nombre: ")
    for caracter in frase:
        print(caracter.upper())


if __name__ == "__main__":
    run()
