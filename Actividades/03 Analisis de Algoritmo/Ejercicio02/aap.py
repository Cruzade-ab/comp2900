# Enfoque 1: usando un ciclo for para recorrer todos los números# de 1 a n y sumarlos
# 
def suma_for(n):
    suma = 0
    for i in range(1, n+1):
        suma += i
        return suma
    
# Enfoque 2: fórmula matemática para calcular la suma de# una serie aritmética
def suma_formula(n):return (n * (n+1)) // 2
