'''
Duración de un vuelo.
'''

# Carga de datos
hotel = 45
horas = int(input('Introduzca las horas de vuelo: '))
minutos = int(input('Intruduzca los minutos de vuelo: '))
minutos_totales = (horas * 60) + minutos + hotel

# Salida en pantalla
print('La hora de llegada al hotel sera de: ', minutos_totales)
