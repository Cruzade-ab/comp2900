#Encontrar indice de elemento en la lista
def encontrar_indice(lista, elemento):
    for i in lista:
        if lista[i] == elemento:
            return i
    return -1

lista = [1,2,3,4,5,6]
elemento = 6

resultado = encontrar_indice(lista, elemento)

if resultado == -1:
    print("Elemento no encontrado.")
else:
    print(f"Elemento encontrado en el indice: {resultado}")