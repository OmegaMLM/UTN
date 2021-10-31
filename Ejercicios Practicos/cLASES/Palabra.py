'''
Análisis de palabra
'''
cantidad_letras = 0
cantidad_palabras = 0
cantidad_palabra_p = 0
cantidad_palabra_ta = 0
hay_palabra_ta = False
texto = input('Ingrese una cadena de caracteres: ')
for letra in texto:
    cantidad_letras += 1
    if letra == ' ' or letra == ".":
        cantidad_palabras += 1
        if hay_palabra_ta == True:
            cantidad_palabra_ta = + 1
            hay_palabras_ta = False
    elif letra == 'p' and (cantidad_letras == 1 or texto[cantidad_letras - 2] == ' '):
        cantidad_palabra_p += 1
    elif letra == 'a' and (cantidad_letras > 1 and texto[cantidad_letras - 2] == 't'):
        hay_palabra_ta = True
print('La cantidad de palabras es:', cantidad_palabras)
print('La cantidad de palabras que comienzan con p es:', cantidad_palabra_p)
print('Cantidad de palabras con ta:', cantidad_palabra_ta)
