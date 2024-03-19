# Python program to get average of a list 
def promedio(lista_numeros):
    suma = 0  
    array_length = 0  
    
    for element in lista_numeros:
        suma = suma + element 
        array_length = array_length + 1  #   ctr++
    return (suma / array_length)


list = [15, 9, 55, 41, 35, 20, 62, 49] 

# Version del Curso
print(list)
print(f'El valor promedio de la lista es {promedio(list)}')