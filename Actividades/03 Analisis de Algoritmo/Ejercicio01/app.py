# Enfoque 1: usando un ciclo for
def search_for(number, numbers):
    for i in range(len(numbers)):
        if numbers[i] == number:
            return i
    return -1

# Enfoque 2: usando la función index()
def search_index(number, numbers):
    try:
        return numbers.index(number)
    except ValueError:return -1
    
import timeit

#Lista de 1000 valores
numbers = list(range(1, 1001))
#Numero a buscar
number = 1000

#Timeit #Enfoque 1
time_for = timeit.timeit(lambda: search_for(number, numbers))
print(f"Enfoque con un ciclo for:  {time_for}")

#Timeit #Enfoque 1
time_index = timeit.timeit(lambda: search_index(number, numbers))
print(f"Enfoque con index:  {time_index}")
