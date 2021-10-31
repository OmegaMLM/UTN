'''
Menores y promedio
'''
import random

# Carga de datos
anterior = 100001
contador = 0
tmen = 0
contadormen = 0
men = 0
# Proceso
while contador != 5000:
    num = random.randint(0, 100000)
    contador += 1
    print(num)
    if anterior > num:
        men = num
        anterior = men
        tmen += men
        contadormen += 1
    else:
        anterior = men

# Salida en pantalla
print('Numero menor:', men)
promedio = tmen / contadormen
print('Promedio:', promedio)
