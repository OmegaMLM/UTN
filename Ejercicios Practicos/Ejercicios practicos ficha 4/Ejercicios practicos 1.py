'''
Generador de direccion de mail
'''

# Carga de datos
nombre = input('Introduzca su nombre: ')
apellido = input('Introduzca su apellido: ')
dominio = input('Introduzca un dominio: ')

# Proceso y salida en pantalla
if nombre[0] == apellido[0]:
    print(nombre[0] + apellido + '@' + dominio)
else:
    print(nombre + '.' + apellido + '@' + dominio)
