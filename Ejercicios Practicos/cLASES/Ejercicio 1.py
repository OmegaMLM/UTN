'''
Programa para calcular las frigorías de una habitación.
'''
ancho = float(input('Introduzca el ancho: '))
largo = float(input('Introduzca el largo: '))
area = ancho * largo
alto = float(input('Introduzca el alto: '))
volumen = area * alto
frig = volumen * 40
print('El total de frigorías es de:', frig)
