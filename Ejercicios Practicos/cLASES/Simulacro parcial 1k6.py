"""
Simulacro Parcial 1 1K6
"""
# Contadores
corredores = totaltiempo = sumatexto = 0

# Estructura Opciones
opc2 = 1
opc = 1
while opc != 3:
    print("Menu de opciones:"
          "\n1 - Análisis de temperaturas."
          "\n2 - Análisis de carrera o Análisis de texto."
          "\n3 - Salir.")
    opc = int(input("Ingrese una opción: "))
    # Validación
    while opc < 1 or opc > 3:
        opc = int(input("Error - Ingrese una opción valida: "))
        # Opción 1
    if opc == 1:
        # Entrada de datos
        frio = int(input("Ingrese el Frio Record: "))
        nombre1 = input("Ingrese el nombre de la primera provincia: ")
        temp1 = int(input("Ingrese la temperatura de la primera provincia: "))
        nombre2 = input("Ingrese el nombre de la segunda provincia: ")
        temp2 = int(input("Ingrese la temperatura de la segunda provincia: "))
        nombre3 = input("Ingrese el nombre de la tercera provincia: ")
        temp3 = int(input("Ingrese la temperatura de la tercera provincia: "))
        # Proceso entre temperaturas
        if temp1 < temp2 and temp1 < temp3:
            print("La temperatura minima es de la provincia:", nombre1, "con", temp1, "Grados")
        elif temp2 < temp1 and temp2 < temp3:
            print("La temperatura minima es de la provincia:", nombre2, "con", temp2, "Grados")
        elif temp3 < temp1 and temp3 < temp2:
            print("La temperatura minima es de la provincia:", nombre3, "con", temp3, "Grados")
        # Proceso entre temperaturas y Frio record
        if temp1 < frio:
            print("La provincia de", nombre1, "tuvo la temperatura mas baja de la historia.")
        elif temp2 < frio:
            print("La provincia de", nombre2, "tuvo la temperatura mas baja de la historia.")
        elif temp3 < frio:
            print("La provincia de", nombre3, "tuvo la temperatura mas baja de la historia.")
    # SubOpciones
    if opc == 2:
        while opc2 != 3:
            print("Menu de opciones 2:"
                  "\n1 - Análisis de Carrera."
                  "\n2 - Análisis de Texto."
                  "\n3 - Volver.")
            opc2 = int(input("Ingrese una opción: "))
            # Validación
            while opc2 < 1 or opc2 > 3:
                opc2 = int(input("Error - Ingrese una opción valida: "))
            # Opción 2a
            if opc2 == 1:
                # Cantidad de corredores
                n = int(input("Ingrese la cantidad de corredores: "))
                # Ciclo
                for runners in range(0, n):
                    # Entrada de datos
                    tiempo = int(input("Ingrese el tiempo del corredor (en segundos): "))
                    totaltiempo += tiempo
                    corredores += 1
                    # Procesos mas rapido y mas lento
                    if corredores == 1:
                        ganador = tiempo
                        perdedor = tiempo
                    elif tiempo < ganador:
                        ganador = tiempo
                    elif tiempo > perdedor:
                        perdedor = tiempo
                # Salida en pantalla
                promedio = totaltiempo / corredores
                d = int(input("Ingrese la diferencia: "))
                print("El ganador tuvo un tiempo de:", ganador, "segundos.")
                print("El mas lento tuvo un tiempo de:", perdedor, "segundos.")
                if ganador < d:
                    print("Tiempo Sobresaliente.")
            # Opción 2b
            if opc2 == 2:
                # Ingreso de datos
                texto = input("Ingrese el texto: ")
                # Ciclo
                for text in texto:
                    # Proceso del texto
                    if text == "2" or text == "4" or text == "6" or text == "8":
                        sumatexto += int(text)
                # Salida en pantalla
                print("La suma de los numeros pares es:", sumatexto)
