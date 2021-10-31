class Nombreclase:
    def __init__(self, dato1, dato2, dato3, dato4):
        self.nombre1 = dato1
        self.nombre2 = dato2
        self.nombre3 = dato3
        self.nombre4 = dato4


def validacion(texto='Texto', num1=0, num2=12):
    numero = int(input(texto))
    while numero < num1 or numero > num2:
        numero = int(input('Error - Ingrese el numero nuevamente: '))
    return numero


def validacion_1limite(texto='Texto', num1=0):
    numero = int(input(texto))
    while numero < num1:
        numero = int(input('Error - Ingrese el numero nuevamente: '))
    return numero

def read(self, texto):
    n = len(self)
    for i in range(n):
        dato1 = input('Texto')
        dato2 = validacion()
        dato3 = float(input('Texto'))
        dato4 = float(input('Texto'))
        self[i] = Nombreclase(dato1, dato2, dato3, dato4)





def to_string(self):
    r = ''
    r += '{:<15}'.format('Dato1: ' + str(self.dato1))
    r += '{:<30}'.format('Dato2: ' + self.dato2)
    r += '{:<18}'.format('Dato3: ' + str(self.dato3))
    r += '{:<15}'.format('Dato4: ' + str(self.dato4))
    return r
