'''
Temperatura diaria
'''
# Carga de datos
t1 = float(input('Introduzca la primera temperatura: '))
t2 = float(input('Introduzca la segunda temperatura: '))
t3 = float(input('Introduzca la tercera temperatura: '))

# Proceso y salida a pantalla
prom = (t1 + t2 + t3) / 3
if t1 > prom or t2 > prom or t3 > prom:
    print('Una de las temperaturas es mayor a la promedio.')
else:
    print('Ninguna de las temperaturas es mayor a la promedio.')
