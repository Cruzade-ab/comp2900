def ejercicio_8(lista):
    mid = len(lista) // 2
    left = lista[:mid]
    right = lista[mid:]
    return left, right
