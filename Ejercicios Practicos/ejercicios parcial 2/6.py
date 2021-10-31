def es_consonante(letraciclo):
    return letraciclo in "bcdfghjklmnñpqrstvxzwy"


def letras_sucesivas(letraciclo, cadena, cantidadletras, letracomienzo, letrafinal):
    if letraciclo == letrafinal and cadena[cantidadletras - 2] == letracomienzo:
        return True


def promedio(numero1, numero2):
    if numero2 != 0:
        numero = numero1 / numero2
        return numero
    else:
        return "Sin posible calculo"


def principal():
    # Init
    cpal = clp = cl = cc = consonantes = posicionmin = llpar = 0
    side = cplde = sill = False
    palabramin = None

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

            # Cantidad de consonantes
            if es_consonante(car):
                consonantes += 1

            # Palabras que incluyeron DE
            if letras_sucesivas(car, cadena, cc, "d", "e"):
                side = True

            # Palabras con LL
            if letras_sucesivas(car, cadena, cc, "l", "l"):
                sill = True

        else:
            # Al finalizar la palabra
            if clp == 0:
                continue
            cpal += 1

            # Bandera DE
            if side:
                cplde += 1

            # Busqueda palabra mas corta
            if cpal == 1:
                palabramin = clp
                posicionmin = cpal

            elif clp < palabramin:
                palabramin = clp
                posicionmin = cpal

            # Busqueda y paridad LL
            if sill and clp % 2 == 0:
                llpar += 1
            # Reset
            clp = 0
            side = False
            sill = False

    # Salida en pantalla
    print("Cantidad de letras:", cl)
    print("Cantidad de palabras:", cpal)
    print("Cantidad caracteres:", cc)
    print("Promedio de consonantes:", promedio(consonantes, cpal))
    print("Cantidad de palabras con DE:", cplde)
    print("Posicion palabra mas corta:", posicionmin)
    print("Cantidad de palabras con LL y cantidad de letras par:", llpar)


if __name__ == "__main__":
    principal()
