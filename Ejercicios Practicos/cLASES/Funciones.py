# Deteccion consonante
def es_consonante(letraciclo):
    return letraciclo in "bcdfghjklmnñpqrstvxzwy"


# Deteccion de vocal
def es_vocal(letraciclo):
    return letraciclo in "aeiouàèìòùäëïöü"


# Deteccion de numero
def es_numero(letraciclo):
    return letraciclo in "0123456789"


# Búsqueda de letras sucesivas
def letras_sucesivas(letraciclo, cadena, cantidadletras, letracomienzo, letrafinal):
    if letraciclo == letrafinal and cadena[cantidadletras - 2] == letracomienzo:
        return True


# Búsqueda de letras del comienzo (2 letras)
def letras_comienzo(letraciclo, cantidadletraspalabras, cadena, cantidadletras, letrafinal, letracomienzo):
    if letraciclo == letrafinal and cantidadletraspalabras == 2 and cadena[cantidadletras - 2] == letracomienzo:
        return True


# Busqueda de letras al final (2 letras)
def letras_final(letraciclo, cadena, cantidadletras, letrafinal, letracomienzo):
    if letraciclo == letrafinal and cadena[cantidadletras - 2] == letracomienzo and (
            cadena[cantidadletras] == " " or cadena[cantidadletras] == "."):
        return True


# Confirmar posicion primera mitad
def posicion(booleano, posicion, cantidadletraspalabras):
    if booleano and posicion <= cantidadletraspalabras / 2:
        return True


# Busqueda palabra mas corta
def palabramascorta(cantidadpalabras, cantidadletraspalabras, palabrasmin):
    if cantidadpalabras == 1:
        palabramin = cantidadletraspalabras
        posicionmin = cantidadpalabras

    elif cantidadletraspalabras < palabrasmin:
        palabramin = cantidadletraspalabras
        posicionmin = cantidadpalabras


# Base análisis de texto
def principal():
    # Init
    cpal = clp = cl = 0

    # Lectura de texto
    cadena = input("Ingrese el texto a procesar (finalizar con un punto): ")
    cadena = cadena.lower()

    # Bucle for
    for car in cadena:
        if car != " " and car != ".":
            # Dentro de la palabra
            clp += 1
            cl += 1

        else:
            # Al finalizar la palabra
            if clp == 0:
                continue
            cpal += 1
            clp = 0

    # Salida en pantalla
    print("Cantidad de letras:", cl)
    print("Cantidad de palabras:", cpal)


# Porcentaje
def porcentaje(numero1, numero2):
    if numero2 != 0:
        numero = (numero1 * 100) / numero2
        return numero
    else:
        return "Sin posible calculo"


# Promedio
def promedio(numero1, numero2):
    if numero2 != 0:
        numero = numero1 / numero2
        return numero
    else:
        return "Sin posible calculo"


# Menu de Opciones
op = 0
while op != 4:
    print('1. Texto')
    print('2. Texto')
    print('3. Texto')
    print('4. Texto')
    op = validacion():
    if op == 1:
        opcion1(self)
    elif op == 2:
        opcion2(self)
    elif op == 3:
        opcion3(self)


# Array Conteo
def contador(self, array):
    contadorarry = [0] * 12
    for i in range(len(self)):
        d = self[i].nivel
        contadorarry[d] += 1
    for j in range(len(contadorarry)):
        if contadorarry[j] != 0:
            print("Genero: ", array[j], "\t Cantidad: ", contadorarry[j])


def validacion(num1, num2):
    numero = int(input('Ingrese un numero de las opciones: '))
    while numero < num1 or numero > num2:
        numero = int(input('Error -- Ingrese un numero de las opciones: '))
    return numero