array = [33, 44, 55, 22, 11, 22, 44, 6, 62, 23, 34, 65, 68, 7, 53, 4, 4, 8, 9]

print(f"Array original: {array}")

n = len(array)
for i in range(n):
    for j in range(0, n - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]

print(f"Array ordenado: {array}")
