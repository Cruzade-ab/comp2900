def promedio(lista_numeros):
    suma = sum(lista_numeros)
    lenght = len(lista_numeros)
        
    promedio = suma / lenght
    
    return print(f"El promedio de la lista es {promedio}")

promedio([2,3,4,2,1,4,5,5,6,7,7])