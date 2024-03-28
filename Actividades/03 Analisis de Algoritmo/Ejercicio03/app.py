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
        
        
import timeit


#Lista de numeros 
numbers = list(range(1,1001))


#MaxNumber #1
maxNumber = max_lista(numbers)
#Enfoque 1 Resultado
print(f"Enfoque 1 resultado: {maxNumber}")
#Timeit #Enfoque 1
time_max = timeit.timeit(lambda: max_lista(numbers))
print(f"Enfoque con un max:  {time_max}")




#MaxNumber #2
maxNumber = max_iterativo(numbers)
time_iterative = timeit.timeit(lambda: max_iterativo(numbers))
print(f"Enfoque con Iteraciones:  {time_iterative}")
#Enfoque 1 Resultado
print(f"Enfoque 2 resultado: {maxNumber}")