'''
Ventas por sucursal
'''

# Carga de datos
tv = 0
cv1 = 0
cv2 = 0
cv3 = 0
cv = int(input('Ingrese la cantidad de ventas: '))

# Salida en pantalla de cantidad de ventas
print('Usted ingreso: ', cv)

# Proceso
while cv > 0:
    if 100 <= cv <= 300:
        cv1 += cv
        tv += cv
    elif cv == 400 or cv == 500 or cv == 600:
        cv2 += cv
        tv += cv
    elif cv < 50:
        cv3 += cv
        tv += cv
    else:
        tv += cv
    cv = int(input('Ingrese la cantidad de ventas: '))
    print('Usted ingreso:', cv)

# Salida en pantalla
print()
print('Total de ventas:', tv)
print('Total de ventas entre 100 y 300 unidades:', cv1)
print('Total de ventas con 400, 500 y 600 unidades:', cv2)
print('Total de ventas inferiores a 50 unidades:', cv3)
