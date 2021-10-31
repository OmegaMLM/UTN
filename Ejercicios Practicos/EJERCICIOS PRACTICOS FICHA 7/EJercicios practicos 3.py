'''
Sueldos y aguinaldo
'''

# Carga de datos
sma = aguinaldo = sp = sueldo = sueldot = 0
smb = 100000000 ** 20
mes = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio')

# Proceso
for i in mes:
    sueldo = int(input('Ingrese su sueldo: '))
    sueldot += sueldo
    if sueldo > sma:
        sma = sueldo
    elif sueldo < smb:
        smb = sueldo

# Salida en pantalla
print('El aguinaldo es:', sma / 2)
print('El sueldo mas bajo es:', smb)
print('El sueldo promedio es de:', sueldot / 6)
