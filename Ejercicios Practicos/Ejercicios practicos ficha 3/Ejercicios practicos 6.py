'''
Calculo de sueldo
'''

# Carga de datos
nombre = input('Introduzca el Nombre y el Apellido: ')
area = input('Introduzca el Area Funcional: ')
salario = int(input('Introduzca el Salario Actual: '))

# Proceso
incremento = (salario * 0.8) * 0.25
salariofinal = salario + incremento

# Salida en pantalla
print('Nombre del empleado:', nombre, '\tNuevo Salario: $', salariofinal)
print('Area Funcional:', area)
print('Salario actual: $', salario)
