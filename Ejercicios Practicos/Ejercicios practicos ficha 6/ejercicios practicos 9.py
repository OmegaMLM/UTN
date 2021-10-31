'''
Comisión de Vendedores
'''

# Carga de datos
category = int(input('Ingrese su categoría: '))
venta = int(input('Ingrese el total de la venta: '))

# Proceso
while category != 0:
    if category == 1:
        comision1 = (venta * 10) / 100
    if category == 2:
        comision2 = (venta * 25) / 100
    if category == 3:
        comision3 = (venta * 30) / 100
    if category == 4:
        comision4 = (venta * 40) / 100
    category = int(input('Ingrese su categoría: '))
    venta = int(input('Ingrese el total de la venta: '))

# Salida en pantalla
print()
print('Comisiones totales de la categoría 1:', comision1)
print('Comisiones totales de la categoría 2:', comision2)
print('Comisiones totales de la categoría 3:', comision3)
print('Comisiones totales de la categoría 4:', comision4)
