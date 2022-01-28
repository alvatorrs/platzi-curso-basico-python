def run():
    
    diccionario = {
        "llave1": 1,
        "llave2": 2,
        "llave3": 3
    }
    # print(diccionario)
    # print(diccionario["llave1"])
    # print(diccionario["llave2"])
    # print(diccionario["llave3"])

    poblacion_paises = {
        "Mexico": 147000000,
        "Argentina": 44938712,
        "Brasil": 210147152,
        "Colombia": 50372424
    }
    # print(poblacion_paises["Mexico"])

#Mostrar llaves
    for pais in poblacion_paises.keys():
        print(pais)

#Mostrar valores
    for poblacion in poblacion_paises.values():
        print(poblacion)

#Mostrar ambos
    for pais, poblacion in poblacion_paises.items():
        print(f"{pais} tiene {poblacion} habitantes")

if __name__ == "__main__":
    run()
