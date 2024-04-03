def coeficiente_binomial(n, k):
    # Casos base
    if k == 0 or k == n:
        return 1
    # Paso recursivo
    else:
        return coeficiente_binomial(n - 1, k) + coeficiente_binomial(n - 1, k - 1)

 
print(coeficiente_binomial(5, 2))  
print(coeficiente_binomial(6, 3))  
print(coeficiente_binomial(10, 5)) 
