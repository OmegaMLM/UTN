'''
Tarjeta de Bingo
'''

# Carga de datos

import random

n1 = int(input('Introduzca el primer numero: '))
n2 = int(input('Introduzca el segundo numero: '))
n3 = int(input('Introduzca el tercer numero: '))
numeros = n1, n2, n3

# Proceso y salida en pantalla
random1 = random.randint(1, 100)
random2 = random.randint(1, 100)
random3 = random.randint(1, 100)
random4 = random.randint(1, 100)
random5 = random.randint(1, 100)
random6 = random.randint(1, 100)
random7 = random.randint(1, 100)
random8 = random.randint(1, 100)
random9 = random.randint(1, 100)
random10 = random.randint(1, 100)
random11 = random.randint(1, 100)
random12 = random.randint(1, 100)
random13 = random.randint(1, 100)
random14 = random.randint(1, 100)
random15 = random.randint(1, 100)

if random1 or random2 or random3 or random4 or random5 or random6 or random7 or random8 or random9 or random10 or random11 or random12 or random13 or random14 or random15 in numeros:
    print('El jugador tiene mala suerte, no marcó ninguna casilla')
else:
    print('El jugador marcó algún numero de la tarjeta')
