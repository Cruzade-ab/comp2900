def invertir_cadena(cadena):
    # Caso base: 
    if len(cadena) <= 1:
        return cadena
    # Paso recursivo: 
    else:
        return cadena[-1] + invertir_cadena(cadena[:-1])

# Probando la función con el mensaje dado
message1 = "El oso peresozo"
cadena_invertida1 = invertir_cadena(message1)

message2 = "La ave voladora"
cadena_invertida2 = invertir_cadena(message2)

print(cadena_invertida1)
print("")
print(cadena_invertida2)

