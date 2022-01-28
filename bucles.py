# While

def run():
    LIMITE = 1000

    contador = 0
    potencia_2 = 2**contador
    while potencia_2 < LIMITE:
        print(f"2 elevado a {contador} es igual a {potencia_2} ")
        contador = contador + 1
        potencia_2 = 2**contador


if __name__ == "__main__":
    run()


"""
Contador del 1 al 50

# While
contador = 1
print(contador)
while contador < 50:
    contador += 1
    print(contador)

# For
for contador in range(51):
    print(contador)

"""

"""
range(51)
a = list(range(51))
print(a)
"""