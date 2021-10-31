'''Analizando Temperaturas'''


class Temperaturas:
    def __init__(self, region, mes, tempmax, tempmin):
        self.region = region
        self.mes = mes
        self.tempmax = tempmax
        self.tempmin = tempmin


def read(analisis):
    n = len(analisis)
    for i in range(n):
        region = input('Ingrese el nombre de la region: ')
        mes = validacion()
        tempmax = float(input('Ingrese la temperatura maxima: '))
        tempmin = float(input('Ingrese la temperatura minima: '))
        analisis[i] = Temperaturas(region, mes, tempmax, tempmin)


def validacion():
    numero = int(input('Ingrese un mes entre 1 y 12: '))
    while numero < 1 or numero > 12:
        numero = int(input('Numero equivocado, ingrese un numero entre 1 y 12: '))
    return numero


def tempmax(analisis):
    temperaturas = 0
    n = len(analisis)
    cantidad = 0
    for i in range(n):
        if not analisis[i].mes < 1 or analisis[i].mes > 6:
            cantidad += 1
            temperaturas += analisis[i].tempmax
    print(temperaturas)
    prom = promedio(temperaturas, cantidad)
    return prom


def promedio(numero1, numero2):
    if numero2 != 0:
        numero = numero1 / numero2
        return numero
    else:
        return "Sin posible calculo"


def menormin(analisis):
    n = len(analisis)
    for i in range(n):
        if i == 0:
            menorminima = analisis[i].tempmin
            indicemenor = i
        elif menorminima > analisis[i].tempmin:
            menorminima = analisis[i].tempmin
            indicemenor = i

    return indicemenor


def display(analisis, indicemenor):
    print('La temperatura minima del año se registro en', analisis[indicemenor].region,
          'En el mes', analisis[indicemenor].mes)


def write(empleado):
    print("\nRegion:", empleado.region, end=' ')
    print("- Mes:", empleado.mes, end=' ')
    print("- Temp. Max:", empleado.tempmax, end=' ')
    print("- Temp. Min:", empleado.tempmin, end=' ')


def opcion1(analisis):
    read(analisis)
    n = len(analisis)
    for i in range(n):
        write(analisis[i])


def opcion2(analisis):
    prom = tempmax(analisis)
    print('La temperatura maxima del primer promedio fue de:', prom, 'Grados')


def opcion3(analisis):
    indicemenor = menormin(analisis)
    display(analisis, indicemenor)


def test():
    op = 0
    while op != 4:
        print('1. Cargar análisis térmicos')
        print('2. Informar promedio maximo del primer semestre')
        print('3. Informar region y mes de la menor minima del año')
        print('4. Salir')
        op = int(input('Ingrese opción: '))
        if op == 1:
            n = int(input('Ingrese el numero de análisis térmicos: '))
            analisis = [None] * n
            opcion1(analisis)
        elif op == 2:
            opcion2(analisis)
        elif op == 3:
            opcion3(analisis)


if __name__ == '__main__':
    test()
