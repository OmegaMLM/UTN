"""
Menu de Opciones con secuencias
"""

# Estructura opciones
cuadrados = cl = vocales = pares = impares = 0

opc = 1
while opc != 4:
    print("Lista de opciones: \n1 - Suma de cuadrados de una serie de numeros."
          " \n2 - Determinar la cantidad de palabras de una vocal. \n3 - Determinar la mayor "
          "cantidad de valores pares o impares. \n4 - Salir.")
    opc = int(input("Ingrese una opción: "))
    if opc > 4 or opc <= 0:
        opc = print("Error - Ingrese una opción correcta:")
    # Opción 1
    if opc == 1:
        n = int(input("Ingrese hasta donde llega la serie: "))
        while n <= 0:
            n = int(input("Error - Ingrese un numero mayor a 0: "))
        for cuad in range(1, n + 1):
            cuadrados += (cuad ** 2)
        print("La suma de los cuadrados es:", cuadrados)
    # Opción 2
    elif opc == 2:
        texto = input("Ingrese una oración (finalizada con un punto): ")
        texto = texto.lower()
        while texto[0] == " ":
            texto = input("Error ingrese una palabra que no empiece con espacio: ")
        for text in texto:
            cl += 1
            if text == " " or text == ".":
                if texto[cl - 2] in "aeiouáéíóú":
                    vocales += 1
            if text == ".":
                break
        print("La cantidad de palabras que finalizan con vocales es:", vocales)
    # Opción 3
    elif opc == 3:
        numero = int(input("Ingrese un numero (con 0 finaliza): "))
        while numero != 0:
            if numero % 2 == 0:
                pares += 1
            else:
                impares += 1
            numero = int(input("Ingrese un numero (con 0 finaliza): "))
        if pares > impares:
            print("Los pares son mayores que los impares.")
        else:
            print("Los impares son mayor que los impares.")
