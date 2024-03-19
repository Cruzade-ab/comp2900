def contar_carracter_string(string, element):
    conteo = 0
    for n in string:
        if n == element:
            conteo += 1
    return conteo


string = "Cuantas veces la letra a esta repetida???"
element = "a"

print(f"El caracter {element} existe {contar_carracter_string(string, element)} veces, en el string: {string}")