def sumar_elementos_arreglo(arreglo):
    suma = 0 
    for element in arreglo:
        suma = element + suma
    
    return suma

arreglo = [88,65,3,2,34]

print(f"El resultado de {sumar_elementos_arreglo(arreglo)}")

