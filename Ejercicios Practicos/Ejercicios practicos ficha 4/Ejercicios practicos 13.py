'''
Calculo de Precios con Descuento
'''

# Carga de datos
preciounitario = float(input('Ingrese el precio del producto: '))
cantidad = int(input('Ingrese la cantidad vendida: '))
efectivo = int(input('Ingrese - 1: Si se pago en efectivo - \n - 2:Si no se pago en efectivo - : '))

# Proceso y salida en pantalla
preciofinalsindescuento = preciounitario * cantidad

if efectivo == 1 and cantidad > 10:
    descuento = preciounitario * 0.2
    preciofinal = (preciounitario - descuento) * cantidad
    print('El precio final es de:', preciofinal)
else:
    descuento = preciounitario * 0.05
    preciofinal = (preciounitario - descuento) * cantidad
    print('El precio final es de:', preciofinal)

# Salida en pantalla
print('El precio final sin descuento es de:', preciofinalsindescuento)
