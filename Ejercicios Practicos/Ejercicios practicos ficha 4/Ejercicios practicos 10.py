'''
Terreno
'''

# Carga de datos
frente = float(input('Ingrese las medidas del frente del terreno: '))
fondo = float(input('Ingrese las medidas del fondo del terreno: '))
# Proceso y salida en pantalla
if frente == fondo:
    print('El terreno es cuadrado.')
else:
    (print('El terreno es rectangular.'))
superficie = frente + fondo
# Salida en pantalla
print('La superficie es de:', superficie)