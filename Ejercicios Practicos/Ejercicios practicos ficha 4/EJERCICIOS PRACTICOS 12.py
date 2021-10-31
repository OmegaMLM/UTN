'''
Cartas de truco
'''

import random

# Proceso
c1 = random.randint(1, 12)
sec = 'Basto', 'Espada', 'Copa',
palo1 = random.choice(sec)
c2 = random.randint(1, 12)
palo2 = random.choice(sec)
c3 = random.randint(1, 12)
palo3 = random.choice(sec)
print(c1, palo1, c2, palo2, c3, palo3)
if c1 == 1 and palo1 == 'Espada' or c2 == 1 and palo2 == 'Espada' or c3 == 1 and palo3 == 'Espada':
    print('El as de espadas esta en tu mazo.')
else:
    print('El as de espada no esta en tu mazo.')

if palo1 == palo2 and palo2 == palo3:
    if c1 > c2:
        may1 = c1
    if  c2 > c3:
        may1 = c2
    if  c3:
        may1 = c3
    if c1 > c2:
        may2 = c1

