"""
Otro Ejercicio Tipo Parcial (Resuelto 1K14)
"""
nintervalo = npar = nacumuladoint = cm = 0
# Estructura Opciones
opc = 1
while opc != 3:
    print("Menu de opciones: "
          "\n1 - Análisis de secuencia de numeros."
          "\n2 - Calculo de producción agropecuario."
          "\n3 - Salir.")
    opc = int(input("Ingrese una opción: "))
    while opc < 1 or opc > 3:
        opc = int(input("Error - Ingrese una opción correcta: "))
    # Opción 1
    if opc == 1:
        numero = float(input("Ingrese un numero (con 0 termina): "))
        while numero != 0:
            if numero > 15 and numero < 25:
                nintervalo += 1
                nacumuladoint += numero
                if nintervalo == 0:
                    print("No se ingreso ningún numero en el intervalo.")
                if numero % 2 == 0:
                    npar += 1
            numero = float(input("Ingrese un numero (con 0 termina): "))
        if nintervalo == 0:
            print("No se ingreso ningún numero en el intervalo.")
        else:
            print("Promedio del intervalo 15 y 25:", nacumuladoint / nintervalo)
    # Opcion 2
    if opc == 2:
        provincia1 = float(input("Ingrese la cantidad de tonelada de granos de la primera "
                                 "provincia: "))
        provincia2 = float(input("Ingrese la cantidad de tonelada de granos de la segunda "
                                 "provincia: "))
        provincia3 = float(input("Ingrese la cantidad de tonelada de granos de la tercera "
                                 "provincia: "))
        promedio = (provincia1 + provincia2 + provincia3) / 3
        if provincia1 > promedio:
            cm += 1
        if provincia2 > promedio:
            cm += 1
        if provincia3 > promedio:
            cm += 1
        print("El promedio de producción de las 3 provincias es de:", round(promedio, 2))
        print("Cantidad de provincias que producieron mas que el promedio:", cm)
