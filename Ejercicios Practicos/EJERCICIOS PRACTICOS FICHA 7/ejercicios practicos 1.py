'''
Ciclistas
'''

# Carga de datos
competidores = int(input('Ingrese la cantidad de competidores: '))
tiempo_record = int(input('Ingrese el tiempo record en segundos: '))
ganador = 0
tiempototal = 0
nombreganador = None

# Proceso
for cantidad in range(competidores):
    nombre = input('Ingrese el nombre del competidor: ')
    tiempo = int(input('Ingrese el tiempo del competidor en segundos: '))
    if tiempo > ganador:
        ganador = tiempo
        nombreganador = nombre
    tiempototal += tiempo
    if tiempo > tiempo_record:
        print('Se logro un nuevo tiempo record.')
        tiempo_record = tiempo

# Salida en pantalla
print('El ganador es:', nombreganador, '\nCon un tiempo de:', ganador)
print('El promedio es de:', tiempototal / competidores)
