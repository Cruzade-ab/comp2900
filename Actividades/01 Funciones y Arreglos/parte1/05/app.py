#Encontrar indice de elemento en la lista
def encontrar_indice(lista, elemento):
    global element 
    element = int(elemento)
    
    for i in range(len(lista)):
        if (element == lista[i]):
            for j in range(len(lista)):    
                if (element == lista[j]):
                    return print(element)
                return print("00")
        return print("-1")
        
                
encontrar_indice([2,3,4,5,6,7,8], 7)