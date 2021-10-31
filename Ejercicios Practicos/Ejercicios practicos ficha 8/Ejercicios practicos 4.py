"""
Secuencia numérica II
"""
nm = nt = nd = ni = csi = tnm = 0
numeros = int(input("Ingrese un numero(con 0 finaliza): "))
while numeros != 0:
    nt += 1
    # El promedio de los números que son múltiplos de 6
    if numeros % 6 == 0:
        nm += 1
        tnm += numeros
    #  Cantidad de números que son divisor exacto del anterior
    if nt == 1:
        numeroanterior = numeros
    elif numeros % numeroanterior == 0:
        nd += 1
    numeroanterior = numeros
    # Indicar la cantidad de veces que se generó una secuencia ascendente de 3 o más números impares
    if numeros % 2 != 0:
        ni += 1
        if ni == 3:
            csi += 1
    else:
        ni = 0
    numeros = int(input("Ingrese un numero(con 0 finaliza): "))
print("Promedio de los numeros que son multiplos de 6:", tnm / nm)
print("Cantidad de números que son divisor exacto del anterior:", nd)
print("Cantidad de secuencia ascendente de impares:", csi)
