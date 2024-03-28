# Enfoque 1: usando un ciclo for para recorrer todos los números# de 1 a n y sumarlos
# 
def suma_for(n):
    suma = 0
    for i in range(1, n+1):
        suma += i
        return suma
    
# Enfoque 2: fórmula matemática para calcular la suma de# una serie aritmética
def suma_formula(n):
    return (n * (n+1)) // 2

    
import timeit

#Valor de n 
number = 1000

#Timeit #Enfoque 1
time_for = timeit.timeit(lambda: suma_for(number))
print(f"Enfoque con un ciclo for:  {time_for}")

#Timeit #Enfoque 1
time_math_formula = timeit.timeit(lambda: suma_formula(number))
print(f"Enfoque con Formula matematica:  {time_math_formula}")
