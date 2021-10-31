'''
Ejercicio Estadística de Guardería Náutica
'''

# Carga de datos
tvel = tlancha = tmonto = 0
mayormonto = 0
mayormontononbre = None
promedio = porcentajevel = porcentajelanchas = 0
cantidad = int(input('Ingrese la cantidad de barcos: '))
for i in range(cantidad):
    nombre = input('Ingrese el nombre del barco: ')
    tipo = int(input('Ingrese el tipo de barco, (1 para velero, 2 para lancha): '))
    monto = int(input('Ingrese el monto por mes: '))
    if tipo == 1:
        tvel += monto
        tmonto += monto
    else:
        tlancha += monto
        tmonto += monto
    if tipo == 1 and monto > mayormonto:
        mayormonto = monto
        mayormontononbre = nombre
    promedio = tmonto / cantidad
    porcentajevel = (tvel / tmonto) * 100
    porcentajelanchas = (tlancha / tmonto) * 100
print('Total aportado por los veleros:', tvel, '\nTota aportado por las lanchas:', tlancha)
print('Nombre del velero que mas aporta:', mayormontononbre, '\tMonto:', mayormonto)
print('El promedio pagado es de:', promedio)
print('Porcentaje de los veleros:', str(porcentajevel) + '%', '\nPorcentaje de las lanchas:',
      str(porcentajelanchas) + '%')
