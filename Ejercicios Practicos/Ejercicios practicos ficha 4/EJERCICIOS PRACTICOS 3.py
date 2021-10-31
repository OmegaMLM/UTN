'''
Jornal de un operario
'''

# Carga de datos
turno = int(input('Introduzca - 1: Si trabajo en horario diurno  - \n- 2:Si trabajo '
                  'en horario nocturno: '))
horas = float(input('Introduzca la cantidad de horas trabajadas: '))

#Proceso y salida a pantalla
if turno == 1:
    print('El pago sera de:', horas * 35.50)
else:
    print('El pago sera de:', horas * 40.60)
