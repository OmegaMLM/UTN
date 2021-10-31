'''
Galería de arte
'''

# Carga por teclado
cuadro1 = int(input('Ingrese el año:'))
cuadro2 = int(input('Ingrese el año:'))
cuadro3 = int(input('Ingrese el año:'))
creacion = int(input('Ingrese un año:'))

# Proceso y salida por pantalla
if cuadro1 < 1901 and cuadro2 < 1901 and cuadro3 < 1901:
    print('Los cuadros son anteriores al siglo XX.')
else:
    print('Los cuadros no son anteriores al siglo XX.')

if creacion == cuadro1 or creacion == cuadro2 or creacion == cuadro3:
    print('Alguno de los cuadros fue creado en la fecha introducida.')
else:
    print('Ninguno de los cuadros fue creado en el año creado.')

if cuadro1 > cuadro2:
    may = cuadro1
elif cuadro2 > cuadro3:
    may = cuadro2
else:
    may = cuadro3

if cuadro1 < cuadro2:
    men = cuadro1
elif cuadro2 < cuadro3:
    men = cuadro2
else:
    men = cuadro3

print('La diferencia de años es de:', may - men)
