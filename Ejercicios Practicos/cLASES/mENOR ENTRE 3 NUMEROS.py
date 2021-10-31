a = int(input('N1: '))
b = int(input('N2: '))
c = int(input('N3: '))

if a < b and a < c:
    men = a
elif b < a and b < c:
    men = b
else:
    men = c
print(men)


