'''
Lanzamiento de dados
'''
import random

# Proceso y salida en pantalla
dado1 = 1, 2, 3, 4, 5, 6
dado2 = 1, 2, 3, 4, 5, 6
lado1 = random.choice(dado1)
lado2 = random.choice(dado2)
numeros = 2, 4, 6, 8, 10, 12
if lado1 == lado2 or lado1 + lado2 in numeros:
    print('Ganaste.')
else:

    print('Perdiste.')
