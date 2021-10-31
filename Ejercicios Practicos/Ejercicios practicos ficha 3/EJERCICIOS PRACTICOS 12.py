'''
Calculo de posta de natación
'''

# Carga de datos
espalda = 0, 52, 15
pecho = 1, 2, 75
mariposa = 0, 59, 80
libre = 0, 48, 15

# Proceso
minutos = espalda[0] + pecho[0] + mariposa[0] + libre[0]
segundos = espalda[1] + pecho[1] + mariposa[1] + libre[1]
centesimas = espalda[2] + pecho[2] + mariposa[2] + libre[2]
minutosf = minutos + segundos // 60
centesimasf = centesimas % 100
segundosf = segundos % 60 + centesimas // 100

# Salida en pantalla
print('El tiempo total de carrera fue de: ', '\nMinutos:', minutosf, '\nSegundos:', segundosf,
      '\nCentésimas:', centesimasf)
