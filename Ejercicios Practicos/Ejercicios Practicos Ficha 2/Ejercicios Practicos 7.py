va = int(input('Ingresar el total de votos a favor: '))
vc = int(input('Ingresar el total de votos en contra: '))
vt = va + vc
pva = (va * 100) / vt
pvc = 100 - pva
print('Votos a favor = %', pva, 'Votos en contra', pvc)
