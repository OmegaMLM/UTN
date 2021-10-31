'''
Proceso de Discriminantes
'''

#Carga de datos y proceso
seguir = 's'
while seguir == 's' or seguir == 'S':
    print('Raíces de la ecuación de segundo grado...')
    a = float(input('a: '))
    b = float(input('b: '))
    c = float(input('c: '))
    x1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
    x2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
# Salida en pantalla
    print('x1:', x1)
    print('x2:', x2)
    seguir = input('Desea resolver otra ecuación? (s/n): ')
