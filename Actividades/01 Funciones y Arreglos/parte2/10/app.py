array = [11,22,33,44,55]

lastElement = array[-1]

for i in range(len(array)-1, 0, -1):
    array[i] = array[i-1]
array[0] = lastElement

print("Arreglo con los elementos rotados a la derecha:", array)