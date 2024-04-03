#Escribe una función recursiva que calcule la suma de los primeros n números naturales. 
def suma(n):
    #Caso Base
    if n == 1:
        return 1 
    #Recursivo
    else:
        return n + suma( n - 1 )

def suma_detallada(n, nivel=1):
    resultado = suma(n)
    print(f"Valor de n: {n}, suma total: {resultado}")
    if n > 1:
        suma_detallada(n - 1, nivel + 1)

suma_detallada(5)
print("")
print("")
suma_detallada(10)