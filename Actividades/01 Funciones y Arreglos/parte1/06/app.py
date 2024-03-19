def invertir_cadena(cadena):
    nueva_cadena = ''
    for i in range(len(cadena)):
        nueva_cadena += (cadena[len(cadena)-1-i])
    return nueva_cadena

message = "El oso peresozo"

print(message)
print(invertir_cadena(message))