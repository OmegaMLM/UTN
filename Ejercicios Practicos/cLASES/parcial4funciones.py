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

def write(self):
    print("\nCodigo:", self.codigo, end=' ')
    print("- Nombre:", self.nombre, end=' ')
    print("- Costo:", self.costo, end=' ')
    print("- Tipo", self.tipo, end=' ')
    print("- Material", self.material, end=' ')


def add_in_order(array, self):
    n = len(array)
    pos = n
    for i in range(n):
        if self.hist_clinica < array[i].hist_clinica:
            pos = i
            break

    array[pos:pos] = [self]

#Binary search
def add_in_order2(array, self):
    izq, der = 0, len(array) - 1
    while izq <= der:
        c = (izq + der) // 2
        if self.isbn == array[c].isbn:
            return c

        if self.isbn < array[c].isbn:
            der = c - 1
        else:
            izq = c + 1
            break


def read(array):
    n = int(input('Cantidad de elementos: '))
    for i in range(n):
        dato1 = input('Texto')
        dato2 = validacion()
        dato3 = float(input('Texto'))
        dato4 = float(input('Texto'))
        self = Nombreclase(dato1, dato2, dato3, dato4)
        add_in_order(array, self)
        print()
    return array

def read2(array):
    n = int(input('Cantidad de elementos: '))
    m = open(fd, 'wd')
    for i in range(n):
        dato1 = input('Texto')
        dato2 = validacion()
        dato3 = float(input('Texto'))
        dato4 = float(input('Texto'))
        self = Nombreclase(dato1, dato2, dato3, dato4)
        pickle.dump(self, m)
        print()
    return array


def crear_archivo(self):
    fd = input('Ingrese el nombre del archivo: ')
    if not os.path.exists(fd):
        m = open(fd, 'wb')
        t = validacion('Ingrese el tipo: ', 0, 4)
        for emb in self:
            if t == emb.codigo:
                pickle.dump(emb, m)
        m.close()

    else:
        print('El archivo ya existe')


def mostrar_archivo(self):
    fd = input('Ingrese el nombre del archivo: ')
    if os.path.exists(fd):
        m = open(fd, 'rb')
        tam = os.path.getsize(fd)
        while m.tell() < tam:
            reg = pickle.load(m)
            registro.write(reg)
        m.close()
    else:
        print('No existe el archivo')


def crear_matriz(self, cant1, cant2):
    mat = [[0] * cant1 for i in range(cant2)]
    for reg in self:
        fil = reg.dato1
        col = reg.dato2
        mat[fil][col] += reg.dato3
    return mat

def mostrar_matriz(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            #mat[i] dato1
            #mat[j] dato2
            #mat[i][j] dato3