def sucesion(n):
    if n % 2 == 0:
        orbita = n / 2
    else:
        orbita = 3 * n + 1
    return orbita


def mayor(may, i):
    if may < i:
        may = i
    return may


if __name__ == '__main__':
    # Init
    i = 0
    orbitan = []

    # Carga de n
    n = float(input('Ingrese el numero n: '))
    orbitan.append(n)
    promedio = n
    may = n

    # Bucle
    while i != 1:
        if len(orbitan) == 1:
            i = sucesion(n)
            orbitan.append(i)
            promedio += i
            may = mayor(may, i)
        else:
            i = sucesion(i)
            orbitan.append(i)
            promedio += i
            may = mayor(may, i)

    # Salida en pantalla
    print('El numero n es igual a:', n)
    print('Orbita de n =', orbitan)
    print('Longitud de la orbita:', len(orbitan))
    print('Promedio de todos los valores de la orbita:', promedio / len(orbitan))
    print('Numero mayor de la orbita:', may)
