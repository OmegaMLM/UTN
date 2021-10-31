"""
Ejercicio Preparación
"""
# Contadores, Acumuladores
cl = cv = 0
# Estructura Opciones
opc = 1
while opc != 3:
    print("Menu de Opciones:"
          "\n1 - Análisis de temperaturas."
          "\n2 - Análisis de texto."
          "\n3 - Salir.")
    opc = int(input("Ingrese una opción: "))
    while opc < 1 or opc > 3:
        opc = int(input("Ingrese una opción valida: "))
    # Opción 1
    if opc == 1:
        temp1 = int(input("Ingrese la primera temperatura: "))
        temp2 = int(input("Ingrese la segunda temperatura: "))
        temp3 = int(input("Ingrese la tercera temperatura: "))
        # Temperatura mayor
        if temp1 > temp2 and temp1 > temp3:
            tempmayor = temp1
        elif temp2 > temp1 and temp2 > temp3:
            tempmayor = temp2
        elif temp3 > temp1 and temp3 > temp2:
            tempmayor = temp3
        # Temperatura menor
        if temp1 < temp2 and temp1 < temp3:
            tempmenor = temp1
        elif temp2 < temp1 and temp2 < temp3:
            tempmenor = temp2
        elif temp3 < temp1 and temp3 < temp2:
            tempmenor = temp3
        print("Mayor temperatura:", tempmayor, "Grados",
              "\nMenor temperatura:", tempmenor, "Grados")
        print("Diferencia entre maxima y minima:", tempmayor - tempmenor)
        print("Promedio de temperaturas:", (temp1 + temp2 + temp3) / 3)
    # Opción 2
    if opc == 2:
        texto = input("Ingrese un texto: ")
        texto = texto.lower()
        for text in texto:
            cl += 1
            if text in "aeiouáéíóú":
                cv += 1
        print("Cantidad de vocales en el texto:", cv)
        print("Porcentaje de vocales:", (cv * 100 / cl), "%")
