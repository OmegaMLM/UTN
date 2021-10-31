def linear_search(v, x):
    # busqueda secuencial...
    for i in range(len(v)):
        if x == v[i]:
            return i
    return -1

def selection_sort(v):
    # ordenamiento por seleccion directa
    n = len(v)
    for i in range(n-1):
        for j in range(i+1, n):
            if v[i] > v[j]:
                v[i], v[j] = v[j], v[i]

def binary_search(v, x):
    izq, der = 0, len(v) - 1
    while izq <= der:
        c = (izq + der) // 2
        if x == v[c]:
            return c

        if x < v[c]:
            der = c - 1
        else:
            izq = c + 1
    return -1