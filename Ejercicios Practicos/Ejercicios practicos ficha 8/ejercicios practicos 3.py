"""
Secuencia de n números
"""
nt5 = nt = cr = numeroanterior = nm = 0
numero1 = False
n = int(input("Ingrese la cantidad de numeros de la secuencia: "))
if n > 0:
    for i in range(1, n + 1):
        numero = int(input("Ingrese un numero: "))
        nt += 1
        # Cuántos números ingresados terminan en 5
        if (numero - 5) % 2 == 0:
            nt5 += 1
        # La cantidad de veces que aparece el primer número ingresado por el usuario en la secuencia
        if nt == 1:
            numero1 = True
            pn = numero
            numeroanterior = numero
        elif pn == numero:
            cr += 1
        # Cuántos números ingresados son mayores al anterior
        if numero > numeroanterior:
            nm += 1
        numeroanterior = numero
    print(pn)
    print("Numeros terminados en 5:", nt5)
    print("Cantidad de veces que aparece el primer numero:", cr)
    print("Numeros mayores al anterior:", nm)
