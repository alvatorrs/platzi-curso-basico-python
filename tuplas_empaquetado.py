"""comprimir elementos para generar tuplas"""

lista1 = [1,2,3,4,5]
print('lista1:', lista1)
tupla1 = (10,20,30,40,50)
print('tupla1:', tupla1)
lista2 = [100,200,300,400,500, 600]
print('lista2:', lista2)
tupla2 = (1000,2000,3000,4000,5000)
print('tupla2:', tupla2)

#utilizando zip() combinaremos los valores de cada iterable en tuplas
# zip() retorna un objeto tipo zip
resultado = zip(lista1, tupla1, lista2, tupla2)
print('\nobjeto zip:',resultado,'\n')

#convertimos a una tupla
resultado = tuple(resultado)
print('zip tuplada:', resultado)

#si los iterables tienen distinta longitud, 
#los elementos sobrantes serán omitidos por zip()
#las tuplas de zip() siempre tendrán la misma longitud
