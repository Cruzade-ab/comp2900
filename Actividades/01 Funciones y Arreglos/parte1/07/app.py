def es_numero_entero(string):
    
    try:
        int(string)
        return True
    except ValueError:
        return False
    

string1 = "100"
string2 = "String"

print(es_numero_entero(string1))
print(es_numero_entero(string2))
