# Conversor de monedas


def conversion(moneda,cantidad):
    if moneda == "dolares":
        factor = 19.95
    elif moneda == "pesos":
        factor = 1/(19.95)
    convertido = cantidad/factor
    convertido = round(convertido,2)
    print(f'Tienes {convertido} {moneda}')


def main():
    print("Selecciona una de las siguientes opciones.")
    print(''' [1] Convertir peso Mx a dolar Us
 [2] Convertir dolar Us a peso Mx\n''')
    opcion = int(input("Opcion: "))

    if opcion == 1:
        print("Convertir peso Mx a dolar Us\n")
        pesos = float(input("Cantidad de pesos: "))
        moneda = "dolares"
        conversion(moneda,pesos)
    elif opcion == 2:
        print("Convertir dolar Us a peso Mx\n")
        dolar = float(input("Cantidad de dolares: "))
        moneda = "pesos"
        conversion(moneda,dolar)
    else:
        print("\nIntentelo de nuevo 😂\n")
        main()

if __name__ == '__main__':
    main()
