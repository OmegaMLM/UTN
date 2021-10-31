'''
Tiempos de Triatlón
'''

# Carga de datos
minyseg1 = input('Introduzca los minutos y segundos de la prueba de natación en un formato '
                 'de mm:ss : ')
minyseg2 = input('Introduzca los minutos y segundos de la prueba de ciclismo en un formato '
                 'de mm:ss : ')
minyseg3 = input('Introduzca los minutos y segundos de la prueba de pedestre en un formato '
                 'de mm:ss : ')

# Proceso
min1 = float(minyseg1[0:2])
seg1 = float(minyseg1[3:5])
min2 = float(minyseg2[0:2])
seg2 = float(minyseg2[3:5])
min3 = float(minyseg3[0:2])
seg3 = float(minyseg3[3:5])
segt1 = min1 * 60 + seg1
segt2 = min2 * 60 + seg2
segt3 = min3 * 60 + seg3
tts = segt1 + segt2 + segt3
hh = tts // 3600
mm = tts % 3600 // 60
ss = tts % 60
maximo = max(segt1, segt2, segt3)
minimo = min(segt1, segt2, segt3)
promedioi = (segt1 + segt2 + segt3) / 3
promediof = round(promedioi, 2)

# Salida en pantalla
print('Tiempo total de prueba: ', int(hh), ':', int(mm), ':', int(ss))
print('Tiempo maximo:', maximo, 'Segundos', '\tTiempo minimo:', minimo, 'Segundos')
print('Tiempo promedio:', promediof, 'Segundos')
