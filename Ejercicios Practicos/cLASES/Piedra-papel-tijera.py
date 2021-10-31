'''
Piedra-Pape;-Tijera
'''
import random

opciones = 'Piedra', 'Papel', 'Tijera', 'Lagarto', 'Spock'

print('*******************************')
print('** Juego Piedra Papel Tijera **')
print('*******************************')

nombre = input('Como te llamas? ')
print('Ok', nombre, 'Vamos a jugar...')
opc_usuario_nro = int(
    input('Hace tu juego\n\t1 - Piedra' + '\n\t2 - Papel\n\t3 - Tijera\n\t4 - Lagarto\n\t5 - Spock \n\tTu opción: '))

opc_usuario = opciones[opc_usuario_nro - 1]
print('Bien, elegiste: ', opc_usuario)
opc_compu = random.choice(opciones)
print('Yo elijo:', opc_compu)

if opc_usuario == opc_compu:
    resultado = 'Empatamos'
    print()
elif opc_usuario == ('Piedra' and opc_compu == 'Tijera') or (opc_usuario == 'Tijera' and opc_compu == 'Papel') \
        or (opc_usuario == 'Papel' and opc_compu == 'Piedra') or (opc_usuario == 'Piedra' and opc_compu == 'Lagarto') \
        or (opc_usuario == 'Lagarto' and opc_compu == 'Spock') or (opc_usuario == 'Spock' and opc_compu == 'Tijera') \
        or (opc_usuario == 'Tijera' and opc_compu == 'Lagarto') or (opc_usuario == 'Lagarto' and opc_compu == 'Papel') \
        or (opc_usuario == 'Papel' and opc_compu == 'Spock') or (opc_usuario == 'Spock' and opc_compu == 'Piedra') \
        or (opc_usuario == 'Piedra' and opc_compu == 'Tijeras'):
    resultado = 'Me ganaste'
else:
    resultado = 'Gane'
print(resultado)
