def es_numero(letraciclo):
    return letraciclo in "0123456789"


def es_vocal(letraciclo):
    return letraciclo in "aeiouàèìòùäëïöü"


def es_consonante(letraciclo):
    return letraciclo in "bcdfghjklmnñpqrstvxzwy"


def porcentaje(numero1, numero2):
    if numero2 != 0:
        numero = (numero1 * 100) / numero2
        return numero
    else:
        return None


def posicion(booleano, posicion, cantidadletraspalabras):
    if booleano and posicion <= cantidadletraspalabras / 2:
        return True


def letras_final(letraciclo, cadena, cantidadletras, letrafinal, letracomienzo):
    if letraciclo == letrafinal and cadena[cantidadletras - 2] == letracomienzo and (
            cadena[cantidadletras] == " " or cadena[cantidadletras] == "."):
        return True


def promedio(numero1, numero2):
    if numero2 != 0:
        numero = numero1 / numero2
        return numero
    else:
        return "Sin posible calculo"


def principal():
    # Init
    cpal = clp = cl = crnum = cvocalconsonante = cc = cigualultimaletra = posiciona = cposiciona = condicionaldepalabras = 0
    sinumero = sir = sivocal = siconsonante = igualultimaletra = sia = aencontrada = sier = False
    ultimaletra = None

    # Lectura de texto
    cadena = input("Ingrese el texto a procesar (finalizar con un punto): ")
    cadena = cadena.lower()

    # Bucle for
    for car in cadena:
        cc += 1
        if car != " " and car != ".":
            # Dentro de la palabra
            clp += 1
            cl += 1
            # Búsqueda de letra R y numero
            if es_numero(car):
                sinumero = True
            if car == "r":
                sir = True

            # Búsqueda de palabra comienza con vocal y termina en consonante
            if clp == 1 and es_vocal(car):
                sivocal = True
            if es_consonante(car) and (cadena[cc] == " " or cadena[cc] == "."):
                siconsonante = True
            # Búsqueda palabra que comienza con la letra de la anterior
            if cadena[cc] == " " or cadena[cc] == ".":
                ultimaletra = car
            if car == ultimaletra and clp == 1:
                igualultimaletra = True

            # Primera mitad A termina en ER
            if car == "a" and aencontrada == False:
                sia = True
                posiciona = clp
                aencontrada = True
            if letras_final(car, cadena, cc, "r", "e"):
                sier = True



        else:
            # Al finalizar la palabra
            if clp == 0:
                continue
            cpal += 1
            # Bandera letra R y numero
            if sinumero and sir:
                crnum += 1

            # Bandera vocal y consonante
            if sivocal and siconsonante:
                cvocalconsonante += 1

            # Bandera palabra que comienza con la ultima
            if igualultimaletra:
                cigualultimaletra += 1

            # Posicion y siER
            if posicion(sia, posiciona, clp) and sier:
                cposiciona += 3
                condicionaldepalabras += clp
            # Reset
            clp = 0
            sinumero = False
            sir = False
            sivocal = False
            siconsonante = False
            igualultimaletra = False
            aencontrada = False
            sier = False
    # Salida en pantalla
    print("Cantidad de letras:", cl)
    print("Cantidad de palabras:", cpal)
    print("Cantidad de palabras con R y numero:", crnum)
    print("Porcentaje de palabras que comenzaron con vocal y finalizaron con consonante:",
          porcentaje(cvocalconsonante, cpal), "%")
    print("Cantidad de palabras que comienzan con la ultima letra:", cigualultimaletra)
    print("Promedio de palabras con A en la primera mitad y ER al final:", promedio(cposiciona, condicionaldepalabras))


if __name__ == "__main__":
    principal()
