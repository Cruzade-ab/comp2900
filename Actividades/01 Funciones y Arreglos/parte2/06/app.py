def contar_elemento_array(array, element):
    conteo = 0
    for n in array:
        if n == element:
            conteo += 1
    return conteo

array = [11,22,33,44,55,55,55,55,55,33,22,11,11,22,11]
element = 11

print(f"El elemento {element} existe {contar_elemento_array(array, element)} veces, en el array : {array}")