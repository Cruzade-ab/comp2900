array = [22, 33,  44, 55, 66 ,77 ,88, 99]

conteo = 0 
suma = 0 
for n in array:
    suma += n
    conteo += 1

promedio = suma / conteo 

print(f"El promedio del array: {array}, tiene un promedio de: {promedio}")