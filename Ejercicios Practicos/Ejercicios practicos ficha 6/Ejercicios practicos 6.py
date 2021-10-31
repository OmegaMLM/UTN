'''
Números pares e impares
'''

# Carga de datos
suma = 0
num = float(input('Ingrese un numero: '))
numpares = 0
numerosimpares = 0
verdad = 'No'
# Proceso
while num >= 0:
    resto = num % 2
    if 50 <= num <= 100:
        suma += num
    if resto == 0:
        numpares += 1
    else:
        numerosimpares += 1
    if num == 0:
        verdad = 'Si'
    else:
        verdad = 'No'
    num = float(input('Ingrese un numero:'))
print()
print('Suma entre los numeros 50 y 100:', suma)
print('Cantidad de valores pares ingresados:', numpares)
print('Cantidad de valores impares ingresados:', numerosimpares)
print(verdad, 'hay 0 cargados.')
