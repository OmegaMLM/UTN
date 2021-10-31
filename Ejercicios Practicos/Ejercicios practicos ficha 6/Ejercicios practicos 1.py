'''
Complejo de cines
'''
# Carga de datos
ce = int(input('Cantidad de espectadores: '))
desc = float(input('Descuento: '))
ct = 0
cfsd = 0
ctf = 0
dinero = 0
# Proceso
while ce != 0:
    if desc == 0:
        cfsd += 1
        ctf += 1
        dinero = ce * 75

    else:
        ctf += 1
        dinero = ce * (50 - (50 * desc // 100))
    ct += dinero
    ce = int(input('Cantidad de espectadores: '))
    desc = float(input('Descuento: '))
pcfsd = (cfsd / ctf) * 100

# Salida en pantalla
print('Cantidad de dinero recaudado:', ct)
print('Cantidad de funciones sin descuento:', cfsd)
print('Porcentaje de funciones sin descuento:', str(pcfsd) + '%')
