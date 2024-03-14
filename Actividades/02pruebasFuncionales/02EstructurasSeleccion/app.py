def clasificar_numero(num):
    if num > 0:return "Positivo"
    elif num < 0:return "Negativo"
    else:
        return "Cero"
    
# Prueba

assert clasificar_numero(0) == "Positivo", "La clasificación NO es correcta."