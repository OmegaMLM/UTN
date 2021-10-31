'''
Números: Mayor y Menor
'''

# Carga de datos
numero = int(input('Ingrese un numero(con un numero negativo termina): '))
menimpar = 10000000000000 ** 10000
maypar = 0

# Proceso
while numero >= 0:
    div = numero % 2
    if div == 0 and (numero > maypar):
        maypar = numero
    elif div != 0 and numero < menimpar:
        menimpar = numero
    numero = int(input('Ingrese un numero(con un numero negativo termina): '))
# Salida en pantalla
print('El mayor numero par es:', maypar)
print('El menor numero impar es:', menimpar)
