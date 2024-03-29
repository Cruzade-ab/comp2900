def ejercicio_3(lista):
    total = 0
    for i in lista:
        for j in lista:total += i * j
        mid = len(lista) // 2
        left = lista[:mid]
        right = lista[mid:] # O(n/2)
        return left, right, total