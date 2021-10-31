'''
Edad mínima
'''
# Carga de datos
edadminima = int(input('Ingrese la edad minima: '))
edad1 = int(input('Ingrese la edad del primer participante: '))
edad2 = int(input('Ingrese la edad del segundo participante: '))
edad3 = int(input('Ingrese la edad del tercer participante: '))

# Proceso y salida en pantalla
if edad1 >= edadminima and edad2 >= edadminima and edad3 >= edadminima:
    print('Los participantes pueden ingresar.')
else:
    print('Los participantes no pueden ingresar.')
