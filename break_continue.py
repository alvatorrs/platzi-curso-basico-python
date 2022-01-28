#Continue

# def run1():
#     for contador in range(51):
#         if contador%2 != 0:
#             continue
#         print(contador)


# if __name__ == "__main__":
#     run1()


#Break

# def run2():
#     for i in range(51):
#         print(i)
#         if i == 25:
#             break


# if __name__ == "__main__":
#     run2()


numero = 0
eleccion = int(input('Ingrese un numero: '))
while numero < 10000:        
    if numero == eleccion:
        break
    numero += 1 
    if numero % 2 != 0:
        continue
    print(numero)
