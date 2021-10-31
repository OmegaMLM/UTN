'''
Control electoral
'''

# Carga de datos
apellido = input('Introduzca el apellido: ')
nombre = input('Introduzca el nombre: ')
votos = int(input('Introduzca la cantidad de votos: '))
votos_x = 'x' * votos
# Salida en pantalla
print('Apellido:', apellido, '-', 'Nombre:', nombre, '-', 'Votos:', '(', votos, ')')
print('Cantidad de votos:', votos_x)
