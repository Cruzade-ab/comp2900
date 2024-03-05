##Calcular el maximo de dos numeros

def maximo(a,b):
    array = [a,b]
    array.sort
    maxValueIndex = len(array) -1
    return print(f"El maximo de los numberos es {array[maxValueIndex]}")

maximo(3,5)