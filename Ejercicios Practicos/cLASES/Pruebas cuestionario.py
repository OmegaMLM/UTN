def registrar(a, c):
    reg = []
    for i in range(a):
        for j in range(c):
            reg[i][j] = 50

    return reg

if __name__ == '__main__':
    print(registrar(5,5))