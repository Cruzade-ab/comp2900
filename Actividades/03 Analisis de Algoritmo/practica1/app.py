# Enfoque 1: usando un ciclo for
def sum_even_numbers_for(numbers):
    total = 0
    for number in numbers:
        if number % 2 == 0:
            total += number
            return total

# Enfoque 2: usando sum() y una expresión generadora (lambda)

def sum_even_numbers_genexp(numbers):return sum(number for number in numbers if number % 2 == 0)


import timeit

# Crear una lista de números del 1 al 1000
numbers = list(range(1, 1001))

# Medir el tiempo de ejecución del Enfoque 1
time_for =timeit.timeit(lambda: sum_even_numbers_for(numbers), number=10000)
print("Enfoque 1: ", time_for)

# Medir el tiempo de ejecución del Enfoque 2

time_genexp =timeit.timeit(lambda: sum_even_numbers_genexp(numbers),number=10000)
print("Enfoque 2: ", time_genexp)
