print("Selecciona una de las siguientes opciones.")
print(''' [1] Convertir peso Mx a dolar Us\n [2] Convertir dolar Us a peso Mx\n''')
opcion = int(input("Opcion: "))


def conversion_pesos_dolar(pesos):
    valor_dolar = 19.95
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")

def conversion_dolares_peso(dolar):
    valor_peso = 1/(19.95)
    pesos = dolar/valor_peso
    pesos = round(pesos,2)
    pesos = str(pesos)
    print("Tienes $" + pesos + " pesos")   


if opcion == 1:
    print("Convertir peso Mx a dolar Us\n")
    pesos = float(input("Cantidad de pesos: "))
    conversion_pesos_dolar(pesos)
elif opcion == 2:
    print("Convertir dolar Us a peso Mx\n")
    dolar = float(input("Cantidad de dolares: "))
    conversion_dolares_peso(dolar)

