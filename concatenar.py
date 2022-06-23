"""Concatenar"""

nombre = 'Alvaro'
apellido = 'Torres'

# +
nombre_completo = 'Mr. ' + nombre + ' ' + apellido + ' Sánchez.'
print(nombre_completo)

# %s
nombre_completo = 'Mr. %s %s %s.' %(nombre, apellido, 'Sánchez')
print(nombre_completo)

# format()
nombre_completo = 'Mr. {} {} {}.'.format(nombre, apellido, 'Sánchez')
print(nombre_completo)

# format() con parametros
nombre_completo = 'Mr. {nombre} {apellido1} {apellido2}.'.format(
    nombre= nombre,
    apellido1= apellido,
    apellido2 = 'Sánchez'
)
print(nombre_completo)

# FString
nombre_completo = f'Mr. {nombre} {apellido} Sánchez.'
print(nombre_completo)
