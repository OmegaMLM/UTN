def porcentaje(numero1, numero2):
    if numero2 != 0:
        numero = (numero1 * 100) / numero2
        return numero
    else:
        return None


def letras_final(car, cadena, cl, letrafinal, letracomienzo):
    if car == letrafinal and cadena[cl - 2] == letracomienzo and (cadena[cl] == " " or cadena[cl] == "."):
        return True


def letras_sucesivas(car, cadena, cl, letrafinal, letracomienzo):
    if car == letrafinal and cadena[cl - 2] == letracomienzo:
        return True


def es_vocal(car):
    return car in "aeiouàèìòùäëïöü"


def posicion(booleano, posicion, clp):
    if booleano and posicion <= clp / 2:
        return True


def principal():
    # init
    cl = cpal = clp = cnp = pcv = pon = posde = pde = 0
    np = cv = sion = side = False
    # Lectura cadena de texto
    cadena = input("Ingrese la cadena de texto (finalizar con un punto): ")
    cadena = cadena.lower()

    # Bucle for
    for car in cadena:

        if car != " " and car != ".":
            # Dentro de la palabra
            cl += 1
            clp += 1

            # Porcentaje de palabras que tuvieron un digito
            if car in "123456789":
                np = True

            # Vocales y consonantes alternadas
            if es_vocal(car) and (cadena[cl - 2] in "bcdfghjklmnñpqrstvxzwy" or cadena[cl] in "bcdfghjklmnñpqrstvxzwy"):
                cv = True

            # Palabras que terminaron en ON
            if letras_final(car, cadena, cl, "n", "o"):
                sion = True

            # Palabras con DE en la primera mitad de la palabra
            if letras_sucesivas(car, cadena, cl, "e", "d"):
                side = True
                posde = clp
                cpal += 1
        else:
            # Al finalizar la palabra
            if clp == 0:
                continue

            # Porcentaje de numeros
            if np:
                cnp += 1

            # Consonante y vocales
            if cv:
                pcv += 1

            # Palabra que termina con ON
            if sion:
                pon += 1

            # Posicion DE
            if posicion(side, posde, clp):
                pde += 1

            # Reinicio
            clp = 0
            np = False
            cv = False
            sion = False
            side = False

    # Salida en pantalla
    print("Cantidad de letras:", cl)
    print("Cantidad de palabras:", cpal)
    print("Porcentaje de palabras con numeros:", porcentaje(cnp, cpal), "%")
    print("Cantidad de palabras con vocales y consonantes alternadas:", pcv)
    print("Porcentaje palabras que terminan con on:", porcentaje(pon, cpal), "%")
    print("Cantidad de palabras que incluyen de en la primera mitad:", pde)


# Start
if __name__ == "__main__":
    principal()
