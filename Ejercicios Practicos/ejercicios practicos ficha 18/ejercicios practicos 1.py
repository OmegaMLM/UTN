'''Triatlón'''


class Competidores:
    def __init__(self, nombre, tiemponatacion, tiempociclismo, tiempocorriendo):
        self.nombre = nombre
        self.tiemponatacion = tiemponatacion
        self.tiempociclismo = tiempociclismo
        self.tiempocorriendo = tiempocorriendo


def read(competidores):
    for i in range(3):
        nombre = input('Ingrese el nombre del competidor: ')
        tiempo1 = float(input('Ingrese el tiempo de la prueba de natacion: '))
        tiempo2 = float(input('Ingrese el tiempo de la prueba de ciclismo: '))
        tiempo3 = float(input('Ingrese el tiempo de la prueba de carrera: '))
        competidores[i] = Competidores(nombre, tiempo1, tiempo2, tiempo3)


def prom(tiempo1, tiempo2, tiempo3, ):
    tiempototal = (tiempo1 + tiempo2 + tiempo3) / 3
    return tiempototal


def promdisplay(prom1, prom2, prom3, nom1, nom2, nom3):
    print('El promedio de', nom1, 'es:', prom1)
    print('El promedio de', nom2, 'es:', prom2)
    print('El promedio de', nom3, 'es:', prom3)


def podio(tiempototal1, tiempototal2, tiempototal3, nombre1, nombre2, nombre3):
    if tiempototal1 < tiempototal2 and tiempototal1 < tiempototal3:
        print('El primer lugar es para:', nombre1)
        if tiempototal2 < tiempototal3:
            print('El segundo puesto es para:', nombre2, '\nEl tercer puesto es para:', nombre3)
        else:
            print('El segundo puesto es para:', nombre3, '\nEl tercer puesto es para:', nombre2)
    elif tiempototal2 < tiempototal1 and tiempototal2 < tiempototal3:
        print('El primer lugar es para:', nombre2)
        if tiempototal1 < tiempototal3:
            print('El segundo puesto es para:', nombre1, '\nEl tercer puesto es para:', nombre3)
        else:
            print('El segundo puesto es para:', nombre3, '\nEl tercer puesto es para:', nombre1)
    elif tiempototal3 < tiempototal2 and tiempototal3 < tiempototal1:
        print('El primer lugar es para:', nombre2)
        if tiempototal1 < tiempototal2:
            print('El segundo puesto es para:', nombre1, '\nEl tercer puesto es para:', nombre2)
        else:
            print('El segundo puesto es para:', nombre2, '\nEl tercer puesto es para:', nombre1)


if __name__ == '__main__':
    competidores = [None] * 3
    read(competidores)
    prom1 = prom(competidores[0].tiemponatacion, competidores[0].tiempociclismo, competidores[0].tiempocorriendo)
    prom2 = prom(competidores[1].tiemponatacion, competidores[1].tiempociclismo, competidores[1].tiempocorriendo)
    prom3 = prom(competidores[2].tiemponatacion, competidores[2].tiempociclismo, competidores[2].tiempocorriendo)
    promdisplay(prom1, prom2, prom3, competidores[0].nombre, competidores[1].nombre, competidores[2].nombre)
    podio(prom1, prom2, prom3, competidores[0].nombre, competidores[1].nombre, competidores[2].nombre)
