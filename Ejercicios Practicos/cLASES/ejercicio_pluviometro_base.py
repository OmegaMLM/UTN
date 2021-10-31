__author__ = 'Catedra de Algoritmos y Estructuras de Datos'

'''
1. Pluviómetro
Se ha solicitado un programa que permita cargar las precipitaciones promedio en cada mes del país, en base a esos datos 
  armar un menú de opciones que permita:

1 Determinar el promedio anual de lluvias
2 Determinar el promedio de lluvias para un determinado trimestre
3 Determinar el mes más seco del año
4 Determinar los meses del año en los que llovió más que el promedios de lluvia de todo el año.
'''

import random


def vector_meses():
    return ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
            'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']


def validar_rango(lim_ini, lim_fin, mensage='Ingrese un numero: '):
    numero = lim_ini - 1
    while numero < lim_ini or numero > lim_fin:
        numero = int(input(mensage))
        if numero < lim_ini or numero > lim_fin:
            print('Valor incorrecto!!! El valor debe estar comprendio entre', lim_ini, 'y', lim_fin, 'incluidos.')
    return numero


def promedio_sub_vector(vec, ind_desde, ind_hasta):
    '''
    retorna el promedio ode los elementos comprendidos entre el índice desde y el índice hasta del vector
    :param vec: vector
    :param ind_desde: índice desde de los elementos a calcular el promedio
    :param ind_hasta: índice hasta de los elementos a calcular el promedio
    :return:
    '''

    suma = contador = 0
    if ind_desde < ind_hasta and (ind_desde >= 0 and ind_desde <= len(vec)) and (
            ind_hasta >= 0 and ind_hasta < len(vec)):
        for i in range(ind_desde, ind_hasta + 1):
            suma += vec[i]
            contador += 1
        promedio = round((suma / contador), 1)
        return promedio


def determinar_promedio_trimestre(lluvias):
    '''
    retorna el promedio del trimestre que se carga por teclado
    :param lluvias: vector con las lluvias de todos los meses
    :return: trimestre cargado y promedio de lluvias de ese trimestre
    '''
    suma = contador = 0
    trimestre = validar_rango(1, 4, 'Ingrese el trimestre: ')
    promedio = promedio_sub_vector(lluvias, (trimestre - 1) * 3, ((trimestre - 1) * 3) + 2)
    return promedio, trimestre


def buscar_mes_menor_lluvia(vec):
    '''
    busca el mes de menor lluvias
    :param vec: vector con las lluvias promedio de todos los meses
    :return: més de menor lluvias.
    '''
    menor = vec[0]
    mesmenor = 0
    for i in range(1, len(vec)):
        if vec[i] < menor:
            menor = vec[i]
            mesmenor = i
    meses = vector_meses()
    return meses[mesmenor]


def mostrar_lluvias(lluvias):
    print("Lluvias anuales")
    meses = vector_meses()
    for i in range(len(lluvias)):
        print("Promedio de lluvias en el mes", meses[i], " => ", lluvias[i])
    print()


def mostrar_meses_mayores_promedio(lluvias):
    '''
    Meses con más lluvias que el promedio anual
    :param lluvias: vector con las lluvias promedio de todos los meses
    '''
    promedio = promedio_sub_vector(lluvias, 0, 11)
    meses = vector_meses()
    for i in range(len(lluvias)):
        if lluvias[i] > promedio:
            print(meses[i])



def principal():
    menu = 'Menu de Opciones \n' \
           '=================================== \n' \
           '1 \t Determinar el promedio anual de lluvias \n' \
           '2 \t Determinar el promedio de lluvias para un determinado trimestre \n' \
           '3 \t Determinar el mes más seco del mes \n' \
           '4 \t Determinar los meses con más lluvias que el promedio general \n' \
           '5 \t Mostrar lluvias mensuales \n' \
           '0 \t Salir \n ' \
           'Ingrese su opcion: '
    opcion = -1

    lluvias = [0] * 12
    for i in range(len(lluvias)):
        lluvias[i] = round((random.random() * 114.3) + 45.8, 1)  # (45.8, 160.1)

    while opcion != 0:
        opcion = validar_rango(0, 5, menu)
        if opcion == 1:
            print('Desarrollar:')
            prom = promedio_sub_vector(lluvias, 0, len(lluvias) - 1)
            print('El promedio anual de lluvias en el pais fue', prom, 'mm')
        elif opcion == 2:
            print('Desarrollar:')
            trimestre = determinar_promedio_trimestre(lluvias)
            print('El promedio de lluvias del trimestre', trimestre[0], 'fue de', trimestre[1], 'mm')
        elif opcion == 3:
            print('Desarrollar:')
            menor = vector_meses()
            print('El mes con menor lluvia registrada fue', menor[buscar_mes_menor_lluvia(lluvias)])
        elif opcion == 4:
            print('Desarrollar:')
            mostrar_meses_mayores_promedio(lluvias)
        elif opcion == 5:
            mostrar_lluvias(lluvias)


if __name__ == '__main__':
    principal()
