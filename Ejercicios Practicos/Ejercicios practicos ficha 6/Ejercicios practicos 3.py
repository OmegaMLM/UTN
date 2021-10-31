'''
Promedio de números aleatorios
'''

import random

# Carga de datos
contador = 0
numt = 0

# Proceso
while contador != 1000:
    num = random.randint(0, 100000)
    numt += num
    contador += 1
promedio = numt / 1000

# Salida en pantalla
print('Promedio:', promedio)
