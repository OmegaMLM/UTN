"""
Ejercicio Tipo Parcial 1 (Resuelto 1K3)
"""
# Contadores y Acumuladores
tn = m3 = tnacumulados = m3acumulados = sc = 0
# Estructurá Opciones
opc = 1
while opc != 4:
    print("Menu de opciones:"
          "\n1 - Barcos."
          "\n2 - Secuencia de numeros."
          "\n3 - Cadena de caracteres."
          "\n4 - Salir.")
    opc = int(input("Ingrese una opcion: "))
    while opc < 1 or opc > 4:
        opc = int(input("Error - Ingrese una opcion valida: "))
    # Opcion 1
    if opc == 1:
        t1 = int(input("Ingrese el tiempo del primer barco: "))
        t2 = int(input("Ingrese el tiempo del segundo barco: "))
        t3 = int(input("Ingrese el tiempo del tercer barco: "))
        if t1 <= t2 and t1 <= t3:
            print("El ganador es el primer barco con un tiempo de :", t1, "segundos")
            print("Diferencias de tiempo:"
                  "\nCon el segundo barco -", t2 - t1,
                  "\nCon el tercer barco -", t3 - t1)
        elif t2 <= t1 and t2 <= t3:
            print("El ganador es el segundo barco con un tiempo de :", t2, "segundos")
            print("Diferencias de tiempo:"
                  "\nCon el primer barco -", t1 - t2,
                  "\nCon el tercer barco -", t3 - t2)
        elif t3 <= t1 and t3 <= t2:
            print("El ganador es el tercer barco con un tiempo de :", t3, "segundos")
            print("Diferencias de tiempo:"
                  "\nCon el primer barco -", t3 - t1,
                  "\nCon el segundo barco -", t3 - t2)
    # Opcion 2
    if opc == 2:
        n = int(input("Ingrese la cantidad de numeros enteros: "))
        while n == 0:
            n = int(input("Se ingreso 0, ingrese un numero mayor: "))
        for num in range(1, n + 1):
            tn += 1
            tnacumulados += num
            if num % 3 == 0:
                m3 += 1
                m3acumulados += num
        print("La cantidad de numeros multiplos de 3 son:", m3)
        promtn = tnacumulados / tn
        promm3 = m3acumulados / m3
        print(tn)
        if promm3 < promtn:
            print("El promedio de numeros multiplos de 3 es menor.")
        elif promm3 == promtn:
            print("El promedio de numeros multiplos de 3 es igual.")
        elif promm3 > promtn:
            print("El promedio de numeros multiplos de 3 es mayor.")
    # Opción 3
    if opc == 3:
        texto = input("Ingrese una cadena de caracteres: ")
        for text in texto:
            if text in "0123456789":
                sc += int(text)
        print("La suma de los digitos en el texto es: ", sc)
