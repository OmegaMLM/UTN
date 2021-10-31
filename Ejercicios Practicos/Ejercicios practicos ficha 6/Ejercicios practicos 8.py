'''
Mayor numero en orden par
'''
anterior = 0
may = 0
# Carga de datos
num = int(input('Ingrese un numero: '))

# Proceso
while num != 0:
    if (num % 2) == 0:
        if anterior <= num:
            may = num
            anterior = num
        else:
            anterior = may
    num = int(input('Ingrese un numero: '))

# Salida en pantalla
print('El mayor de los numeros pares es:', may)
