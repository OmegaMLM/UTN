"""
Validación Datos Personales
"""
#Estructura opciones
opc = 1
while opc != 3:
    print("Menu de opciones: \n 1 - Validacion de CUIT."
          "\n 2 - Validar DNI.")
    opc = int(input("Ingrese una opcion: "))
    while opc <= 0 or opc > 3:
        opc = int(input("Error - Ingrese una opción valida: "))
#Opcion 1
"""
if opc == 1:
    acumulador = posicion =0
# Ingreso de CUIT
    cuit = int(input("Ingrese su CUIT: "))
# Validación CUIT
    cuitstr = str(cuit)
    while len(cuitstr) != 13 or cuitstr[2] != "-" or cuitstr[11] != "-":
        cuit = input("Erro - Mal ingreso de CUIT. Ingrese su CUIT: ")
# Validación digito verificador
    for numero in cuitstr:
        while numero != "-":
            posicion += 1
            if posicion != 3 or posicion != 12:
                acumulador +=  * 5432765432
                resto = (acumulador % 11)
                dv = 11 - resto
                print(dv)
"""
#Opcion 3
if opc == 2:
    dni = input("Ingrese su dni:")
    while len(dni) >= 9:
