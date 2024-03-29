def ejercicio_1(lista):
    suma = 0
    for num in lista:
        suma += num
        for i in lista:
            for j in lista:
                suma += i * j
    return suma