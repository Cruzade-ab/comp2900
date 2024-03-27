# Enfoque 1: Utilizando la función max() de Python para encontrar el# número más grande en una lista.
def max_lista(lista):
    return max(lista)

# Enfoque 2: Recorriendo la lista y comparando cada número con un valor# de referencia para encontrar el número más grande
def max_iterativo(lista):
    maximo = lista[0]
    for numero in lista:
        if numero > maximo:
            maximo = numero
            return maximo
