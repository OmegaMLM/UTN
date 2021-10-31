'''
Desafió 1 - AED - UTN - Primer año
'''

print('Calculadora de horas, minutos  y segundo, a base de segundos.')

# Carga de datos
si = int(input('Segundos iniciales: '))

# Proceso
horas = si // 3600
sr = si % 3600
minutos = sr // 60
sf = si % 60

# Salida en pantalla
print('Horas:', horas, 'Minutos:', minutos, 'Segundos:', sf)

print('Calculadora de segundos a base de horas, minutos y segundos')

#Carga de datos
hora=int(input('Horas:'))
min=int(input('Minutos:'))
segundos=int(input('Segundos:'))
#Proceso
segundoshora= hora * 3600
segundosmin= min * 60
segundostotales= segundoshora + segundosmin + segundos

#Salida en pantalla
print('Segundos finales:', segundostotales)