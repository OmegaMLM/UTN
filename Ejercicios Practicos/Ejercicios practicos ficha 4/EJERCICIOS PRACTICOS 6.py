'''
Analisis de palabra
'''

# Carga de datos \
palabra = input('Ingrese la palabra: ')

# Proceso y salida en pantalla
cantidad = len(palabra) - 1
print(palabra[cantidad])
if palabra[3] == 'a' or palabra[3] == 'e' or palabra[3] == 'i' or palabra[3] == 'o' or palabra[3] == 'u':
    print('La palabra termina en vocal.')
else:
    print('La palabra no termina en vocal.')
