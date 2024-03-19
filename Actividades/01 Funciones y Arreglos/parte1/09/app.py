#Integrando random

import random

def generar_numeros_aleatorios(cantidad, maximo,minimo):
    arrayAleatorio = []
    for n in range(cantidad):
        number = random.randint(minimo, maximo)
        arrayAleatorio.append(number)
    return arrayAleatorio

cantidad = 22
minimo = 1
maximo = 100

print(f"Array generado: {generar_numeros_aleatorios(cantidad, maximo, minimo)}")