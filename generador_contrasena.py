import random
from typing import Mapping

def generar_contrasena():
    MAYUS = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
     'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z')
    MINUS = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
     'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z')
    NUMS = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
    CHARS = ('*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}',
     ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"')

    caracteres = MAYUS + MINUS + NUMS + CHARS

    contrasena = []

    for _ in range(15):
        character_random = random.choice(caracteres)
        contrasena.append(character_random)
    
    contrasena = "".join(contrasena)  #Convierte la lista a un String
    return contrasena



def run():
    contrasena = generar_contrasena()
    print(f"Su nueva contraseña es: {contrasena}")


if __name__ == "__main__":
    run()
