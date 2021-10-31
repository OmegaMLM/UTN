'''
Búsqueda de mayor
'''
import random

may = 0
contador = 0
anterior = 0
while contador != 10000:
    num = random.randint(0, 100000)
    print(num)
    contador += 1
    if anterior < num:
        may = num
        anterior = may
    else:
        may = anterior
print('Numero mayor:', may)
