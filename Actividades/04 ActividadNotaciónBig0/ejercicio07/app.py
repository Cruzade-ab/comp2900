def ejercicio_7(n):
    result = 1
    while n > 1:
        result *= n
        n -= 2
    return result