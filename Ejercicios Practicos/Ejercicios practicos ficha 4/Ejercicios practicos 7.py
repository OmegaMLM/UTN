'''
Tirada de moneda
'''
import random

# Carga de datos
eleccion = input('Elige Cara o Cruz: ')

# Proceso y salida en pantalla
moneda = 'Cara', 'Cruz'
lado = random.choice(moneda)
if  eleccion == lado:
    print('Acertaste.')
else:
    print('No acertaste')

