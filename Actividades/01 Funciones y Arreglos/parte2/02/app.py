
def mayor(lista):
    valor_mayor = lista[0]
    for n in lista:
        if (n > valor_mayor):
            valor_mayor = n
    return valor_mayor



lst = [10, 4, 3, 15, 9, 22, 221, 1, 22, 12]

print(lst)

print(f'El valor maximo es {mayor(lst)}')