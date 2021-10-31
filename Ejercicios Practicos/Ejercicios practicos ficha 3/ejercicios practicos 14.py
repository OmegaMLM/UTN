'''
Sumador de Ángulos
'''

# Carga de Datos
v1 = (input('Ingrese el valor del primer ángulo en un formato de gg:mm:ss :'))
v2 = (input('Ingrese el valor del segundo ángulo en un formato de gg:mm:ss '))

# Procesos
g1 = float(v1[0:2])
m1 = float(v1[3:5])
s1 = float(v1[6:8])
g2 = float(v2[0:2])
m2 = float(v2[3:5])
s2 = float(v2[6:8])

gradosi = g1 + g2
minutosi = m1 + m2
segundosi = s1 + s2
segundosf = segundosi % 60
minutosf = minutosi % 60 + segundosi // 60
gradosf = gradosi + minutosi // 60

# Salida en pantalla
print('Grados :', gradosf, '\nMinutos:', minutosf, '\nSegundos:', segundosf)
