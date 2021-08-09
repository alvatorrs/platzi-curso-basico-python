def conversor(tipo_pesos,valor_dolar):
    pesos = input(f"¿Cuántos pesos {tipo_pesos} tienes?: ")
    pesos = float(pesos)
    dolares = pesos/valor_dolar
    dolares= str(round(dolares,2))
    print(f"Tienes $ {dolares} dolares")


print("Selecciona el tipo de moneda a convertir.")
print(''' [1] Convertir peso Mexicano\n [2] Convertir peso Colombiano\n [3] Convertir peso Argentino\n''')
opcion = int(input("Opcion: "))


if opcion == 1:
    conversor("Mexicanos",19.95)  
elif opcion == 2:
    conversor("Colombianos",3875)
elif opcion == 3:
    conversor("Argentinos",65)

