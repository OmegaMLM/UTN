'''
Calculo Distancia de Viaje
'''

# Carga de datos
kmtotales = 3641.3
mrecorridos = float(input('Introduzca los metros recorridos: '))

# Proceso
mtotales = kmtotales * 1000
kmrecorridos = mrecorridos // 1000
porcentaje = mrecorridos / mtotales * 100

# Salida en pantalla
print('Kilómetros recorridos:', kmrecorridos, '\nMetros recorridos:', mrecorridos, 'Porcentaje recorrido:',
      round(porcentaje))
