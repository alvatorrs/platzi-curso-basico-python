"""Podemos desempaquetar o descomprimir las tuplas"""


#cuando conocemos la cantidad de elementos
numeros = (1,2,3,4,5)
num1, num2, num3, num4, num5 = numeros

print(num1)
print(num2)
print(num3)
print(num4)
print(num5,'\n')

#cuando no conocemos la cantidad de elementos
uno, dos, tres, cuatro, *valores_sobrantes = (1,2,3,4,5,6,7,8,9,10)
# con * hacemos que 'valores_sobrantes' almacene el resto de valores
# con * queremos decir que la variable es una lista
print(uno)
print(dos)
print(tres)
print(cuatro)
print(valores_sobrantes,'\n')

#omitir el resto de valores
uno, dos, tres, cuatro, *_ = (1,2,3,4,5,6,7,8,9,10)
# con *_ ignoramos el resto de valores faltantes 
# _ nos permite omitir algun valor
print(uno)
print(dos)
print(tres)
print(cuatro,'\n')

#omitiendo valores intermedios
n1, n2, n3, *_, n9, n10 = (1,2,3,4,5,6,7,8,9,10)
print(n1)
print(n2)
print(n3)
print(n9)
print(n10,'\n')


#omitimos valores arbitrarios
a, _, c, d, *lista, _, e = (1,2,3,4,5,6,7,8,9,10)
print(a)
print(c)
print(d)
print(lista)
print(e)
