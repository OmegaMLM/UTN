'''
Censo
'''

# Carga de datos
sexo = input('Ingrese sus sexo, M/H: ')
edad = int(input('Ingrese su edad: '))
mujeres = 0
hombres = 0
viejo = 'No'
edadescolar = 0
while sexo == 'M' or sexo == 'H':
    if sexo == 'M':
        mujeres += 1
    else:
        hombres += 1
    if 4 <= edad <= 18:
        edadescolar += 1
    if edad >= 80 and sexo == 'H':
        viejo = 'Si'
    else:
        viejo = 'No'
    sexo = input('Ingrese sus sexo, M/H: ')
    edad = int(input('Ingrese su edad: '))
if mujeres > hombres:
    print('Mayor cantidad de mujeres que de hombres')
else:
    print('Mayor cantidad de hombres que de mujeres')
print('La cantidad de niños en edad escolar es de:', edadescolar)
print(viejo, 'hay algún varón que supere los 80 años de edad')
