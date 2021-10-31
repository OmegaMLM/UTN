"""
1. Ejercicio Tipo Parcial (Resuelto 1K14)
"""
lt = p = j = 0
# Estructura Opciones
opc = 1
while opc != 3:
    print("Menu de opciones: \n1 - Indicar el ganador de 3 competidores. "
          "\n2 - Análisis de texto."
          "\n3 - Salir.")
    opc = int(input("Ingrese una opción: "))
    while opc < 1 or opc > 3:
        opc = int(input("Error - Ingrese una opción valida: "))
    # Opción 1
    if opc == 1:
        atleta1 = int(input("Ingrese el tiempo (en segundos) del primer atleta: "))
        atleta2 = int(input("Ingrese el tiempo (en segundos) del segundo atleta: "))
        atleta3 = int(input("Ingrese el tiempo (en segundos) del tercer atleta: "))
        if atleta1 <= atleta2 and atleta1 <= atleta3:
            print("El ganador es el primer atleta")
        elif atleta2 <= atleta1 and atleta2 <= atleta3:
            print("El ganador es el segundo atleta")
        elif atleta3 <= atleta1 and atleta3 <= atleta2:
            print("El ganador es el tercer atleta")
        if atleta1 < 850:
            print("El primer atleta batió el record")
        elif atleta2 < 850:
            print("El segundo atleta batió el record")
        elif atleta3 < 850:
            print("El tercer atleta batió el record")
    # Opción 2
    if opc == 2:
        texto = input("Ingrese un texto (finalizado con un punto): ")
        texto = texto.lower()
        for text in texto:
            if text != ".":
                lt += 1
            if text == ".":
                break
            elif text == "p":
                p += 1
            elif text == "j":
                j += 1
        print("El porcentaje de p's en el texto es de:", "%" + str(round(p * 100 / lt, 2)))
        print("El porcentaje de j's en el texto es de:",  "%" + str(round(j * 100 / lt, 2)))