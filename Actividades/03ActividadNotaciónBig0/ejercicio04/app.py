def ejercicio_4(n):
    if n <= 1:
        return n
    else:
        return ejercicio_4(n-1) + ejercicio_4(n-2)