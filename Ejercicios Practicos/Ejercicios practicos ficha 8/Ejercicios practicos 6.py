"""
Menú de opciones y validación
"""
import random

# Estructura Opciones
cn = tn = cp = cneg = 0
opc = 1
while opc != 4:
    print("Menu de opciones: \n1 - Cargar numeros y calcular su promedio. "
          "\n2 - Generar n valores entre -100 y 100. Determinar cantidad positivos y negativos."
          "\n3 - Cargar la nota de un alumno e informar si esta aprobado."
          "\n4 - Salir.")
    opc = int(input("Ingrese una opción: "))
    while opc <= 0 or opc > 4:
        opc = int(input("Error - Ingrese una opción valida: "))
    # Opción 1
    if opc == 1:
        numero = float(input("Ingrese un numero (con -1 finaliza): "))
        while numero != -1:
            cn += 1
            tn += numero
            numero = int(input("Ingrese un numero (con -1 finaliza): "))
        print("El promedio de todos los numeros es:", tn / cn)
    # Opción 2
    if opc == 2:
        n = int(input("Ingrese la cantidad de numeros aleatorios: "))
        for i in range(n):
            aleatorios = random.randint(-100, 100)
            if aleatorios >= 0:
                cp += 1
            else:
                cneg += 1
        print("La cantidad de numeros positivos son:", cp,
              "\n La cantidad de numeros negativos son:", cneg)
    # Opción 3
    if opc == 3:
        nota = float(input("Ingrese la nota del alumno: "))
        while nota < 0:
            nota = float(input("Error - Ingrese una nota entre 0 y 10: "))
        if nota >= 4:
            print("El alumno esta aprobado.")
        else:
            print("El alumno esta desaprobado.")
