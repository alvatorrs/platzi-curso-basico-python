"""Justificar texto"""

# recordemos que los strings son inmutables
saludo = 'Hola, mundo'

# justificar a la izquierda con ljust()
nuevo_saludo = saludo.ljust(20)
print(nuevo_saludo,'|')

# justificar a la derecha con rjust()
nuevo_saludo = saludo.rjust(20)
print('|',nuevo_saludo)

# centrar con center()
nuevo_saludo = saludo.center(20)
print('|',nuevo_saludo,'|')
