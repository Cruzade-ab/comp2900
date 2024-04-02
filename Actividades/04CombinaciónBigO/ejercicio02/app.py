def ejercicio_2(n):
    i = 1
    while n > 1:
        n = n / 2
        i += 1
    for i in range(n):
        print(i)
    return i