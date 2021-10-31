def letras_sucesivas(car, cadena, cl, letra1, letra2):
    if car == letra1 and cadena[cl - 2] == letra2:
        return True


def letras_comienzo(car, clp, cadena, cl, letra1, letra2):
    if car == letra1 and clp == 2 and cadena[cl - 2] == letra2:
        return True


def principal():
    # Inicializaciones
    cpal = clp = cl = cvoc = cprr = cpla = cpulo = 0
    rrsi = lasi = banderau = ulo = False
    # Lectura de texto
    cadena = input("Ingrese el texto a analizar (finalizar con un punto): ")
    cadena = cadena.lower()

    # Bucle
    for car in cadena:
        # Dentro de la palabra
        if car != " " and car != ".":
            clp += 1
            cl += 1
            # Cantidad de palabras con rr
            if letras_sucesivas(car, cadena, cl, "r", "r"):
                rrsi = True

            # Cantidad de palabras que comienzan con la
            if letras_comienzo(car, clp, cadena, cl, "a", "l"):
                lasi = True

            # Cantidad de palabras con u y que finalizador con lo
            if car == "u" and banderau == False:
                banderau = True
            elif car == "o" and banderau and cadena[cl - 2] == "l" and (cadena[cl] == "." or cadena[cl] == " "):
                ulo = True
                banderau = False
        # Al finalizar palabra
        else:
            if clp == 0:
                continue
            cpal += 1
            # Bandera rr
            if rrsi:
                cprr += 1
            rrsi = False

            # Bandera la
            if lasi:
                cpla += 1
            lasi = False

            # Bandera ulo
            if ulo:
                cpulo += 1
            ulo = False
            clp = 0
            cl += 1
    # Salida en pantalla
    print("Cantidad de letras:", cl)
    print("Cantidad de palabras del texto:", cpal)
    print("Cantidad de palabras con rr:", cprr)
    print("Cantidad de palabras que comienzan con la:", cpla)
    print("Cantidad de palabras con ulo:", cpulo)


if __name__ == "__main__":
    principal()
