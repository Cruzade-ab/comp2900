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
    
