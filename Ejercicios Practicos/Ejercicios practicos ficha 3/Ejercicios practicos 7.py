'''
Calculo Presupuestario
'''

# Carga de datos
presupuesto = int(input('Introduzca el presupuesto total: '))

# Proceso
urgencias = presupuesto * 37 / 100
pediatria = presupuesto * 42 / 100
traumatologia = presupuesto * 21 / 100

# Salida en pantalla
print('Presupuesto para Urgencias:', urgencias, '\nPresupuesto para Pediatría:', pediatria,
      '\nPresupuesto para Traumatología:', traumatologia)
