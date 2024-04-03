def mcd(a, b):
    # Caso base: 
    if b == 0:
        return a
    # Recursivo: 
    else:
        return mcd(b, a % b)

def mcd_detallado(a, b):
    resultado = mcd(a, b)
    print(f"MCD de {a} y {b} es {resultado}")
    if b != 0:
        print(f"Aplicando mcd({b}, {a} % {b}) = mcd({b}, {a % b})")
        mcd_detallado(b, a % b)


mcd_detallado(48, 18)
print()
mcd_detallado(150, 305)
