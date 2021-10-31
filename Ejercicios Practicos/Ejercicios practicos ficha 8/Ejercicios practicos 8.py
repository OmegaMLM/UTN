"""
Menu de Opciones con Secuencias
"""
nt = nm = letras = palabras = 0
# Estructura Opciones
opc = 1
while opc != 4:
    print("Menu de opciones: \n 1 - Determinar la cantidad de numeros de una secuencia los "
          "multiplos de 3 y 5."
          "\n 2 - Determinar cuantas palabras con mas de 4 letras hay en un texto."
          "\n 3 - Indicar el alumno con peor nota de tres."
          "\n 4 - Salir.")
    opc = int(input("Ingrese una opción: "))
    while opc < 1 or opc > 4:
        opc = int(input("Error - Ingrese una opción correcta:"))
    # Opcion 1
    if opc == 1:
        numero = int(input("Ingrese un numero (con numeros iguales o menores a 0 termina): "))
        while numero <= 0:
            numero = int(input("Error - Ingrese al menos un numero "
                               "(con numeros iguales o menores a 0 termina): "))
        while numero > 0:
            nt += 1
            if numero % 3 == 0 or numero % 5 == 0:
                nm += 1
            numero = int(input("Ingrese un numero (con numeros iguales o menores a 0 termina): "))
        print("La cantidad de numeros multiplos de 3 y 5 es:", nm)
        print("El porcentaje de multiplos sobre los totales es:", str((nm * 100) / nt) + "%")
    # Opcion 2
    if opc == 2:
        texto = input("Ingrese un texto (que termine con punto): ")
        texto = texto.lower()
        for text in texto:
            if text == ".":
                break
            elif text != " ":
                letras += 1
                if letras == 5:
                    palabras += 1
            elif text == " ":
                letras = 0
        print("Cantidad de palabras con mas de 4 letras:", palabras)
    # Opcion 3
    if opc == 3:
        alumno1 = int(input("Ingrese la nota final del primer alumno: "))
        alumno2 = int(input("Ingrese la nota final del segundo alumno: "))
        alumno3 = int(input("Ingrese la nota final del tercer alumno: "))
        if alumno1 < alumno2 and alumno1 < alumno3:
            print("El alumno 1 tiene la peor nota.")
        elif alumno2 < alumno1 and alumno2 < alumno3:
            print("El alumno 2 tiene la peor nota.")
        elif alumno3 < alumno1 and alumno3 < alumno2:
            print("El alumno 3 tiene la peor nota.")
