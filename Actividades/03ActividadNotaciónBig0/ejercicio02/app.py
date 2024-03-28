def ejercicio_2(lista):
    total = 0
    for i in lista:
        for j in lista:
            total += i * j
    return total