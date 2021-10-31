"""
Secuencia numérica
"""
# Carga de datos
nt = ni = cn = numeroanterior = mi = pn = 0
numero1 = False
numero = int(input("Ingrese un numero (con 0 finaliza): "))
while numero != 0:
    nt += 1
# Porcentaje numeros impares
    if numero % 3 == 0:
        ni += 1
# Determinar la cantidad de números que son el cuadrado del número anterior
    if nt == 1:
        numeroanterior = numero
        numero1 = True
    if numero == numeroanterior ** 2:
        cn += 1
    numeroanterior = numero
# Determinar la posición del mayor elemento impar de la secuencia
    if numero % 2 != 0:
        if mi < numero:
            mi = numero
            pn = nt
    numero = int(input("Ingrese un numero (con 0 finaliza): "))
print("Porcentaje de numeros impares sobre los numeros totales:", (ni * 100) / nt)
print("Cantidad de numeros que son el cuadrado del anterior:", cn)
print("Posicion del mayor elemento impar:", pn)





