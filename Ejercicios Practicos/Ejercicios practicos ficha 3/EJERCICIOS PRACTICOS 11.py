'''
Palabra Enmascarada
'''

# Carga de datos
palabra = input('Palabra a enmascarar: ')

# Proceso
primeraletra = palabra[0]
letras = len(palabra)
l2 = letras - 1
ultimaletra = palabra[l2]
l3 = letras - 2
cifrado = l3 * '*'

# Salida en pantalla
print(primeraletra + cifrado + ultimaletra)
