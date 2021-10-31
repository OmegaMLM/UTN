'''Trafico de Red'''
import random


class Registros:
    def __init__(self, dato1, dato2, dato3):
        self.ipenvia = dato1
        self.iprecibe = dato2
        self.bytes = dato3


def generate():
    ips = '172.20.4.11', '172.18.1.196', '172.18.1.54', '172.20.4.13', '172.20.4.20'
    return ips


def read(self, ips):
    n = len(self)
    for i in range(n):
        ipenvio = random.choice(ips)
        iprecibe = random.choice(ips)
        informacion = str(random.randint(1000000, 1000000000000))
        self[i] = Registros(ipenvio, iprecibe, informacion)


def menordatos(self):
    n = len(self)
    for i in range(n):
        if i == 0:
            datosmenos = self[i].bytes
            indice = i
        elif datosmenos > self[i].bytes:
            datosmenos = self[i].bytes
            indice = i
    return indice


def to_string(self):
    r = ''
    r += '{:<1}'.format('Ips host: ' + str(self.ipenvia))
    r += '{:^60}'.format('Ips receptor: ' + str(self.iprecibe))
    r += '{:>1}'.format('Bytes de información: ' + str(self.bytes))
    return r


def validacion(num1, num2):
    numero = int(input('Ingrese un numero de las opciones: '))
    while numero < num1 or numero > num2:
        numero = int(input('Error -- Ingrese un numero de las opciones: '))
    return numero


def selection_sort(v):
    # ordenamiento por seleccion directa
    n = len(v)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i].ipenvia > v[j].ipenvia:
                v[i], v[j] = v[j], v[i]


def binary_search(v, x):
    # búsqueda binaria... asume arreglo ordenado...
    izq, der = 0, len(v) - 1
    while izq <= der:
        c = (izq + der) // 2
        if x == v[c]:
            return c
        if x < v[c]:
            der = c - 1
        else:
            izq = c + 1
    return -1


def linear_search(v, x):
    # busqueda secuencial...
    for i in range(len(v)):
        if x == v[i]:
            return i
    return -1


def opcion1():
    ip = input('Ingrese una ip: ')
    indice = linear_search(registro, ip)
    write(registro[indice])
    print(' ')


def opcion2():
    pass


def write(self):
    print("\nIp host:", self.ipenvia, end=' ')
    print("- Ip receptor:", self.iprecibe, end=' ')
    print("- Informacion:", self.bytes, end=' ')


if __name__ == '__main__':
    ips = generate()
    n = int(input('Ingrese la cantidad de registros: '))
    print('{:^100}'.format('Creado base de datos'))
    registro = [None] * n
    read(registro, ips)
    selection_sort(registro)
    for i in range(n):
        print(to_string(registro[i]))
    print('')
    op = 0
    while op != 3:
        print('1. Imprimir bytes de una ip')
        print('2. Datos de registro con menor informacion')
        print('3. Salir')
        op = validacion(1, 3)

        if op == 1:
            opcion1()
        elif op == 2:
            opcion2()
