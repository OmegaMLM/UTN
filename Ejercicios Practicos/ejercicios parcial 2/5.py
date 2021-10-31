def letras_sucesivas(letraciclo, cadena, cantidadletras, letrafinal, letracomienzo):
    if letraciclo == letrafinal and cadena[cantidadletras - 2] == letracomienzo:
        return True


def porcentaje(numero1, numero2):
    if numero2 != 0:
        numero = (numero1 * 100) / numero2
        return numero
    else:
        return "Sin posible calculo"


def principal():
    # Init
    cpal = clp = cl = cc = cplmay3 = psino = cen = cpen = cpultima = 0
    plmay3 = sisi = sino = ultima = False
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
            # Cantidad de palabras con mas de 3 caracteres
            if clp > 3:
                plmay3 = True

            # Palabras que tienen SI y NO
            if letras_sucesivas(car, cadena, cc, "i", "s"):
                sisi = True
            if letras_sucesivas(car, cadena, cc, "o", "n"):
                sino = True

            # Palabras con EN 2 veces
            if letras_sucesivas(car, cadena, cc, "n", "e"):
                cen += 1

            # Cantidad de palabras que comienzan con la letra anterior
            if cadena[cc] == "." or cadena[cc] == " ":
                ultimaletra = car
            if clp == 1 and ultimaletra == car:
                ultima = True

        else:
            # Al finalizar la palabra
            if clp == 0:
                continue
            cpal += 1

            # Palabras con mas de 3 caracteres
            if plmay3:
                cplmay3 += 1

            # Palabras con SI y NO
            if sisi and sino:
                psino += 1

            # Palabras con EN 2 veces
            if cen == 2:
                cpen += 1

            # Cantidad de palabras que comienzan con la letra anterior
            if ultima:
                cpultima += 1
            # Reset
            clp = 0
            plmay3 = False
            sisi = False
            sino = False
            ultima = False
            cen = 0

    # Salida en pantalla
    print("Cantidad de letras:", cl)
    print("Cantidad de palabras:", cpal)
    print("Cantidad caracteres:", cc)
    print("Cantidad de palabras con mas de 3 letras:", cplmay3)
    print("Porcentaje de palabras con SI y NO:", round(porcentaje(psino, cpal), 2))
    print("Cantidad de palabras con EN:", cpen)
    print("Cantidad de palabras que empiezan con la letra anterior:", cpultima)


if __name__ == "__main__":
    principal()
