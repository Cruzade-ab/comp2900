def contar_vocales(string):
    
    vocales = "aeiouAEIOU"
    contadorVocales = 0
    
    for caracter in string: 
        if caracter in vocales:
            contadorVocales += 1
    return contadorVocales

string = "Cuantas Vocales Habra?"
print(f"Hay {contar_vocales(string)} vocales.")