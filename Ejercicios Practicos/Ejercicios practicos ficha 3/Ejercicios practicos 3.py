'''
Importe como cadena
'''

# Carga de datos
cantidad_dinero = float(input('Introduzca el importe: '))

# Proceso
dinerosigno = '$' + str(cantidad_dinero)
dineropesos = str(cantidad_dinero) + ' ' + 'Pesos'

# Salida en pantalla
print(dinerosigno, '-', dineropesos)
