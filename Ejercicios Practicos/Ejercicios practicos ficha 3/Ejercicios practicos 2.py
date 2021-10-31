'''
Fecha con cadena
'''

# Carga de datos
fecha = input('Introduzca la fecha en formato de dd/mm/aaaa: ')

# Proceso
dia = fecha[0:2]
mes = fecha[3:5]
año = fecha[6:10]

# Salida en pantalla
print('Dia:', dia, ' - ', 'Mes:', mes, ' - ', 'año:', año)
