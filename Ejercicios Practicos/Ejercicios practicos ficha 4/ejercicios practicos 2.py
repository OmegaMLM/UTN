'''
Suma-Division-Potencia
'''

# Carga de datos
n1 = float(input('Introduzca el primer numero: '))
n2 = float(input('Introduzca el segundo numero: '))
n3 = float(input('Introduzca el tercer numero: '))

# Proceso y salida en pantalla
suma = n1 + n2 + n3
if suma > 10:
    print('El resultado es:', suma // 2)
else:
    print('El resultado es:', suma ** 3)
