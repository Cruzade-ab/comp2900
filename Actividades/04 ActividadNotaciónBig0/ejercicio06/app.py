def ejercicio_6(lista):
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista