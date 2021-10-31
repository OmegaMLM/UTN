def principal():
    # Init
    cpal = clp = cl = cc = 0

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


        else:
            # Al finalizar la palabra
            if clp == 0:
                continue
            cpal += 1

            # Reset
            clp = 0

    # Salida en pantalla
    print("Cantidad de letras:", cl)
    print("Cantidad de palabras:", cpal)
    print("Cantidad caracteres:", cc)


if __name__ == "__main__":
    principal()
