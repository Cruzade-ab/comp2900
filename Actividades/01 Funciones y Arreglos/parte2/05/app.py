def eliminar_elemento_array(array, elemento):
    arrayActualizado = [num for num in array if num != elemento]
    
    return arrayActualizado

array = [22,33,44,55,66,77,88]
elemento = 44

print(f"Del array: {array}, se elimino el elemento: {elemento}")
print(eliminar_elemento_array(array,elemento))