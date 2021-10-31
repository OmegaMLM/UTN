'''
Triangulo Rectángulo
'''
import math

# Carga de datos
c1 = float(input('Introduzca el valor del primer cateto: '))
c2 = float(input('Introduzca el valor del segundo cateto: '))

# Proceso
hipotenusa = math.sqrt((c1 ** 2) + (c2 ** 2))
mayor = max(c1, c2)
menor = min(c1, c2)

# Salida en pantalla
print('El valor de la hipotenusa es de:', hipotenusa, '\nEl lado de mayor es:', mayor, '\nEl lado menor es:', menor)
