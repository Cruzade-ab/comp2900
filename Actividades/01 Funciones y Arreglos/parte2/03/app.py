def invertir_elementos(array):
    nuevo_array = []
    for i in range(len(array)):
        nuevo_array.append(array[len(array)-1-i])
    return nuevo_array

array = [1,2,3,4,5,6,7]

print(array)
print(invertir_elementos(array))