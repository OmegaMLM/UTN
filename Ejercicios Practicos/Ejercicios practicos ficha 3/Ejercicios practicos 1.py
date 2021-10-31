'''
Plazo Fijo
'''

# Carga de datos
dinero_depositado = int(input('Introduzca la cantidad de dinero depositado:'))

# Proceso
recargo = dinero_depositado * 0.23
dinero_final = dinero_depositado + recargo - 20

# Salida en pantalla
print('Saldo en cuenta: ', dinero_final)
