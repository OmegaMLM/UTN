def porcentaje(numero1, numero2):
    if numero2 != 0:
        numero = (numero1 * 100) / numero2
        return numero


def principal():
    # Init
    cpal = clp = cl = cc = cpl = cvocp = cu2v = 0
    up = False
    ulp = None

    # Lectura de texto
    cadena = input("Ingrese el texto a procesar (finalizar con un punto): ")
    cadena = cadena.lower()

    # Bucle for
    for car in cadena:
        if car != " " and car != ".":
            # Dentro de la palabra
            clp += 1
            cl += 1

            # Cantidad de consonantes
            if car in "bcdfghjklmnñpqrstvxzwy":
                cc += 1
            if cl == 1:
                pl = car
            elif pl == car and cl != 1 and clp == 1:
                cpl += 1

            # Comienzan con la ultima palabra del primero y tienen 2 vocales.
            if cpal == 0 and (cadena[cl] == " " or cadena[cl] == "."):
                ulp = car
            if ulp == car and clp == 1:
                up = True
            if car in "aeiouàèìòùäëïöü":
                cvocp += 1
            if up and cvocp > 2:
                cu2v += 1
                up = False

        else:
            # Al finalizar la palabra
            if clp == 0:
                continue
            cpal += 1

            # Posicion de la palabra mas larga
            if cpal == 1:
                maslarga = clp
                pmaslarga = cpal
            elif cpal != 1 and clp > maslarga:
                maslarga = clp
                pmaslarga = cpal

            clp = 0

    # Salida en pantalla
    print("Cantidad de letras:", cl)
    print("Cantidad de palabras:", cpal)
    print("Porcentaje de letras consonantes:", round(porcentaje(cc, cl), 2), "%")
    print("Posicion palabra mas larga:", pmaslarga)
    print("Cantidad de letras que comienzan con la ultima letra y tienen mas de 2 vocales:"
          "", cu2v)



if __name__ == "__main__":
    principal()
