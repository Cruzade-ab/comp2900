def potencia(base, exponente):
    # Caso base: 
    if exponente == 0:
        return 1
    # Recursivo:
    else:
        return base * potencia(base, exponente - 1)

def potencia_detallada(base, exponente):
    resultado = potencia(base, exponente)
    print(f"{base} elevado a la potencia de {exponente} es {resultado}")
    if exponente > 0:
        potencia_detallada(base, exponente - 1)


potencia_detallada(2, 3)
print("")
potencia_detallada(3, 4)
