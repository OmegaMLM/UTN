'''
Puntos en un plano
'''

# Carga de datos
puntos = int(input('Ingrese la cantidad de coordenadas: '))
cuadrante1y3 = mayordistancia = 0

for i in range(puntos):
    puntox = float(input('Ingrese el punto del eje x: '))
    puntoy = float(input('Ingrese el punto del eje y: '))
    if puntox >= 0 and puntoy >= 0:
        print('Se encuentra en el primer cuadrante.')
        cuadrante1y3 += 1
    elif puntox <= 0 and puntoy >= 0:
        print('Se encuentra en el segundo cuadrante.')
    elif puntox <= 0 and puntoy <= 0:
        print('Se encuentra en el tercer cuadrante.')
        cuadrante1y3 += 1
    elif puntox >= 0 and puntoy <= 0:
        print('Se encuentra en el cuarto cuadrante.')
    if puntox > mayordistancia:
        mayordistancia = puntox
    elif puntoy > mayordistancia:
        mayordistancia = puntoy
print('Cantidad de puntos en el primer y tercer cuadrante es:', cuadrante1y3)
print('Punto mas alejado del origen:', mayordistancia)
